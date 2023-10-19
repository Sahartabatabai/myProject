from django import forms
from .models import Book
from django.core.exceptions import ValidationError



class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'author2']

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        author2 = cleaned_data.get('author2')

        if author and author2 and abs(len(author) - len(author2)) > 1:
            raise ValidationError("Author and Author 2 must be similar (differ by at most one character).")

        return cleaned_data

