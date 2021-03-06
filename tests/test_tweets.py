"""Testing api calls related to tweeting."""
import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session
import pdb

class TestTweets():
    """Testing api calls related to tweeting."""

    def test_post_tweet(self, app, client, cookie):
        """Testing that a user can correctly add to the tweet table."""
        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        # Test that posting fails when a user is not logged in
        with client:
            response = client.post('/api/v1/tweet', json={'body': 'This should fail'})
            assert response.status_code == 403

        cookie.login(test_username, test_password)
        # This is actually the second tweet, test.sql already added one
        body = 'The first tweet!'
       
        with client:
            # Test that posting fails with no body provided
            response = client.post('/api/v1/tweet')
            assert response.status_code == 403

            response = client.post('/api/v1/tweet', json={'body': body})
            client.post('/api/v1/tweet', json={'body': 'The first tweet!'})
            assert response.status_code == 201

            cursor = get_db()
            cur = cursor.execute("SELECT * FROM tweets WHERE owner='{}' AND body='{}'".format(test_username, body))

            data1 = cur.fetchall()

            assert data1[0]['body'] == body

            assert data1[0]['tweetid'] == '2'
            # Test to ensure tweets with identical bodies and owners have separate tweetids
        

            cur = cursor.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format(test_username, 'The first tweet!'))

            data2 = cur.fetchall()

            assert data1[0]['tweetid'] != data2[1]['tweetid']
            assert data2[1]['tweetid'] == '3'
        
        cookie.logout()

    
    def test_get_tweet(self, app, client, cookie):
        """Test that a user can fetch a requested tweet."""

        with client:
            # Test that response fails when a tweetid param isn't supplied
            response = client.get('/api/v1/tweet')
            assert response.status_code == 403

            # Test that response fails when the tweet isn't found
            response = client.get('/api/v1/tweet?tweetid=1000000')
            assert response.status_code == 404

            response = client.get('/api/v1/tweet?tweetid=1')
            test_json = response.get_json()

            assert test_json['tweetid'] == '1'
            assert test_json['owner'] == 'osagie01'
            assert test_json['body'] == 'Hopefully this passes pytest'
        
        cookie.logout()

    
    def test_retweet(self, app, client, cookie):
        """Test that a user can retweet any tweet."""
        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        cookie.login(test_username, test_password)

        with client:
           client.post('/api/v1/tweet', json={'body': 'I hope somone retweets this!'})

        cookie.logout()

        cookie.login('osagie01', test_password)

        with client:
            # Test that tweet data is either body or id, but not both
            response = client.post('/api/v1/tweet', json={'id' : 1, 'body': 'This should fail' })
            assert response.status_code == 403
            
            response = client.post('/api/v1/tweet', json={'tweet': 'This should fail' })
            assert response.status_code == 403

            client.post('/api/v1/tweet', json={'id' : 2 })

            cur = get_db().cursor()
            cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format('osagie01', 'I hope somone retweets this!'))

            data = cur.fetchall()

            assert data[0]['originalOwner'] == 'osagie_01'
            assert data[0]['tweetid'] != 2

        cookie.logout()

    def test_like_tweet(self, app, client, cookie):
        """Test that a user can like a tweet."""
        test_username = 'osagie01'
        test_password = 'thisIsATestPassword'

        with app.app_context():
            cur = get_db().cursor()
            # Check that a logged out user cannot like a tweet
            response = client.patch('/api/v1/tweet', json={'tweetid': 1 })
            assert response.status_code == 403

            cur.execute("SELECT * FROM tweets WHERE tweetid=1")
            data1 = cur.fetchall()

            like_check = data1[0]['likes']

            assert like_check == 0

            cookie.login(test_username, test_password)
            cur = get_db().cursor()
            # Check that post fails if tweet isn't found
            response = client.patch('/api/v1/tweet', json={'tweetid': 100000000 })
            assert response.status_code == 404

            # Check that post fails with no id field
            response = client.patch('/api/v1/tweet', json={'test': 100000000 })
            assert response.status_code == 403

            response = client.patch('/api/v1/tweet', json={ })
            assert response.status_code == 403

            response = client.patch('/api/v1/tweet')
            assert response.status_code == 403

            # Check that post fails with multiple fields
            response = client.patch('/api/v1/tweet', json={'tweetid': 1, 'body': 'This should fail' })
            assert response.status_code == 403

            # Test normal like
            response = client.patch('/api/v1/tweet', json={'tweetid': 1 })
            assert response.status_code == 202

            cur.execute("SELECT * FROM tweets WHERE tweetid=1")
            data2 = cur.fetchall()

            assert data2[0]['likes'] == 1

            cur.execute("SELECT * FROM likes WHERE tweetid='{}' and owner='{}'".format(1, test_username))
            data2 = cur.fetchall()

            assert len(data2) > 0

            # Check that the same user cannot like the same tweet more than once
            response = client.patch('/api/v1/tweet', json={'tweetid': 1 })
            assert response.status_code == 403

        cookie.logout()
    
    def test_delete_tweet(self, app, client, cookie):
        """Test that a user can delete their own tweet"""
        test_username = 'osagie01'
        test_password = 'thisIsATestPassword'

        # Test that a logged out user cannot delete a tweet
        with client:
            response = client.delete('/api/v1/tweet', json={'tweetid': 1})
            assert response.status_code == 403

        # Test that a logged in user cannot delete a tweet that isn't theirs
        cookie.login('osagie_01', test_password)
        
        with client:
            response = client.delete('/api/v1/tweet', json={'tweetid': 1})
            assert response.status_code == 403
        
        cookie.logout()

        cookie.login(test_username, test_password)

        with client:
            # Test that a tweet cannot be deleted with an invalid request
            response = client.delete('/api/v1/tweet', json={'id': 1})
            assert response.status_code == 403

            response = client.delete('/api/v1/tweet')
            assert response.status_code == 403

            # Test that a non existent tweet can't be deleted
            response = client.delete('/api/v1/tweet', json={'tweetid': 100000})
            assert response.status_code == 404

            # Normal test
            response = client.patch('/api/v1/tweet', json={'tweetid': 1 })
            assert response.status_code == 202

            response = client.delete('/api/v1/tweet', json={'tweetid': 1})
            assert response.status_code == 204

            cur = get_db().cursor()
            cur.execute("SELECT * FROM tweets WHERE tweetid=1")
            data1 = cur.fetchall()

            assert len(data1) == 0
            
            # Assert that a like on the deleted tweet is removed from the database
            cur.execute("SELECT * FROM likes WHERE tweetid='{}' and owner='{}'".format(1, test_username))
            data2 = cur.fetchall()

            assert len(data2) == 0
        
        cookie.logout()

    def test_remove_tweet_like(self, app, client, cookie):
        """Test that a user can remove a like from a tweet"""
        test_username = 'osagie01'
        test_password = 'thisIsATestPassword'

        cookie.login(test_username, test_password)

        with app.app_context():
           client.patch('/api/v1/tweet', json={'tweetid': 1 })
        
        cookie.logout() 
        # Assert that a logged out user cannot remove a like
        response = client.delete('/api/v1/tweet', json={'like_tweetid': 1})
        assert response.status_code == 403

        cookie.login(test_username, test_password)
        
        with client:
            # Test that a like cannot be deleted with invalid data
            response = client.delete('/api/v1/tweet', json={'likeid': 1})
            assert response.status_code == 403

            # Test that a like cannot be deleted when the tweet is not found
            response = client.delete('/api/v1/tweet', json={'like_tweetid': 100000})
            assert response.status_code == 404

            # Normal test
            response = client.delete('/api/v1/tweet', json={'like_tweetid': 1})
            assert response.status_code == 204

            cur = get_db().cursor()
            cur.execute("SELECT * FROM likes WHERE tweetid='{}' AND owner='{}'".format(1, test_username))
            data1 = cur.fetchall()

            assert len(data1) == 0
        
        cookie.logout()