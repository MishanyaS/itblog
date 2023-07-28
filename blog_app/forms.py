from django import forms
from .models import Post, Category, Comment
from django.utils.translation import gettext_lazy as _



choices = Category.objects.all().values_list('name', 'name')
choices_list = []

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    """
    Form class for creating and editing Post objects.
    
    Inherits from ModelForm.
        
    Meta:
        model (str): The model that the form is based on.
        fields (str): The fields from the Post model that should be included in the form.
        widgets (str): The widgets to be used for rendering each form field.
        labels (str): The labels to be displayed for each form field.

    Methods:
        clean_post_title(): Returns cleaned and validated post title.
    """
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model=Post
        fields = ('post_title', 'post_image', 'post_content', 'post_category', 'post_author')
        
        widgets = {
            'post_title': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Post Title'), 'id': 'post_title_id'}),
            'post_image': forms.FileInput(attrs={'class':'form-control', 'id': 'post_image_id'}),
            'post_content': forms.Textarea(attrs={'class':'form-control', 'id': 'post_content_id'}),
            'post_category': forms.Select(choices=choices_list, attrs={'class':'form-select', 'id': 'post_category_id'}),
            'post_author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'post_author_id', 'type':'hidden'}),
        }
        
        labels = {
            'post_title': _('Post Title'),
            'post_image': _('Post Image'),
            'post_content': _('Post Content'),
            'post_category': _('Post Category'),
            'post_author': _('Post Author'),
        }
        
    def clean_post_title(self):
        """
        Cleans and validates the post title.

        Returns:
            str: The cleaned post title.

        Raises:
            forms.ValidationError: If a post with the same title already exists.
        """
        post_title = self.cleaned_data['post_title']
        if Post.objects.filter(post_title=post_title).exists():
            raise forms.ValidationError(f'Post with title \"{post_title}\" already exists. Choose other name for your post')
        return post_title
        
class EditPostForm(forms.ModelForm):
    """
    Form class for creating and editing Post objects.

    Inherits from ModelForm.
        
    Meta:
        model (str): The model that the form is based on.
        fields (str): The fields from the Post model that should be included in the form.
        widgets (str): The widgets to be used for rendering each form field.
        labels (str): The labels to be displayed for each form field.
    """
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model=Post
        fields = ('post_title', 'post_image', 'post_content', 'post_category', 'post_author')
        
        widgets = {
            'post_title': forms.TextInput(attrs={'class':'form-control', 'id': 'post_title_id'}),
            'post_image': forms.FileInput(attrs={'class':'form-control', 'id': 'post_image_id'}),
            'post_content': forms.Textarea(attrs={'class':'form-control', 'id': 'post_content_id'}),
            'post_category': forms.Select(choices=choices_list, attrs={'class':'form-select', 'id': 'post_category_id'}),
            'post_author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'post_author_id', 'type':'hidden'}),
        }
        
        labels = {
            'post_title': _('Post Title'),
            'post_image': _('Post Image'),
            'post_content': _('Post Content'),
            'post_category': _('Post Category'),
            'post_author': _('Post Author'),
        }

class CategoryForm(forms.ModelForm):
    """
    Form class for creating and editing Category objects.
    
    Inherits from ModelForm.
        
    Meta:
        model (str): The model that the form is based on.
        fields (str): The fields from the Category model that should be included in the form.
        widgets (str): The widgets to be used for rendering each form field.
        labels (str): The labels to be displayed for each form field.

    Methods:
        clean_name(): Returns validated the uniqueness name.
    """
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model = Category
        fields = ('name', 'description', 'icon', 'svg_icon')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name'), 'id':'name_id'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'id':'description_id'}),
            'icon': forms.FileInput(attrs={'class':'form-control', 'id':'icon_id'}),
            'svg_icon': forms.FileInput(attrs={'class':'form-control', 'id':'svg_icon_id'}),
        }
        
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'icon': _('Icon'),
            'svg_icon': _('Svg Icon'),
        }
        
    def clean_name(self):
        """
        Validates the uniqueness of the name field.
        
        Raises:
            forms.ValidationError: If a Category with the same name already exists.
        
        Returns:
            str: The cleaned name value.
        """
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError(f'Category {name} already exists.')
        return name

class CommentForm(forms.ModelForm):
    """
    Form class for creating and editing Comment objects.
    
    Inherits from ModelForm.
        
    Meta:
        model (str): The model that the form is based on.
        fields (str): The fields from the Comment model that should be included in the form.
        widgets (str): The widgets to be used for rendering each form field.
        labels (str): The labels to be displayed for each form field.
    """
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model = Comment
        fields = ('name', 'comment_content')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name'), 'value':'', 'id':'comment_author_id', 'type':'hidden'}),
            'comment_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Comment Content'), 'id':'comment_content_id'}),
        }
        
        labels = {
            'name': _('Name'),
            'comment_content': _('Comment Content'),
        }
    
class EmailForm(forms.Form):
    """
    Form class for sending emails.
    
    Inherits from Form.
    
    Attributes:
        email (EmailField): Field for capturing the email address of the recipient.
        subject (CharField): Field for capturing the subject of the email.
        message (CharField): Field for capturing the body text of the email.
    """
    email = forms.EmailField(label=_('Email Address'))
    subject = forms.CharField(label=_('Subject'))
    message = forms.CharField(label=_('Email Text'), widget=forms.Textarea)