from django import forms
from .models import Comment
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name','email','text']
        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }