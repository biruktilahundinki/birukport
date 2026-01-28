from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'order', 'timestamp', 'content_snippet')
    list_filter = ('timestamp', 'sender')
    search_fields = ('content', 'sender__username')
    readonly_fields = ('timestamp',)

    def content_snippet(self, obj):
        return obj.content[:50]
    content_snippet.short_description = 'Content Preview'
