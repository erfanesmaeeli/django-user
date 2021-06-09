from django.shortcuts import render
from django.views import generic
from .models import User
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogOutView
from django.urls import reverse_lazy


class LoginView(BaseLoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy("main:dashboard")

    def get_success_url(self):
        return str(self.success_url)

    def get(self, request, *args, **kwargs):
        try:
            #TODO This line of code is not working properly !
            request.session["next"] = request.GET['next']
            self.success_url = request.session["next"]
        except KeyError:
            pass            
        return self.render_to_response(self.get_context_data())


class LogOutView(BaseLogOutView):
    pass

class SignUpView(generic.TemplateView):
	template_name = 'accounts/signup.html'

    

