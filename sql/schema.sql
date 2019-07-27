DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tweets;

CREATE TABLE users(
  fullname VARCHAR(50) NOT NULL,
  username VARCHAR(15) NOT NULL,
  email VARCHAR(20),
  password VARCHAR(256) NOT NULL,
  filename VARCHAR(64) NOT NULL,
  totaltweets INTEGER DEFAULT 0,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(username)
);

CREATE TABLE tweets(
  originalOwner VARCHAR(15) NOT NULL, /* The person who first tweeted this tweet */
  body VARCHAR(256) NOT NULL,
  tweetid VARCHAR(20) NOT NULL,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  owner VARCHAR(15) NOT NULL,
  retweet BOOLEAN NOT NULL,
  likes INTEGER DEFAULT 0,
  PRIMARY KEY(tweetid),
  FOREIGN KEY (owner) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE
);