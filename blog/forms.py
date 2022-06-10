from django import forms
from .models import Comment, Review


class CommentForm(forms.ModelForm):
    """Comment form"""
    class Meta:
        """meta class"""
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    """Review form"""
    # Sets a required field on a Django model form (README code reference no.2)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].required = True

    class Meta:
        """meta class"""
        model = Review
        fields = (
            'title',
            'author',
            'genre',
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
