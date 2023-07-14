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
    # fieldsets -> son bandas de subtitlos que se muestran en el navegador 
    # This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”

    inlines=[ChoiceInLine]

    list_display = ["question_text","pub_date","was_published_recently"]
    list_filter = ["pub_date"] # That adds a “Filter” sidebar that lets people filter the change list by the pub_date field:
    search_fields = ["question_text"]
    # list_per_page = 1 # funciona
    # date_hierarchy ="pub_date" # no funciona


    

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice) # <- removed

# Find: Django source files, with the following command
#  python -c "import django; print(django.__path__)"