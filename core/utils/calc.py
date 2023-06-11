
def calc_quiz_marks(questions, answers):
    total_questions = len(questions)
    correct_questions = 0
    if total_questions == 0:
        return 100
    for q in questions:
        if q[4].lower() == answers[f'answer_q{q[0]}'].lower():
            correct_questions += 1
    return (correct_questions * 100)/total_questions