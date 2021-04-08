from django.contrib import admin

from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
 
    fieldsets = [("change the question you woud love to", {'fields': [ 'question_text',] }), ('Publication Date information', {'fields': ['pub_date'], 'classes': ['collapse'], })]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date','was_published_recently')



admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

  