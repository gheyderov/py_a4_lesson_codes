from django import forms
from stories.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'message',
        )
        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message'
            })
        }
    

class SubCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'message',
        )
        widgets = {
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message'
            })
        }
    