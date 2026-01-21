from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'course', 'grade')
    inlines = [ChoiceInline]

admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)
