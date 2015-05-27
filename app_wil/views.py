from django.shortcuts import render
from django.views import generic

from app_wil import models
from .forms import *


class TardyFormView(generic.FormView):
    template_name = 'form.html'
    form_class = AddTardyForm

    def get_context_data(self, *args, **kwargs):
        context = super(TardyFormView, self).get_context_data(*args, **kwargs)
        context['kwargs'] = self.kwargs
        context['request'] = self.request
        return context

    def get_form_kwargs(self):
        kwargs = super(TardyFormView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(TardyFormView, self).form_valid(form)

    def get_success_url(self):
        return '/'

