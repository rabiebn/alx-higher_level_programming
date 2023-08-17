-- Creates table 'unique_id' on a db passed as arg of the command 'mysql'.

CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);

