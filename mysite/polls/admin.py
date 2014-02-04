from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['choice_text']}),
        ('Nbr of Votes', {'fields': ['votes']}),
    ]
    list_display = ('choice_text', 'votes')
    list_filter = ['votes']
    search_fields = ['choice_text']

admin.site.register(Choice, ChoiceAdmin)
