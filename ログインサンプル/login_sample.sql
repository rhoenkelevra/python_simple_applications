DROP DATABASE IF EXISTS login_sample;
CREATE DATABASE IF Not EXISTS login_sample;

use login_sample;

DROP TABLE IF EXISTS user;

CREATE TABLE
 user
 (
  user_id int AUTO_INCREMENT,
  id varchar(255) NOT NULL,
  name varchar(255) NOT NULL,
  pass varchar(20) NOT NULL,
  d_flg tinyint(1) NOT NULL,
  PRIMARY KEY (user_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO user(id, name, pass, d_flg) values('yamadada@abc.com', '山田 太郎', 'pass', 0);
