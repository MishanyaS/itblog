from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from . forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blog_app.models import Profile, Post
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

# Create your views here.



class CreateProfilePageView(CreateView):
    """
    A class-based view for creating a profile page.
    
    Inherits from CreateView.

    Attributes:
    - model (Profile): The model class representing the profile.
    - form_class (ProfilePageForm): The form class used for creating the profile page.
    - template_name (str): The name of the template used for rendering the create profile page.

    Methods:
    - form_valid(form): Overrides the form_valid method of the parent class to set the user instance on the form.
    """
    model=Profile
    form_class=ProfilePageForm
    template_name='registration/create_profile_page.html'
    
    def form_valid(self, form):
        """
        Override the form_valid method to set the user instance on the form.

        Args:
        - form (ProfilePageForm): The form instance.

        Returns:
        - super().form_valid(form): The result of calling the form_valid method of the parent class.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    """
    A class-based view for editing a profile page.
    
    Inherits from UpdateView.

    Attributes:
    - model (Profile): The model class representing the profile.
    - form_class (ProfilePageForm): The form class used for editing the profile page.
    - template_name (str): The name of the template used for rendering the edit profile page.
    - success_url (str): The URL to redirect to after successfully editing the profile page.

    Methods:
    - get_success_url(): Returns the success URL for the view.
    """
    model=Profile
    form_class=ProfilePageForm
    template_name='registration/edit_profile_page.html'
    success_url = reverse_lazy('home')

class ProfilePageView(DetailView):
    """
    A class-based view for displaying a profile page.
    
    Inherits from DetailView.

    Attributes:
    - model (Profile): The model class representing the profile.
    - template_name (str): The name of the template used for rendering the profile page.

    Methods:
    - get_context_data(*args, **kwargs): Returns the context data for rendering the profile page.

    Args:
    - *args: Variable length argument list.
    - **kwargs: Arbitrary keyword arguments.
    """
    model=Profile
    template_name='registration/profile.html'
    
    def get_context_data(self, *args, **kwargs):
        """
        Returns the context data for rendering the profile page.

        Args:
        - *args: Variable length argument list.
        - **kwargs: Arbitrary keyword arguments.

        Returns:
        - context (dict): The context data for rendering the profile page.
        """
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        current_user = self.object.user
        posts = Post.objects.filter(post_author=current_user)
        
        posts_count = posts.count()
                
        context["page_user"] = page_user
        context['posts'] = posts
        context['posts_count'] = posts_count
        return context

class PasswordsChangeView(PasswordChangeView):
    """
    A class-based view for changing passwords.
    
    Inherits from PasswordChangeView.

    Attributes:
    - form_class (class): The form class used for password changing.
    - success_url (str): The URL to redirect to upon successful password change.
    """
    form_class=PasswordChangingForm
    success_url = reverse_lazy('password_success')
    
def password_success(request):
    """
    Renders the password success page.

    Args:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered password success page.
    """
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    """
    A class-based view for user registration.
    
    Inherits from CreateView.

    Attributes:
    - form_class (class): The form class used for user registration.
    - template_name (str): The name of the template used for rendering the registration page.
    - success_url (str): The URL to redirect to upon successful user registration.
    """
    form_class=SignUpForm
    template_name='registration/registration.html'
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    """
    A class-based view for editing user profile.
    
    Inherits from UpdateView.

    Attributes:
    - form_class (class): The form class used for editing user profile.
    - template_name (str): The name of the template used for rendering the edit profile page.
    - success_url (str): The URL to redirect to upon successful profile update.

    Methods:
    - get_object(): Retrieves the object to be edited.
    """
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        """
        Retrieves the object to be edited.

        Returns:
        - Object: The user object to be edited.
        """
        return self.request.user


def set_language(request, language):
    """
    View function for setting the language and redirecting to the appropriate page.

    Args:
        request (HttpRequest): The HTTP request object.
        language (str): The language code to set.

    Returns:
        HttpResponse: The HTTP response for redirecting to the appropriate page.
    """
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response