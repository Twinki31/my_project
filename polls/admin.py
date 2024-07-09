# surveys/admin.py
from django.contrib import admin
from .models import Poll, Question, Answer


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Количество пустых полей для добавления новых вопросов


class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'start_date', 'end_date', 'description')
    search_fields = ('title', 'description')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question_type', 'poll')
    list_filter = ('question_type', 'poll')
    search_fields = ('text',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'question', 'text')


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
