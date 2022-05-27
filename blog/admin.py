from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Genre)
# class TopicAdmin(admin.ModelAdmin):
#     """Admin view for Genres"""
#     list_display = ('name', 'description')
#     search_fields = ('name', 'description')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)} #Slug field will populate automatically from the title field
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on', 'approved')
    search_fields = ('title', 'content')
    summernote_fields = ('content') # Tells Django what fields we want to use Summernote with
    actions = ['approve_review']

    def approve_review(self, request, queryset):
        queryset.update(approved=True)
        

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


