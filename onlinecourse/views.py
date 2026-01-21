from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Enrollment, Submission, Learner
from django.contrib.auth.decorators import login_required

# Homepage showing all courses
def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'onlinecourse/index.html', context)

# Course details page
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    questions = course.questions.all()
    context = {
        'course': course,
        'lessons': lessons,
        'questions': questions
    }
    return render(request, 'onlinecourse/course_detail.html', context)

# Enroll a learner into a course
@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    learner = get_object_or_404(Learner, user=request.user)
    enrollment, created = Enrollment.objects.get_or_create(learner=learner, course=course)
    return redirect('course_detail', course_id=course.id)

# Submit answers to a quiz
@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    learner = get_object_or_404(Learner, user=request.user)
    enrollment = get_object_or_404(Enrollment, learner=learner, course=course)

    if request.method == 'POST':
        selected_choices = request.POST.getlist('choices')
        submission = Submission.objects.create(enrollment=enrollment)
        submission.choices.set(selected_choices)
        submission.save()
        return redirect('show_result', course_id=course.id, submission_id=submission.id)

    return redirect('course_detail', course_id=course.id)

# Show quiz results
@login_required
def show_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    questions = course.questions.all()
    
    total_score = sum([q.is_get_score([c.id for c in submission.choices.filter(question=q)]) for q in questions])
    
    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'questions': questions
    }
    return render(request, 'onlinecourse/result.html', context)
