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
choice_uuid  varchar(36),
type text NULL,
body text NULL,
has_correctness bool NULL,
is_correct bool NULL,
created_at datetime NULL,
deleted_at datetime NULL,
--possible modified
PRIMARY KEY(uuid, choice_uuid)
);

drop TABLE IF  EXISTS questionnaire;

CREATE TABLE IF NOT EXISTS questionnaire (
uuid varchar(36) ,
question_uuid  varchar(36),
name text NULL,
context text NULL,
is_required bool NULL,
created_at datetime NULL,
--possible modified date
PRIMARY KEY(uuid, question_uuid)
);

drop TABLE IF  EXISTS questionnaire_attempt;

CREATE TABLE IF NOT EXISTS questionnaire_attempt (
user_uuid  varchar(36) ,
activity_uuid  varchar(36) ,
questionnaire_uuid  varchar(36) ,
context_uuid  varchar(36) ,
question_uuid  varchar(36) ,
single_answer_choice_uuid  varchar(36),
attempt_number int NULL,
confidence text NULL,
type text NULL,
submitted_at datetime NULL,
created_at datetime NULL,
updated_at datetime NULL,
deleted_at datetime NULL,
PRIMARY KEY(user_uuid, activity_uuid,questionnaire_uuid,context_uuid,question_uuid,single_answer_choice_uuid,attempt_number)
);


