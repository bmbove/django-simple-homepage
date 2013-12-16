from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from pages.models import Page


class PageDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        if not kwargs['slug']:
            return redirect('/home')
        else:
            slug = kwargs['slug']

        try:
            page = Page.objects.get(slug=slug)
        except:
            return redirect('/home')

        template_name = 'pages/page.html'
        context = {'page': page}
        return render(request, template_name, context)
