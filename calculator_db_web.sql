-- CREATE DATABASE calculator_web_db; 
USE calculator_web_db;
-- DROP TABLE user_history;
DROP TABLE user_logs;
CREATE TABLE user_logs(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) UNIQUE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- CREATE TABLE user_history(
-- user_id INT AUTO_INCREMENT PRIMARY KEY,
-- id INT,
-- calculations VARCHAR(1000) NOT NULL,
-- CONSTRAINT fk_user FOREIGN KEY(id) REFERENCES user_logs(id) ON DELETE CASCADE,
-- calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
-- SELECT * FROM user_logs;
-- DROP TABLE user_history;
-- CREATE TABLE user_history(
--   history_id INT AUTO_INCREMENT PRIMARY KEY, -- unique per calculation
--   user_id INT NOT NULL,                      -- links to user_logs
--   calculations VARCHAR(1000) NOT NULL,
--   calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--   CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES user_logs(id) ON DELETE CASCADE
-- );
SELECT * FROM user_logs;