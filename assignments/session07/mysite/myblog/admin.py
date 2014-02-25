from django.contrib import admin
from myblog.models import Post, Category

# class AuthorAdmin(admin.ModelAdmin):
#     fields = ('name', 'title', 'url')

class CatergoryInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
	fields = ('name','description')
	exclude = ('posts',)

class PostAdmin(admin.ModelAdmin):
	# def make_published(self, request, queryset):
	# 	queryset.update(status='p')

	# def make_unpublished(self, request, queryset):
	# 	queryset.update(status='d')

	list_display = ['text', 'author', 'created_date', 'modified_date', 'published_date']
	readonly_fields = ('created_date', 'modified_date')
	fields = ['text', 'author','created_date', 'modified_date', 'published_date' ]
	inlines = [CatergoryInline, ]
	#actions = ['make_published','make_unpublished']
	#make_published.short_description = "Publish selected posts"

#admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)