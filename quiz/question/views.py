from django.shortcuts import render, redirect
from django.views import View

from core.utils.db.course import get_student_courses, get_teacher_courses
from core.utils.db import question

class QuestionCreateView(View):

    def get(self, request, course_id, quiz_id, question_type):
        if question_type == 'MCQs':
            template = 'question/mcqs.html'
        elif question_type == 'Blank':
            template = 'question/blank.html'
        elif question_type == 'T&F':
            template = 'question/tf.html'

        return render(request, template, {
            'question_type': question_type,
            'create': True
        })

    def post(self, request, course_id, quiz_id, question_type):
        if question_type == 'MCQs':
            question.create_question(
                quiz_id,
                'MCQS',
                request.POST
            )
        elif question_type == 'Blank':
            question.create_question(
                quiz_id,
                'BLANK',
                request.POST
            )
        elif question_type == 'T&F':
            question.create_question(
                quiz_id,
                'TF',
                request.POST
            )
        return redirect('quiz:detail', course_id, quiz_id)


class QuestionUpdateView(View):

    def get(self, request, course_id, quiz_id, question_id):
        q = question.get_question(question_id)
        print(q)
        context = {
            'question_type': q[2],
            'question': q,
            'update': True,
        }
        if q[2] == 'MCQS':
            template = 'question/mcqs.html'
            context['choices'] = question.get_question_choices(question_id)
        elif q[2] == 'BLANK':
            template = 'question/blank.html'
        elif q[2] == 'TF':
            template = 'question/tf.html'

        return render(request, template, context)

    def post(self, request, course_id, quiz_id, question_id):
        q = question.update_question(question_id, request.POST)
        return redirect('quiz:detail', course_id, quiz_id)


class QuestionDeleteView(View):
    def get(self, request, course_id, quiz_id, question_id):
        question.delete_question(question_id)
        return redirect('quiz:detail', course_id, quiz_id)
