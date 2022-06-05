# Django imports
from django.contrib import admin

# Models imports
from cats.models import Cat, Breed

admin.site.register(Cat)
admin.site.register(Breed)
