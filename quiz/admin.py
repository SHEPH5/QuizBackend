from django.contrib import admin
from . import models

@admin.register(models.Category)

class Catadmin(admin.ModelAdmin):
    list_display = [
        'name',

    ]

@admin.register(models.Quizzes)

class Quizadmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',

    ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right'

    ]

@admin.register(models.Question)

class Questionadmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',

    ]

    list_display = [
        'title',
        'quiz',
        'date_updated',
    ]
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(models.Answer)

class Answeradmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'question',
        'is_right'
    ]