from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import *
from django.contrib.auth.forms import *

from books.models import *
from utils.models import *
from utils.forms import *


class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'utils/post_view.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'utils/account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['books'] = Book.objects.filter(user=self.request.user.id)
        context['reviews'] = Review.objects.filter(user=self.request.user.id)
        context['requests'] = BookRequest.objects.filter(user=self.request.user.id)
        context['collections'] = BookCollection.objects.filter(user=self.request.user.id)
        return context


class AnotherProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'utils/account/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(CustomUser, pk=self.kwargs.get('id'))
        context['user'] = user
        context['books'] = Book.objects.filter(user=user)
        context['reviews'] = Review.objects.filter(user=user)
        context['requests'] = BookRequest.objects.filter(user=user)
        context['collections'] = BookCollection.objects.filter(user=user, open=True)
        return context


class SignInView(LoginView):
    success_url = "account/profile/"
    template_name = "utils/account/login.html"


class RegView(FormView):
    form_class = RegForm
    template_name = 'utils/account/sign_up.html'
    success_url = '/account/sign_in/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AllUsers(ListView):
    model = CustomUser
    template_name = 'utils/list_uses.html'
    context_object_name = 'users'


class ResetPasswordView(PasswordResetView):
    template_name = 'utils/account/password_reset_form.html'
    email_template_name = 'utils/account/password_reset_email.html'
    subject_template_name = 'utils/account/password_reset_subject.txt'
    success_url = reverse_lazy('utils:password_reset_done')
    form_class = ResetPasswordForm


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'utils/account/password_reset_done.html'
