from django.shortcuts import render, redirect
from django.views import View

from core.utils.db.user import login_authentication_query

class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        data = login_authentication_query(request.POST)
        if data:
            request.session['user_id'] = str(data[0])
            request.session['user_type'] = str(data[1])
            return redirect('course:list')
        else:
            return render(request, self.template_name, {
                'error': 'Invalid email/password'
            })


class LogoutView(View):

    def get(self, request):
        try:
            del request.session['user_id']
            del request.session['user_type']
        except KeyError:
            print('asdsa')
            pass
        return redirect('user:login')
