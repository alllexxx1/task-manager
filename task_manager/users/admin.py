from django.contrib import admin
from task_manager.users.models import User
from django.contrib.admin import DateFieldListFilter


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'date_joined')
    list_display_links = ('id', 'first_name', 'username')
    ordering = ['date_joined']
    list_per_page = 5
    search_fields = ['username__startswith']
    list_filter = (
        ('date_joined', DateFieldListFilter),

    )
    # list_editable = ('username',)
