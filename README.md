# EduGrader

**Requirements for running the project:**

```
pip install -r requirements.txt
```
```
CREATE DATABASE edugrader;
USE edugrader;

CREATE TABLE user (
    id INT PRIMARY KEY,
    username varchar(50),
    password varchar(50),
    email varchar(50)
);

create table history(
	qno int primary key,
    question varchar(1500),
    answer varchar(1500),
    feedback varchar(1500),
    marks int
);

ALTER TABLE history ADD COLUMN user_id INT;

ALTER TABLE history
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id) REFERENCES user(id);

select *  from user;

select * from history;

![Homepage](https://github.com/user-attachments/assets/d69b5507-3587-4b6b-80a9-5d904e4ba60f)

