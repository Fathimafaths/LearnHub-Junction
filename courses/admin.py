from django.contrib import admin

from .models import Course, Review
class CommentInline(admin.TabularInline):
    model = Review
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ("image", "summary", "youtubeUrl")
    inlines = [CommentInline]

admin.site.register(Course,CourseAdmin)
