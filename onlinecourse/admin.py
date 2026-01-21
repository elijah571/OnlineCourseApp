from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission, Enrollment, Instructor, Learner

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'course', 'grade')
    search_fields = ('text',)
    inlines = [ChoiceInline]

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'submitted_at')
    list_filter = ('enrollment__course',)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('learner', 'course', 'date_enrolled', 'mode')
    search_fields = ('learner__user__username', 'course__name')

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_time', 'total_learners')
    search_fields = ('user__username',)

class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'occupation')
    search_fields = ('user__username',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
