from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=50, required=True, label='Author')
    content = forms.CharField(widget=forms.Textarea, required=True, label='Content')

    # Meta class tells Django which model to use and which fields to include
    class Meta:
        model = Comment
        fields = ['author', 'content']