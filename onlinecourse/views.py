from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Submission, Choice

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_details_bootstrap.html', {'course': course})

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        submission = Submission.objects.create(user=request.user, course=course)
        selected_choices = request.POST.getlist('choices')
        submission.choices.set(selected_choices)
        submission.save()
        return redirect('show_exam_result', submission_id=submission.id)
    return redirect('course_details', course_id=course.id)

def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    total = sum(q.grade for q in submission.course.questions.all())
    score = 0
    for question in submission.course.questions.all():
        correct_choices = question.choices.filter(is_correct=True)
        selected = submission.choices.filter(question=question)
        if set(correct_choices) == set(selected):
            score += question.grade
    return render(request, 'exam_result.html', {'submission': submission, 'score': score, 'total': total})
