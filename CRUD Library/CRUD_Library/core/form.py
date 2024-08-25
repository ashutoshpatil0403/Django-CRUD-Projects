from django import forms
from .models import UPSC_Books


class AddUPSCBooks(forms.ModelForm):
    class Meta:
        model=UPSC_Books
        fields=('subject','bookname','authorname','price')
        widgets={
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'bookname':forms.TextInput(attrs={'class':'form-control'}),
            'authorname':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }