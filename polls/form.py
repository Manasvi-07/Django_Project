from django import forms
from .models import Author, Publisher, Book, Store

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

