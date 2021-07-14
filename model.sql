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

drop TABLE IF  EXISTS questionnaire_attempt;

CREATE TABLE IF NOT EXISTS questionnaire_attempt (
user_uuid  varchar(36) ,
activity_uuid  varchar(36) ,
questionnaire_uuid  varchar(36) ,
attempt_number int NULL,
submitted_at datetime NULL,
created_at datetime NULL,
updated_at datetime NULL,
deleted_at datetime NULL,
context_uuid  varchar(36) ,
question_uuid  varchar(36) ,
confidence text NULL,
type text NULL,
single_answer_choice_uuid  varchar(36),
PRIMARY KEY(user_uuid, activity_uuid,questionnaire_uuid,attempt_number,context_uuid,question_uuid,single_answer_choice_uuid)
);

--
--user-uuid : b044ebb4-d149-4285-aac3-9fc679769ff0
--activity-uuid : 7ea971c3-d894-43dd-8d56-aa8fb725ea01
--questionnaire-uuid : d2ef56cf-c8ed-4bf1-9be2-0a074218bcf2
--attempt-number : 1
--submitted-at : None
--created-at : 2021-05-18T13:48:27.497Z
--updated-at : None
--deleted-at : None
--context_uuid : bca6450b-2787-43ae-b392-9f5e0d463472
--question_uuid : b34ab717-0389-44f4-975f-0b2a9d1580af
--confidence : unsure
--type : single-answer
--single_answer_choice_uuid : 62548b52-1640-4f07-91ab-a019ecb9d3c2