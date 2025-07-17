# portfolio_app/admin.py
from django.contrib import admin
from .models import Project

admin.site.register(Project)


from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'subject', 'is_read')  # Fields shown in the list view
    list_filter = ('created_at', 'is_read')  # Add filters for easier searching (e.g., by date and read status)
    search_fields = ('name', 'email', 'subject', 'message')  # Fields searchable in the admin
    ordering = ('-created_at',)  # Order by the most recent message first
    readonly_fields = ('created_at',)  # Make created_at field read-only
    list_editable = ('is_read',)  # If you want to make 'is_read' editable directly in the list view
    actions = ['mark_as_read']  # Custom action to mark messages as read

    # Define a custom action
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

# Register the model with the admin interface
admin.site.register(ContactMessage, ContactMessageAdmin)

