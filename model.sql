drop TABLE IF  EXISTS users;

CREATE TABLE IF NOT EXISTS users (
username varchar(36) PRIMARY KEY,
given_name text NULL,
family_name text NULL,
profession text NULL,
created_date datetime null
);


