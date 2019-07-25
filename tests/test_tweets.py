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

        cookie.login(test_username, test_password)
        # This is actually the second twee, test.sql already added one
        body = 'The first tweet!'
       
        with client:
           client.post('/api/v1/tweet', data={'body': body})

           cur = get_db().cursor()
           cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format(test_username, test_password))

           data1 = cur.fetchall()

           assert not data1[0]['retweet']

           assert data1[0]['body'] == body

           # TODO find what tweetid should be and test for it
           assert data1[0]['tweetid'] == 2
           # Test to ensure tweets with identical bodies and owners have separate tweetids
        
           client.post('/api/v1/tweet', data={'body': 'The first tweet!'})

           cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format(test_username, 'The first tweet!'))

           data2 = cur.fetchall()

           assert data1[0]['tweetid'] != data2[0]['tweetid']
        
        cookie.logout()

    
    def test_get_tweet(self, app, client, cookie):
        """Test that a user can fetch a requested tweet."""
        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        cookie.login(test_username, test_password)

        with client:
            response = client.get('/api/v1/tweet?tweetid=1')
            assert False
        
        cookie.logout()

    
    def test_retweet(self, app, client, cookie):
        """Test that a user can retweet any tweet."""
        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        cookie.login(test_username, test_password)

        with client:
           client.post('/api/v1/tweet', data={'body': 'I hope somone retweets this!',
           'retweet': False})

        cookie.logout()

        cookie.login('osagie01', test_password)

        with client:
            client.post('/api/v1/tweet', data={'id' : 1 })

            cur = get_db().cursor()
            cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format('osagie01' 'The first tweet!'))

            data = cur.fetchall()

            assert data[0]['original_owner'] == 'osagie_01'

        assert False





