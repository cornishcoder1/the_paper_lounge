from .models import Comment, Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):

    # Sets a required field on a Django model form (README code reference no.2)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].required = True

    class Meta:
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
