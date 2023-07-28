from django.contrib import admin
from .models import Post, Category, Profile, Comment, Favorite


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Post model.
    
    Inherits from ModelAdmin.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
        list_display_links (tuple): The fields that link to the change view of the model.
        search_fields (tuple): The fields used for searching in the admin list view.
        list_filter (tuple): The fields used for filtering in the admin list view.
    """
    list_display = ('id', 'post_title', 'post_image', 'post_content', 'post_category', 'post_date', 'post_author')
    list_display_links = ('id', 'post_title')
    search_fields = ('post_title', 'post_content')
    list_filter = ('post_category',)

class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Category model.
    
    Inherits from ModelAdmin.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
        list_display_links (tuple): The fields that link to the change view of the model.
        search_fields (tuple): The fields used for searching in the admin list view.
        list_filter (tuple): The fields used for filtering in the admin list view.
    """
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Profile model.
    
    Inherits from ModelAdmin.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
        list_display_links (tuple): The fields that link to the change view of the model.
        search_fields (tuple): The fields used for searching in the admin list view.
        list_filter (tuple): The fields used for filtering in the admin list view.
    """
    list_display = ('id', 'user', 'user_photo', 'user_description', 'registration_date', 'user_link')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_filter = ('registration_date',)
        
class CommentAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Comment model.
    
    Inherits from ModelAdmin.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
        list_display_links (tuple): The fields that link to the change view of the model.
        search_fields (tuple): The fields used for searching in the admin list view.
        list_filter (tuple): The fields used for filtering in the admin list view.
    """
    list_display = ('id', 'post', 'name', 'comment_content', 'comment_date')
    list_display_links = ('id', 'post')
    search_fields = ('comment_content',)
    list_filter = ('comment_date',)
    
class FavoriteAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Favorite model.
    
    Inherits from ModelAdmin.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
        list_display_links (tuple): The fields that link to the change view of the model.
        search_fields (tuple): The fields used for searching in the admin list view.
        list_filter (tuple): The fields used for filtering in the admin list view.
    """
    list_display = ('id', 'post', 'user', 'created_at')
    list_display_links = ('id', 'post')
    search_fields = ('post',)
    list_filter = ('post',)

# Registering models with their respective admin configurations

admin.site.register(Post, PostAdmin)
"""
Registers the Post model with the PostAdmin custom admin configuration.
This allows managing Post objects in the Django admin interface.
"""

admin.site.register(Category, CategoryAdmin)
"""
Registers the Category model with the CategoryAdmin custom admin configuration.
This enables managing Category objects in the Django admin interface.
"""

admin.site.register(Profile, ProfileAdmin)
"""
Registers the Profile model with the ProfileAdmin custom admin configuration.
This enables managing Profile objects in the Django admin interface.
"""

admin.site.register(Comment, CommentAdmin)
"""
Registers the Comment model with the CommentAdmin custom admin configuration.
This enables managing Comment objects in the Django admin interface.
"""

admin.site.register(Favorite, FavoriteAdmin)
"""
Registers the Favorite model with the FavoriteAdmin custom admin configuration.
This enables managing Favorite objects in the Django admin interface.
"""


