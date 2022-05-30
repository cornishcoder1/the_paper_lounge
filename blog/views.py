from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review, Genre
from .forms import CommentForm, ReviewForm


def add_review(request):
    submitted = False
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.instance.creator = request.user
            review_form.save()
            messages.success(request, 'Success! Your review has been submitted for approval.')
            return redirect('home')
    else:
        review_form = ReviewForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_review.html', {'review_form': review_form, 'submitted': submitted})


def edit_review(request, slug):
    """
    Review update/edit view
    """
    review = get_object_or_404(Review, slug=slug)
    review_form = ReviewForm(request.POST or None, instance=review)
    context = {
        "review_form": review_form,
        "review": review
    }
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.creator = request.user
            review.save()
            return redirect('home')
    else:
        review_form = ReviewForm(instance=review)
    return render(request, "edit_review.html", context)


def delete_review(request, slug):
    """
    Review delete view
    """
    review = Review.objects.get(slug=slug)
    review.delete()
    return redirect('home')


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# GenreReviewList and genre_list views based on code from 'Learn Django -
# Building a Simple Blog Categories Feature' by Very Academy (README code
# reference no.3)

class GenreReviewList(generic.ListView):
    template_name = 'genres.html'
    context_object_name = 'genlist'

    def get_queryset(self):
        content = {
            'gen': self.kwargs['genre'],
            'reviews': Review.objects.filter(genre__name=self.kwargs['genre'])
            .filter(status=1)
        }
        return content


def genre_list(request):
    genre_list = Genre.objects.exclude(name='default')
    context = {
        'genre_list': genre_list,
    }
    return context


class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True 
        
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
        
    def post(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True 

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()
            messages.success(request, 'Success! Your comment has been submitted for approval.')
        else: 
            comment_form = CommentForm()
        
        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class ReviewLike(View):

    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)
      
        return HttpResponseRedirect(reverse('review_detail', args=[slug]))