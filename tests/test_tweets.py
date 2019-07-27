"""Testing api calls related to tweeting."""
import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session

class TestTweets():
    """Testing api calls related to tweeting."""

    def test_post_tweet(self, app, client, cookie):
        """Testing that a user can correctly add to the tweet table."""
        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        # Test that posting fails when a user is not logged in
        with client:
            response = client.post('/api/v1/tweet', data={'body': 'This should fail'})
            assert response.status_code == 403

        cookie.login(test_username, test_password)
        # This is actually the second tweet, test.sql already added one
        body = 'The first tweet!'
       
        with client:
            # Test that posting fails with no body provided
            response = client.post('/api/v1/tweet')
            assert response.status_code == 403

            response = client.post('/api/v1/tweet', data={'body': body})
            assert response.status_code == 201

            cur = get_db().cursor()
            cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format(test_username, test_password))

            data1 = cur.fetchall()

            assert not data1[0]['retweet']

            assert data1[0]['body'] == body

            assert data1[0]['tweetid'] == 2
            # Test to ensure tweets with identical bodies and owners have separate tweetids
        
            client.post('/api/v1/tweet', data={'body': 'The first tweet!'})

            cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format(test_username, 'The first tweet!'))

            data2 = cur.fetchall()

            assert data1[0]['tweetid'] != data2[0]['tweetid']
            assert data2[0]['tweetid'] == 3
        
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
            print(test_json)

            assert test_json['tweetid'] == 1
            assert test_json['owner'] == 'osagie01'
            assert test_json['body'] == 'Hopefully this passes pytest'
        
        cookie.logout()

    
    def test_retweet(self, app, client, cookie):
        """Test that a user can retweet any tweet."""
        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        cookie.login(test_username, test_password)

        with client:
           client.post('/api/v1/tweet', data={'body': 'I hope somone retweets this!'})

        cookie.logout()

        cookie.login('osagie01', test_password)

        with client:
            # Test that tweet data is either body or id, but not both
            response = client.post('/api/v1/tweet', data={'id' : 1, 'body': 'This should fail' })
            assert response.status_code == 403
            
            response = client.post('/api/v1/tweet', data={'tweet': 'This should fail' })
            assert response.status_code == 403

            client.post('/api/v1/tweet', data={'id' : 2 })

            cur = get_db().cursor()
            cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format('osagie01', 'I hope somone retweets this!'))

            data = cur.fetchall()

            assert data[0]['original_owner'] == 'osagie_01'
            assert data[0]['tweetid'] != 2

        cookie.logout()

    def test_like_tweet(self, app, client, cookie):
        """Test that a user can like a tweet."""
        test_username = 'osagie01'
        test_password = 'thisIsATestPassword'

        # Check that a logged out user cannot like a tweet
        response = client.patch('/api/v1/like_tweet', data={'id': 1 })
        assert response.status_code == 403

        cookie.login(test_username, test_password)

        cur = get_db().cursor()
        cur.execute("SELECT * FROM TWEETS WHERE id=1")
        data1 = cur.fetchall()

        like_check = data1[0]['id']

        assert like_check == 0

        with client:
            # Check that post fails if tweet isn't found
            response = client.patch('/api/v1/tweet', data={'id': 100000000 })
            assert response.status_code == 404

            # Check that post fails with no id field
            response = client.patch('/api/v1/tweet', data={'test': 100000000 })
            assert response.status_code == 403

            response = client.patch('/api/v1/tweet', data={ })
            assert response.status_code == 403

            response = client.patc('/api/v1/tweet')
            assert response.status_code == 403

            # Check that post fails with multiple fields
            response = client.patch('/api/v1/ttweet', data={'id': 1, 'body': 'This should fail' })
            assert response.status_code == 404

            # Test normal like
            response = client.patch('/api/v1/tweet', data={'id': 1 })
            assert response.status_code == 202

            cur.execute("SELECT * FROM TWEETS WHERE id=1")
            data2 = cur.fetchall()

            assert data2[0]['likes'] == 1
            # TODO find out how to store likes
            cur.execute("SELECT * FROM likes WHERE tweetid=1 and owner=")
            data2 = cur.fetchall()

            # Check that the same user cannot like the same tweet more than once
            response = client.patch('/api/v1/tweet', data={'id': 1 })
            assert response.status_code == 403

        cookie.logout()
    
    def test_delete_tweet(self, app, client, cookie):
        """Test that a user can delete their own tweet"""