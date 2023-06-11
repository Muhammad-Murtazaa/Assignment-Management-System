-- Table Creation
DROP TABLE Score;
DROP TABLE Choices;
DROP TABLE Question;
DROP TABLE Quiz;
DROP TABLE Student_Course;
DROP TABLE Course;
DROP TABLE Teacher;
DROP TABLE Student;
-- Teacher
CREATE TABLE Teacher (
    th_id number(10) NOT NULL PRIMARY KEY,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL
);

--Course table
CREATE TABLE Course (
    course_id varchar2(255) NOT NULL PRIMARY KEY,
    name varchar2(255) NOT NULL,
    th_id number(10) NOT NULL,

    CONSTRAINT course_thid_FK FOREIGN KEY(th_id) REFERENCES Teacher(th_id)
);

-- Student Table
CREATE TABLE Student (
    st_id number(10) NOT NULL PRIMARY KEY,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL
);

-- Student_Course Table
CREATE TABLE Student_Course (
    course_id varchar(255),
    st_id number(10),

    CONSTRAINT student_course_course_FK FOREIGN KEY(course_id)
        REFERENCES Course(course_id),
    CONSTRAINT student_course_student_FK FOREIGN KEY(st_id)
        REFERENCES Student(st_id)
);

-- Quiz Table
CREATE TABLE Quiz (
    quiz_id number(10) NOT NULL PRIMARY KEY,
    quiz_title varchar(255) NOT NULL,
    course_id varchar(255) NOT NULL,

    CONSTRAINT quiz_course_FK FOREIGN KEY(course_id)
        REFERENCES Course(course_id)
);

-- Question Table
CREATE TABLE Question (
    question_id number(10) NOT NULL PRIMARY KEY,
    question_title varchar(255) NOT NULL,
    question_type varchar(255) NOT NULL,
    quiz_id number(10) NOT NULL,
    answer varchar(255) NOT NULL,

    CONSTRAINT question_quiz_FK FOREIGN KEY(quiz_id)
        REFERENCES Quiz(quiz_id)
);

-- Choices Table
CREATE TABLE Choices (
    choices_id number(10) NOT NULL PRIMARY KEY,
    choices_title varchar(255) NOT NULL,
    question_id number(10) NOT NULL,
    ordering_id varchar(1) NOT NULL,

    CONSTRAINT choices_question_FK FOREIGN KEY(question_id)
        REFERENCES Question(question_id)
);

-- Score Table
CREATE TABLE Score (
    st_id number(10) NOT NULL,
    quiz_id number(10) NOT NULL,
    score number(10),

    CONSTRAINT score_student_FK FOREIGN KEY(st_id)
        REFERENCES Student(st_id),
    CONSTRAINT score_quiz_FK1 FOREIGN KEY(quiz_id)
        REFERENCES Quiz(quiz_id)
);

-- Indexes
-- FOr Quiz ID
DROP SEQUENCE S_QUIZ_ID;
CREATE SEQUENCE S_QUIZ_ID
INCREMENT BY 1
START WITH 1;

-- FOr Question Id
DROP SEQUENCE S_QUESTION_ID;
CREATE SEQUENCE S_QUESTION_ID
INCREMENT BY 1
START WITH 1;

-- For Choices
DROP SEQUENCE S_CHOICES_ID;
CREATE SEQUENCE S_CHOICES_ID
INCREMENT BY 1
START WITH 1;

-- Trigger

DROP TRIGGER T_QUIZ;
CREATE OR REPLACE TRIGGER T_QUIZ
BEFORE DELETE OR INSERT ON QUIZ
FOR EACH ROW
BEGIN
IF INSERTING THEN
    INSERT INTO SCORE(quiz_id, st_id)
    SELECT Q.quiz_id, SC.st_id
    FROM QUIZ Q, Student_Course SC
    WHERE Q.course_id=SC.course_id AND Q.quiz_id = :new.quiz_id;
ELSIF DELETING THEN
    DELETE FROM QUESTION
    WHERE quiz_id = :old.quiz_id;
    DELETE FROM SCORE
    WHERE QUIZ_id = :old.quiz_id;
END IF;
END;
/
DROP TRIGGER T_QUESTION;
CREATE OR REPLACE TRIGGER T_QUESTION
BEFORE DELETE ON QUESTION
FOR EACH ROW
BEGIN
IF DELETING THEN
    DELETE FROM CHOICES
    WHERE question_id = :old.question_id;
  END IF;
END;


