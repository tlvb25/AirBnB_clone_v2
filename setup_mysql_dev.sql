-- create A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user hbnb_dev ans set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges for hbnb_dev
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- grant select privileges
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
