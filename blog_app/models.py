from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from django.core.files.images import get_image_dimensions

# Create your models here.

''' Validators for Profile Model '''
def validate_phone_for_profile(value):
    """
    Validate the phone number for a user profile.

    Args:
        value (str): Phone number to validate.

    Raises:
        ValidationError: If the phone number is invalid.
    """
    if not value:
        return
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("Invalid phone number")
    
def validate_user_link_for_profile(value):
    """
    Validate the user link for a user profile.

    Args:
        value (str): User link to validate.

    Raises:
        ValidationError: If the user link is invalid.
    """
    if not value:
        return
    if not value.startswith(("http://", "https://")):
        raise ValidationError("Invalid user link")

def validate_user_birth_date_for_profile(value):
    """
    Validate the birth date for a user profile.

    Args:
        value (date): Birth date to validate.

    Raises:
        ValidationError: If the birth date is invalid.
    """
    if value and value > datetime.date.today():
        raise ValidationError("Invalid birth date")

def validate_user_github_url_for_profile(value):
    """
    Validate the GitHub URL for a user profile.

    Args:
        value (str): GitHub URL to validate.

    Raises:
        ValidationError: If the GitHub URL is invalid.
    """
    if not value:
        return
    if not re.match(r'^https://github.com/', value):
        raise ValidationError("Invalid GitHub URL")
    
def validate_user_photo_for_profile(value):
    """
    Validate the user photo for a user profile.

    Args:
        value (str): User photo to validate.

    Raises:
        ValidationError: If the user photo is invalid.
    """
    if value:
        width, height = get_image_dimensions(value)
        allowed_extensions = ('.jpg', '.jpeg', '.png')
        if not value.name.endswith(allowed_extensions) or width < 200 or height < 200:
            raise ValidationError("Invalid user photo")

def validate_user_description_for_profile(value):
    """
    Validate the user description for a user profile.

    Args:
        value (str): User description to validate.

    Raises:
        ValidationError: If the user description exceeds the maximum length of 500 characters.
    """
    if value and len(value) > 500:
        raise ValidationError("User description exceeds the maximum length of 500 characters")
''' Validators for Profile Model '''

class Profile(models.Model):
    """
    A model representing a user profile.
    
    Inherits from Model.
    
    Attributes:
        user (User): One-to-one relationship with the built-in Django User model, representing the associated user for this profile.
        user_photo (ImageField): An ImageField that stores the user's photo. It allows null and blank values and defines an upload path for the image files.
        user_description (TextField): A TextField that stores the user's description. It allows null and blank values.
        registration_date (DateTimeField): A DateTimeField that stores the registration date of the profile. It is automatically set to the current date and time when the profile is created.
        phone (CharField): A CharField that stores the user's phone number. It allows a maximum length of 10 characters and allows null and blank values.
        user_link (CharField):  A CharField that stores a link associated with the user. It allows a maximum length of 200 characters and allows null and blank values.
        user_birth_date (DateField): A DateField that stores the user's birth date. It allows null and blank values.
        user_github_url (CharField): A CharField that stores the user's GitHub URL. It allows a maximum length of 200 characters and allows null and blank values.
        
    Meta:
        verbose_name (str): The singular name of the profile.
        verbose_name_plural (str): The plural name of the profile.

    Methods:
        __str__(): Returns the string representation of the profile.
        get_absolute_url(): Returns the absolute URL of the profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    user_photo = models.ImageField(null=True, blank=True, upload_to='images/profile/', validators=[validate_user_photo_for_profile])
    user_description = models.TextField(null=True, blank=True, validators=[validate_user_description_for_profile])
    registration_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10, null=True, blank=True, validators=[validate_phone_for_profile])
    user_link = models.CharField(max_length=200, null=True, blank=True, validators=[validate_user_link_for_profile])
    user_birth_date = models.DateField(null=True, blank=True, validators=[validate_user_birth_date_for_profile])
    user_github_url = models.CharField(max_length=200, null=True, blank=True, validators=[validate_user_github_url_for_profile])
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
    def __str__(self):
        """
        Returns a string representation of the Profile object.

        Returns:
            str: The string representation of the associated User object.
        """
        return str(self.user)
    
    def get_absolute_url(self):
        """
        Returns the absolute URL for the Profile object.

        Returns:
            str: The absolute URL for the 'home' view.
        """
        return reverse('home')

''' Validators for Post Model '''
def validate_post_title_for_post(value):
    """
    Validate the post title for post.

    Args:
        value (str): Post title to validate.

    Raises:
        ValidationError: If the post title exceeds the maximum length of 200 characters or post title equals 0 characters.
    """
    if len(value) == 0:
        raise ValidationError("Fill in the field Post title")
    if len(value) > 200:
        raise ValidationError("Post title exceeds the maximum length of 200 characters")

def validate_post_image_for_post(value):
    """
    Validates a post image for a post.

    Args:
        value (object): The image object to validate.

    Raises:
        ValidationError: If the image is invalid.
    """
    if value:
        width, height = get_image_dimensions(value)
        allowed_extensions = ('.jpg', '.jpeg', '.png')
        if not value.name.endswith(allowed_extensions) or width < 200 or height < 200:
            raise ValidationError("Invalid post image")

def validate_post_content_for_post(value):
    """
    Validates the content of a post.

    Args:
        value (str): The content to validate.

    Raises:
        ValidationError: If the content is empty or exceeds the maximum length.
    """
    if len(value) == 0:
        raise ValidationError("Fill in the field Post content")
    if len(value) > 10000:
        raise ValidationError("Post content exceeds the maximum length of 10000 characters")

def validate_post_category_for_post(value):
    """
    Validates the category of a post.

    Args:
        value (str): The category name to validate.

    Raises:
        ValidationError: If the category is invalid.
    """
    allowed_categories = Category.objects.all()
    if not allowed_categories.filter(name=value).exists():
        raise ValidationError("Invalid post category")
''' Validators for Post Model '''

class Post(models.Model):
    """
    Represents a post.
    
    Inherits from Model.

    Attributes:
        post_title (CharField): The title of the post.
        post_image (ImageField): The image associated with the post.
        post_content (RichTextField): The content of the post.
        post_category (CharField): The category of the post.
        post_date (DateTimeField): The date the post was created.
        post_author (ForeignKey): The author of the post.
        favorites (ManyToManyField): Users who have favorited the post.
        likes (ManyToManyField): Users who have liked the post.
        
    Meta:
        ordering (list[str]): Default ordering of instances based on the primary key.
        verbose_name (str): The singular name of the post.
        verbose_name_plural (str): The plural name of the post.
        unique_together (tuple): Fields must be unique together.

    Methods:
        total_likes(): Returns the total number of likes for the post.
        increase_likes(): Increases the number of likes for the post by 1.
        decrease_likes(): Decreases the number of likes for the post by 1, if the current count is greater than 0.
        total_posts(): Returns the total number of posts.
        __str__(): Returns the string representation of the post.
        get_absolute_url(): Returns the absolute URL of the post.
    """
    post_title = models.CharField(max_length=200, null=False, blank=False, validators=[validate_post_title_for_post])
    post_image = models.ImageField(null=True, blank=True, upload_to='images/posts', validators=[validate_post_image_for_post])
    post_content = RichTextField(null=False, blank=False, default="Post content", validators=[validate_post_content_for_post])
    post_category = models.CharField(max_length=200, default='programming', validators=[validate_post_category_for_post])
    post_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    favorites = models.ManyToManyField(User, through='Favorite', related_name='favorite_posts')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        ordering = ['-pk']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        unique_together = ('post_title', 'post_content')
        
    
    def total_likes(self):
        """
        Returns the total number of likes for the post.

        Returns:
            int: Total number of likes.
        """
        return self.likes
    
    def increase_likes(self):
        """
        Increases the number of likes for the post by 1.
        """
        self.likes += 1
        self.save()
    
    def decrease_likes(self):
        """
        Decreases the number of likes for the post by 1, if the current count is greater than 0.
        """
        if self.likes > 0:
            self.likes -= 1
            self.save()
            
    def total_posts(self):
        """
        Returns the total number of posts.

        Returns:
            int: Total number of posts.
        """
        return self.post_title.count()
    
    def __str__(self):
        """
        Returns a string representation of the post.

        Returns:
            str: Post title.
        """
        return self.post_title
    
    def get_absolute_url(self):
        """
        Returns the absolute URL of the post.

        Returns:
            str: Absolute URL of the post.
        """
        return reverse('home')

''' Validators for Category Model '''
def validate_name_for_category(value):
    """
    Validates the name field for a category.

    Args:
        value (str): The value of the name field.

    Raises:
        ValidationError: If the name field is empty, exceeds the maximum length of 30 characters,
                         or contains non-Latin characters.
    """
    if len(value) == 0:
        raise ValidationError("Fill in the field Name")
    if len(value) > 30:
        raise ValidationError("Category name exceeds the maximum length of 30 characters")
    if not value.isascii():
        raise ValidationError("Category name should only contain Latin characters")
    
def validate_description_for_category(value):
    """
    Validates the description field for a category.

    Args:
        value (str): The value of the description field.

    Raises:
        ValidationError: If the description field exceeds the maximum length of 1000 characters.
    """
    if len(value) > 1000:
        raise ValidationError("Comment content exceeds the maximum length of 1000 characters")

def validate_icon_for_category(value):
    """
    Validates the icon field for a category.

    Args:
        value (File): The value of the icon field.

    Raises:
        ValidationError: If the icon file does not have a '.ico' extension.
    """
    if value:
        if not value.name.endswith('.ico'):
            raise ValidationError("Only ICO files are allowed.")

def validate_svg(value):
    """
    Validates an SVG file for a category.

    Args:
        value (File): The SVG file to validate.

    Raises:
        ValidationError: If the SVG file does not have a '.svg' extension.
    """
    if not value.name.endswith('.svg'):
        raise ValidationError(_('Only SVG files are allowed.'))
''' Validators for Category Model '''
    
class Category(models.Model):
    """
    Represents a category.
    
    Inherits from Model.

    Attributes:
        name (str): The name of the category.
        description (RichTextField): The description of the category.
        icon (ImageField): An image representing the category.
        svg_icon (FileField): An SVG file representing the category.

    Meta:
        verbose_name (str): The singular name of the category.
        verbose_name_plural (str): The plural name of the category.

    Methods:
        __str__(): Returns the string representation of the category.
        get_absolute_url(): Returns the absolute URL of the category.
    """
    name = models.CharField(max_length=30, null=False, blank=False, validators=[validate_name_for_category])
    description = RichTextField(null=True, blank=True, validators=[validate_description_for_category])
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True, validators=[validate_icon_for_category])
    svg_icon = models.FileField(upload_to='category_icons/', blank=True, null=True, validators=[validate_svg])
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        Returns a string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.name
    
    def get_absolute_url(self):
        """
        Returns the absolute URL of the category.

        Returns:
            str: The absolute URL of the category.
        """
        return reverse('home')

''' Validators for Comment Model '''
def validate_name_for_comment(value):
    """
    Validate the name for a comment.

    Args:
        value (str): The name to be validated.

    Raises:
        ValidationError: If the name is empty or exceeds the maximum length of 200 characters.
    """
    if len(value) == 0:
        raise ValidationError("Fill in the field Name")
    if len(value) > 200:
        raise ValidationError("Name exceeds the maximum length of 200 characters")

def validate_comment_content_for_comment(value):
    """
    Validate the comment content for a comment.

    Args:
        value (str): The comment content to be validated.

    Raises:
        ValidationError: If the comment content is empty or exceeds the maximum length of 1000 characters.
    """
    if len(value) == 0:
        raise ValidationError("Fill in the field Comment content")
    if len(value) > 1000:
        raise ValidationError("Comment content exceeds the maximum length of 1000 characters")
''' Validators for Comment Model '''

class Comment(models.Model):
    """
    Represents a comment on a post.
    
    Inherits from Model.

    Attributes:
        post (ForeignKey): The post that the comment belongs to.
        name (CharField): The name of the commenter.
        comment_content (RichTextField): The content of the comment.
        comment_date (DateTimeField): The date and time when the comment was made.

    Meta:
        verbose_name (str): The singular name of the comment.
        verbose_name_plural (str): The plural name of the comment.

    Methods:
        __str__(): Returns the string representation of the comment.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, validators=[validate_name_for_comment])
    comment_content = RichTextField(null=False, blank=False, default="Comment", validators=[validate_comment_content_for_comment])
    comment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        """
        Returns a string representation of the comment.

        Returns:
            str: A formatted string containing the post ID and commenter's name.
        """
        return '%s - %s' % (self.post.id, self.name)
    
class Favorite(models.Model):
    """
    Represents a favorite relationship between a user and a post.
    
    Inherits from Model.

    Attributes:
        post (ForeignKey): The post that is being favorited.
        user (ForeignKey): The user who favorited the post.
        created_at (DateTimeField): The date and time when the favorite relationship was created.

    Meta:
        verbose_name (str): The singular name of the favorite relationship.
        verbose_name_plural (str): The plural name of the favorite relationship.
        unique_together (tuple): Specifies that the combination of 'post' and 'user' should be unique.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        unique_together = ('post', 'user')
    