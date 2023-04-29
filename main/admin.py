from django.contrib import admin
from .models import Posts, Categories
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'cat', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Categories, CategoriesAdmin)
