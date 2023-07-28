from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog_app.models import Profile
from django.utils.translation import gettext_lazy as _



class ProfilePageForm(forms.ModelForm):
    """
    Form class for creating and editing ProfilePage objects.
    
    Inherits from ModelForm.
    
    Attributes:
        forms (module): The module that provides form-related functionality.
        
    Meta:
        model (str): The model that the form is based on.
        fields (str): The fields from the ProfilePage model that should be included in the form.
        widgets (str): The widgets to be used for rendering each form field.
        labels (str): The labels to be displayed for each form field.
    """
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model=Profile
        fields=('user_photo', 'user_description', 'phone', 'user_link', 'user_birth_date', 'user_github_url')
        
        widgets={
            'user_photo': forms.FileInput(attrs={'class':'form-control', 'id':'user_photo_id'}),
            'user_description': forms.Textarea(attrs={'class':'form-control', 'placeholder': _('User Description'), 'id':'user_description_id'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Phone'), 'id':'phone_id'}),
            'user_link': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Social Network'), 'id':'user_link_id'}),
            'user_birth_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder': _('User Birth Date'), 'type':'date', 'id':'user_birth_date_id'}),
            'user_github_url': forms.TextInput(attrs={'class':'form-control', 'placeholder': _('User Github Url'), 'id':'user_github_url_id'}),
        }
        
        labels = {
            'user_photo': _('User Photo'),
            'user_description': _('User Description'),
            'phone': _('Phone'),
            'user_link': _('Social Network'),
            'user_birth_date': _('User Birth Date'),
            'user_github_url': _('User Github Url'),
        }

class SignUpForm(UserCreationForm):
    """
    A form for user sign-up with the following fields:
    - email
    - first_name
    - last_name
    
    Inherits from UserCreationForm.

    Attributes:
        email (forms.EmailField): Email field for the user's email address.
        first_name (forms.CharField): Field for the user's first name.
        last_name (forms.CharField): Field for the user's last name.

    Meta:
        model (User): The User model used for sign-up.
        fields (tuple): The fields to include in the form.
        labels (dict): Custom labels for the fields.

    Methods:
        __init__(self, *args, **kwargs): Initializes the SignUpForm.
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': _('Email'), 'id':'email_id'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('First Name'), 'id':'first_name_id'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Last Name'), 'id':'last_name_id'}))
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        labels = {
            'username': _('Username'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
        }
        
    def __init__(self, *args, **kwargs):
        """
        Initializes the SignUpForm.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = _('Username')
        self.fields['username'].widget.attrs['id'] = 'username_id'
        
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = _('First Name')
        self.fields['first_name'].widget.attrs['id'] = 'first_name_id'
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = _('Last Name')
        self.fields['last_name'].widget.attrs['id'] = 'last_name_id'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = _('Email')
        self.fields['email'].widget.attrs['id'] = 'email_id'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = _('Password')
        self.fields['password1'].widget.attrs['id'] = 'password1_id'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = _('Confirm Password')
        self.fields['password2'].widget.attrs['id'] = 'password2_id'
        
class EditProfileForm(UserChangeForm):
    """
    A form for editing user profile with the following fields:
    - username
    - first_name
    - last_name
    - email
    - last_login
    - date_joined
    
    Inherits from UserChangeForm.

    Attributes:
        username (forms.CharField): Field for the user's username.
        first_name (forms.CharField): Field for the user's first name.
        last_name (forms.CharField): Field for the user's last name.
        email (forms.EmailField): Field for the user's email address.
        last_login (forms.CharField): Field for the user's last login time.
        date_joined (forms.CharField): Field for the user's registration date.

    Meta:
        model (User): The User model used for editing the profile.
        fields (tuple): The fields to include in the form.
        labels (dict): Custom labels for the fields.
    """
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Username'), 'id':'username_id'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('First Name'), 'id':'first_name_id'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Last Name'), 'id':'last_name_id'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': _('Email'), 'id':'email', 'value':'', 'id':'email_id'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Last Login'), 'id':'last_login_id', 'disabled': 'disabled'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Date Joined'), 'id':'date_joined_id', 'disabled': 'disabled'}))
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'date_joined')
        
        labels = {
            'username': _('Username'),
            'first_name': _('First Name'),
            'email': _('Email'),
            'last_name': _('Last Name'),
            'password': _('Password'),
            'last_login': _('Last Login'),
            'date_joined': _('Date Joined'),
        }
        
class PasswordChangingForm(PasswordChangeForm):
    """
    A form for changing the user's password with the following fields:
    - old_password
    - new_password1
    - new_password2
    
    Inherits from PasswordChangeForm.

    Attributes:
        old_password (forms.CharField): Field for the user's old password.
        new_password1 (forms.CharField): Field for the user's new password.
        new_password2 (forms.CharField): Field for confirming the new password.

    Meta:
        model (User): The User model used for changing the password.
        fields (tuple): The fields to include in the form.
        labels (dict): Custom labels for the fields.
    """
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder': _('Old Password'), 'id':'old_password_id'}))
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder': _('New Password1'), 'id':'new_password1_id'}))
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder': _('New Password2'), 'id':'new_password2_id'}))
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        model=User
        fields=('old_password', 'new_password1', 'new_password2')
        
        labels = {
            'old_password': _('Old Password'),
            'new_password1': _('New Password1'),
            'new_password2': _('New Password2'),
        }
        