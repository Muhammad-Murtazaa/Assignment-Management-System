from .conn import run_query


def get_question_id():
    return run_query(f"""
    SELECT S_QUESTION_ID.NEXTVAL
    FROM DUAL
    """)[0][0] - 1

def get_question(question_id):
    query = f"""
    SELECT * FROM QUESTION WHERE question_id={question_id}
    """
    return run_query(query)[0]

def create_question_choices(question_id, data):
    ordering = ['A', 'B', 'C', 'D']
    for i in range(len(ordering)):
        query = f"""
        INSERT INTO CHOICES (choices_id, choices_title, question_id, ordering_id) 
        VALUES (S_CHOICES_ID.NEXTVAL, '{data.getlist('choice')[i]}', {question_id}, '{ordering[i]}')
        """
        run_query(query)
    return

def get_question_choices(question_id):
    query = f"""
    SELECT * FROM CHOICES WHERE question_id={question_id} ORDER BY ordering_id
    """
    return run_query(query)

def create_question(quiz_id, question_type, data):
    query = f"""
    INSERT INTO Question (question_id, question_title, QUESTION_TYPE, QUIZ_ID, ANSWER)
    VALUES (S_QUESTION_ID.NEXTVAL, '{data["question"]}', '{question_type}', {quiz_id}, '{data["answer"]}') 
    """
    run_query(query)
    if question_type == 'MCQS':
        create_question_choices(get_question_id(), data)
    return 

def delete_question(question_id):
    query = f"""
    DELETE FROM QUESTION WHERE question_id={question_id} 
    """
    return run_query(query)

def update_question(question_id, data):
    query = f"""
    UPDATE QUESTION
    SET
        question_title='{data['question']}',
        answer='{data['answer']}'
    WHERE question_id={question_id} 
    """
    return run_query(query)



