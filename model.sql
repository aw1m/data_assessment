--drop TABLE IF  EXISTS users;
--
--CREATE TABLE IF NOT EXISTS users (
--username varchar(36) PRIMARY KEY,
--given_name text NULL,
--family_name text NULL,
--profession text NULL,
--created_date datetime null
----possible modified date
--);

drop TABLE IF  EXISTS questions;

CREATE TABLE IF NOT EXISTS questions (
uuid varchar(36) PRIMARY KEY,
type text NULL,
body text NULL,
has_correctness bool NULL,
created_at datetime NULL,
deleted_at datetime NULL
--possible modified date
);
--
--drop TABLE IF  EXISTS choices;
--
--CREATE TABLE IF NOT EXISTS choices (
--uuid varchar(36) ,
--question_uuid varchar(36),
--is_correct bool null,
----possible body or desc,
--created_at datetime NULL,
--deleted_at datetime NULL
----possible modified date
--PRIMARY KEY (uuid, question_uuid)
--);

