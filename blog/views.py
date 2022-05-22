from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Review
from .forms import CommentForm, ReviewForm
from django.contrib import messages


def add_review(request):
    submitted = False
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_review?submitted=True')
        else:
            form = ReviewForm
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'add_review.html', {'form': form, 'submitted': submitted})


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    

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
            }
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
            comment_form.instance.email = request.user.email
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
        review = get_object_or_404(Review)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('review_detail', args=[slug]))