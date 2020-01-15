from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

class PostAdmin(admin.ModelAdmin):
    exclude = ['author']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'category', 'tags', 'body']
    list_display = ['title', 'category', 'published_date', 'is_published']
    ordering = ('-published_date', )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)