from .models import Comment, Review
from django import forms

# genres = [('crime', 'crime'), ('thriller', 'thriller')]
# genres = Genre.objects.all().values_list('name', 'name')

# genre_list = []

# for genre in genres:
#     genre_list.append(genre)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):

    # Sets a required field on a Django model form (README Acknowledgement no.3)
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

        # widgets = {
        #     'genre': forms.Select(choices=genre_list, attrs={'class': 'form-control'}),
        # }
