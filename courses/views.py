from django.shortcuts import render,get_object_or_404

from django.utils import timezone

from django.http import HttpResponse

from .models import Course, Review

from .forms import ReviewForm

def index(request):
    courses = Course.objects.all()
    return render(request,'courses/index.html',{'courses':courses})

def detail(request,course_id):
    course_detail = get_object_or_404(Course,pk=course_id)
    for course in Course.objects.all():
        comments = Review.objects.filter(course=course_detail)
    return render(request,'courses/detail.html',{'course':course_detail,'reviews':comments})

def updateReview(request, course_id):
    if request.method == 'POST':
        userrating = request.POST.get('rating', None)
        username = request.POST.get('username', None)
        comment_text = request.POST.get('comment', None)
        current_time = timezone.now()

        course_detail = get_object_or_404(Course, pk=course_id)

        review = Review(course=course_detail, user=username, rating=userrating, comment=comment_text, created_at=current_time)
        review.save()

    reviews = Review.objects.all()
    for course in Course.objects.all():
        comments = Review.objects.filter(course=course_detail)
    return render(request,'courses/detail.html',{'course':course_detail,'reviews':comments})
