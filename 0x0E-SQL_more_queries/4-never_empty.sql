-- Creates table 'id_not_null' on a db passed as arg of the command 'mysql'.

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);

