from django.contrib import admin
from .models import (
    Course, Lesson, Question, Choice,
    Submission, Enrollment, Instructor, Learner
)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [QuestionInline]   # ✅ Question belongs to Course


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'course', 'grade')
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')  # ✅ NO inline here


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Learner)
