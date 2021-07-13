drop TABLE IF  EXISTS users;

CREATE TABLE IF NOT EXISTS users (
username varchar(36) PRIMARY KEY,
given_name text NULL,
family_name text NULL,
profession text NULL,
created_at datetime null
--possible modified and deleted
);

drop TABLE IF  EXISTS questions;

CREATE TABLE IF NOT EXISTS questions (
uuid varchar(36) ,
type text NULL,
body text NULL,
has_correctness bool NULL,
choice_uuid  varchar(36),
is_correct bool NULL,
created_at datetime NULL,
deleted_at datetime NULL,
--possible modified
PRIMARY KEY(uuid, choice_uuid)
);

drop TABLE IF  EXISTS questionnaire;

CREATE TABLE IF NOT EXISTS questionnaire (
uuid varchar(36) ,
name text NULL,
context text NULL,
question_uuid  varchar(36),
is_required bool NULL,
created_at datetime NULL,
--possible modified date
PRIMARY KEY(uuid, question_uuid)
);
