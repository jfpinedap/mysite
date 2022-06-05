from django.contrib import admin
from ads.models import Ad

class AdAdmin(admin.ModelAdmin):
    """Define the AdAdmin calss"""
    exclude = ('picture', 'content_type')

# Register the admin class with the associated model
admin.site.register(Ad, AdAdmin)
