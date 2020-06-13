from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from files.models import File

# Register your models here.
admin.site.register(File, DraggableMPTTAdmin)
