from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))
RATING = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class Review(models.Model):
    """
    Model for review
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_posts")
    updated_on = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=RATING, default=0)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Review, self).save(*args, **kwargs)

    class meta:
        """
        Order the reviews in descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return self.title

    def number_of_likes(self):
        """
        See number of likes on a review.
        """
        return self.likes.count()

    # def can_edit(self, request, slug):
    #     """
    #     Allows creator to edit review.
    #     """
    #     if self.creator:
    #         return True
    #     else:
    #         return False

    # def can_delete(self, request, slug):
    #     """
    #     Allows author to delete review.
    #     """
    #     if self.creator:
    #         return True
    #     else:
    #         return False


class Comment(models.Model):
    """
    Model for comments
    """
    post = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta: 
        """
        Order the comments in ascending order (oldest first)
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
