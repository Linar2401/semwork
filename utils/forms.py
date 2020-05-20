from django.contrib.auth.forms import *

from utils.models import CustomUser
from utils.tasks import send_reset_password_email
import logging

logger = logging.getLogger(__name__)


class RegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['password1', 'password2', "username"]:
            self.fields[field_name].help_text = None


class PostForm(forms.Form):
    name = forms.CharField(max_length=50, label="Имя")
    text = forms.Textarea()


class ResetPasswordForm(PasswordResetForm):

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        logger.error(context)
        context['user'] = ""
        send_reset_password_email.delay(subject_template_name, email_template_name,
                                        context, from_email, to_email, html_email_template_name)

