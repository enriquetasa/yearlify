from django.contrib import admin

from .models import Letter

class LetterAdmin(admin.ModelAdmin):
    fields = ['send_on', 'user', 'created_at']
    readonly_fields = ['created_at']

admin.site.register(Letter, LetterAdmin)
