from django.shortcuts import render, redirect
from django.views import View

from core.utils.db.course import get_student_courses, get_teacher_courses


class CourseListView(View):
    template = 'course/list.html'

    def get(self, request):
        if request.session['user_type'] == 'teacher':
            courses = get_teacher_courses(request.session['user_id'])
        elif request.session['user_type'] == 'student':
            courses = get_student_courses(request.session['user_id'])
        
        print(courses)
        return render(request, self.template, {
            'courses': courses,
            'user_type': request.session['user_type']
        })
