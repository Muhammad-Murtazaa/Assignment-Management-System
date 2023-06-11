from .conn import run_query

def get_teacher_courses(teacher_id):
    query = f"""
    SELECT * FROM Course
    WHERE th_id={teacher_id}
    """
    return run_query(query)


def get_student_courses(student_id):
    query = f"""
    SELECT SC.course_id, C.name
    FROM Student_Course SC INNER JOIN Course C ON(SC.course_id = C.course_id)
    WHERE SC.ST_ID={int(student_id)}
    """
    return run_query(query)