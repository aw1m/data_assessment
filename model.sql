drop TABLE IF  EXISTS users;

CREATE TABLE IF NOT EXISTS users (
username varchar(36) PRIMARY KEY,
given_name text NULL,
family_name text NULL,
profession text NULL,
created_date datetime null
--possible modified date
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
--possible modified date
PRIMARY KEY(uuid, choice_uuid)
);


--
--
--    "uuid": "8176b7e9-9a1d-4814-b04f-4195c48b7791",
--    "type": "single-answer",
--    "body": "meh",
--    "has-correctness": true,
--    "choice_uuid": "78b11006-c81c-46ad-9684-c36dcdbeb40e",
--
--    "created-at": "2019-07-17T16:23:02.190Z",
--    "deleted-at": null