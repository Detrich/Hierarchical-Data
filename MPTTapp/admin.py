from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from MPTTapp.models import FolderorFile
# Register your models here.

admin.site.register(FolderorFile, DraggableMPTTAdmin)