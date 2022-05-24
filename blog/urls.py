from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('add-review/', views.add_review, name='add_review'),
    path('edit-review/<slug:slug>', views.edit_review, name='edit_review'),
    path('delete-review/<slug:slug>', views.delete_review,
         name='delete_review'),
    path('reviews/<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>)', views.ReviewLike.as_view(), name='review_like'),
    
]
