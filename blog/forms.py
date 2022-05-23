from .models import Comment, Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'author',
            'rating',
            'content',
            'featured_image',
        )

        labels = {
            'title': 'Book Title',
            'author': 'Book Author',
            'content': 'Write your review here',
            'featured_image': 'cover image',
        }

        # widgets = {
        #     'title': forms.TextInput(attrs={'class' 'form-control'}),
        #     'author': forms.TextInput(attrs={'class' 'form-control'}),
        #     'content': forms.TextInput(attrs={'class' 'form-control'}),
        # }