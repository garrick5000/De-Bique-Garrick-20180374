from django.contrib import admin
from .models import Artifact, Level

class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('level',)
    search_fields = ('name',)
    
admin.site.register(Artifact, ArtifactAdmin)
admin.site.register(Level)