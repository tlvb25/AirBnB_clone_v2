-- create A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user hbnb_dev ans set password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges for hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
