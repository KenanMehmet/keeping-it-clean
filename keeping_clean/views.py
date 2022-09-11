from django.shortcuts import render
from django.views.generic import TemplateView

class KeepingCleanIndex(TemplateView):
    template_name = "templates/keeping_clean/base.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "title": "Keeping It Clean" 
            },
        )

    