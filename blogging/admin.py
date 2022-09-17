from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    # If you want to display many-to-many relations using an inline,
    # you can do so by defining an InlineModelAdmin object for the relationship. The through attribute is a reference
    # to the model that manages the many-to-many relation. This model is automatically created by Django when you define
    # a many-to-many field.
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # category = str(Category.name)  somehow you should be able to link posts/categories and show them in admin
    list_display = (
        "title",
        "author",
        "created_date",
        "modified_date",
        "published_date",
    )
    inlines = [
        CategoryInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)  # excludes 'posts' from showing up in the category admin page


# admin.site.register(Post)      # register Post model is now being done with the decorator
# # admin.site.register(Category)  # register Category model is now being done with the decorator
