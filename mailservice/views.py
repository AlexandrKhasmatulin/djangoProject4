from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from blog.models import Blog
from send_emails.forms import SmsLetterForm, SubjectForm
from send_emails.models import SmsLetter, Mailing, Client

class SmsLetterCreateView(CreateView):
    model = SmsLetter
    form_class = SmsLetterForm
    success_url = reverse_lazy("mailservice:create")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save(commit=False)
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)



# Create your views here.
