from django import forms
from stories.models import Comment, Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'small_description',
            'description',
            'image',
            'cover_image',
            'category',
            'tags'
        )
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Title'
            }),
            'small_description' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Small Description'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Description'
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control',
            }),
            'tags' : forms.SelectMultiple(attrs={
                'class' : 'form-control',
            }),
            'image' : forms.FileInput(),
            'cover_image' : forms.FileInput()

        }


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
    