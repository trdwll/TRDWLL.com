from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

class PostAdmin(admin.ModelAdmin):
    exclude = ['author']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'category__title', 'body', 'keywords']
    list_display = ['title', 'categories', 'published_date', 'is_published']
    select_related = ('category', )
    fieldsets = (
        ('Post Information', {
            'fields': ('published_date', 'difficulty', 'is_published', 'keywords', 'title', 'description', 'category', 'slug', 'body', )
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user

        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('category')    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)