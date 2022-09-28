from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password

from .forms import MainSiteClientSignupForm
from .models import Client

class MainSiteIndex(TemplateView):
    template_name = "main_site/index.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": "Keeping It Clean" 
            },
        )


class MainSiteClientSignup(TemplateView):
    template_name = "main_site/client_signup.html"

    def get(self, request):
        form = MainSiteClientSignupForm()
        return render(
            request,
            self.template_name,
            {
                "form": form
            }
        )

    def post(self, request):
        form = MainSiteClientSignupForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            print("done")
        return render(
            request,
            self.template_name,
            {
                "form": form
            }
        )
