from .conn import run_query

def login_authentication_query(data):
    if data['user_type'] == 'student':
        query = f"""
        SELECT st_id FROM STUDENT 
        WHERE email='{data['email']}' AND password='{data['password']}' 
        """
    elif data['user_type'] == 'teacher':
        query = f"""
        SELECT th_id FROM TEACHER
        WHERE email='{data['email']}' AND password='{data['password']}' 
        """

    query_data =run_query(query)
    if query_data:
        return query_data[0][0], data['user_type']
    else:
        return None

