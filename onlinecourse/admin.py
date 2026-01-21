from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission

# Inline for Choices under Questions
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Admin class for Questions
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'course', 'grade')
    inlines = [ChoiceInline]

# Admin class for Lessons
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    # ❌ Removed QuestionInline to fix the error

# Register models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
