import os
import fwitter
from fwitter.db import get_db
import pytest
from flask import session

class TestTweets():
    """Testing api calls related to tweeting"""

    def test_post_tweet(self, app, client, cookie):
        """Testing that a user can correctly add to the tweet table"""

        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        cookie.login(test_username, test_password)

        body = 'The first tweet!'
       
        with client:
           client.post('/api/v1/tweet', data={'body': 'The first tweet!'})

           cur = get_db().cursor()
           cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format(test_username, test_password))

           data1 = cur.fetchall()

           assert not data1[0]['retweet']

           # TODO find what tweetid should be and test for it
           # Test to ensure tweets with identical bodies and owners have separate tweetids
        
           client.post('/api/v1/tweet', data={'body': 'The first tweet!'})

           cur.execute("SELECT * FROM TWEETS WHERE owner='{}' AND body='{}'".format(test_username, test_password))

           data2 = cur.fetchall()

           assert data1[0]['tweetid'] != data2[0]['tweetid']

    
    def test_get_tweet(self, app, client, cookie):
        """Test that a user can fetch a requested tweet"""

        test_username = 'osagie_01'
        test_password = 'thisIsATestPassword'

        cookie.login(test_username, test_password)

        with client:
            response = client.get('/api/v1/tweet?tweetid=1')






