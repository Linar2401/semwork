from django import forms
from django.contrib.auth.forms import *
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from books.models import *


class BookForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name")
    genres = forms.MultipleChoiceField(choices=Genre.objects.all())
    warnings = forms.MultipleChoiceField(choices=Warning.objects.all())
    rating = forms.ChoiceField(choices=Rating.objects.all())

    file_fb2 = forms.FileField(allow_empty_file=True)
    file_txt = forms.FileField(allow_empty_file=True)
    file_epub = forms.FileField(allow_empty_file=True)
    image = forms.FileField(allow_empty_file=True)


class ReviewForm(forms.Form):
    text = forms.Textarea()
    mark = forms.DecimalField(label="Mark", max_digits=2, decimal_places=1)


class CommentForm(forms.Form):
    text = forms.CharField(max_length=500, label='Text')


class RequestForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name")
    text = forms.Textarea()
    genres = forms.MultipleChoiceField(choices=Genre.objects.all())
    warnings = forms.MultipleChoiceField(choices=Warning.objects.all())
    rating = forms.ChoiceField(choices=Rating.objects.all())


class CollectionForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name")
    open = forms.BooleanField(required=False)


class AddToCollectionForm(forms.Form):
    text = forms.Textarea()
    book_id = forms.HiddenInput()
    collection_id = forms.HiddenInput()
