from .conn import run_query

def get_course_quizes(course_id):
    query = f"""
    SELECT * FROM Quiz
    WHERE course_id='{course_id}'
    """
    return run_query(query)

def get_student_course_quizes(course_id, st_id):
    return run_query(f"""
    SELECT Q.*, S.score
    FROM SCORE S
    INNER JOIN QUIZ Q ON(S.quiz_id = Q.quiz_id)
    WHERE S.ST_ID={st_id} 
    AND S.quiz_id IN (
        SELECT quiz_id FROM Quiz
        WHERE course_id='{course_id}'
    )
    """)


def create_quiz(course_id, name):
    query = f"""
    INSERT INTO QUIZ (quiz_id, quiz_title, course_id)
    VALUES (S_QUIZ_ID.NEXTVAL, '{name}', '{course_id}') 
    """
    run_query(query)

def create_quiz_student_score(quiz_id):
    query= f"""
    INSERT INTO SCORE(quiz_id, st_id)
    SELECT Q.quiz_id, SC.st_id
    FROM QUIZ Q, Student_Course SC
    WHERE Q.course_id=SC.course_id AND Q.quiz_id={quiz_id}
    """
    return run_query(query)

def delete_quiz(quiz_id):
    query = f"""
    DELETE FROM QUIZ WHERE quiz_id={quiz_id}
    """
    return run_query(query)

def get_quiz_id():
    return run_query(f"""
    SELECT S_QUIZ_ID.NEXTVAL
    FROM DUAL
    """)[0][0] - 1

def get_quiz_detail(quiz_id):
    return run_query(f"""
    SELECT * FROM QUIZ
    WHERE QUIZ_ID={quiz_id}
    """)[0]


def get_quiz_questions(quiz_id):
    return run_query(f"""
    SELECT * FROM QUESTION
    WHERE QUIZ_ID={quiz_id}
    """)

def get_quiz_students_score(quiz_id):
    return run_query(f"""
    SELECT SC.ST_ID, ST.NAME, SC.score 
    FROM SCORE SC 
    INNER JOIN STUDENT ST 
    ON(SC.st_id = ST.st_id) 
    WHERE SC.quiz_id={quiz_id} 
    """)

def quiz_update_score(quiz_id, st_id, score):
    return run_query(f"""
    UPDATE SCORE
    SET score={score}
    WHERE quiz_id={quiz_id} AND st_id={st_id}
    """)

