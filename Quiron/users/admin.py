# Django
from django.contrib import admin

# Import our models to the admin
from users.models import Profile

# Register the model profile in the admin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user','prof_register','picture']
    list_display_links = ('pk', 'prof_register',)
    list_editable = ('picture',)
    search_fields = ('user__first_name', 'user__last_name', )

