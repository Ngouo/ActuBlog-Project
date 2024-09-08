from django.contrib import admin
from .models import PostModel, Commentaire

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
  list_display = ("title", 'date_publication','auteur')
  
admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Commentaire)
