from django.shortcuts import render
from django.views.generic import TemplateView

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

    