-- Grant privileges to user_0d_1
CREATE USER 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Grant privileges to user_0d_2
CREATE USER 'user_0d_2'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'user_0d_2'@'localhost';

-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
