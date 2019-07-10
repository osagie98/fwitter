DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tweets;

CREATE TABLE users(
  fullname VARCHAR(50) NOT NULL,
  username VARCHAR(15) NOT NULL,
  email VARCHAR(20),
  password VARCHAR(256) NOT NULL,
  filename VARCHAR(64) NOT NULL,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(username)
);

CREATE TABLE tweets(
  body VARCHAR(256) NOT NULL,
  filename VARCHAR(64) NOT NULL,
  tweetid VARCHAR(20) NOT NULL,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  owner VARCHAR(10) NOT NULL,
  retweet BOOLEAN NOT NULL,
  PRIMARY KEY(tweetid),
  FOREIGN KEY (owner) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE
);