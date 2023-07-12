from django.contrib import admin
from .models import Choice, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question text",{"fields": ["question_text"]}), 
        ("Date information",{"fields": ["pub_date"], "classes":["collapse"]}),
    ]

    inlines=[ChoiceInLine]

    list_display = ["question_text","pub_date","was_published_recently "]

    # fieldsets -> son bandas de subtitlos que se muestran en el navegador 
    # This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice) # <- removed

