from django.urls import path
from . views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name="registration"),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
"""
Defines the URL patterns for routing requests to the corresponding views.

Each path() function represents a URL pattern with a specific route, view, and name.
The route is the URL pattern to match.
The view is the corresponding view function or class-based view.
The name is the unique name assigned to the URL pattern for reverse URL lookups.

The `urlpatterns` variable is a list that contains the URL patterns for routing requests to the corresponding views in a Django project. Each element in the list is created using the `path()` function, which takes three arguments: `route`, `view`, and `name`. Here's a breakdown of each path in the provided code:

1. Registration:
   - Route: registration/
   - View: UserRegisterView.as_view()
   - Name: 'registration'
   - Description: This pattern represents the registration page of the website. When the root URL is accessed, it maps to the UserRegisterView class-based view, which is responsible for displaying registration form.
   
2. Edit Profile:
   - Route: edit_profile/
   - View: UserEditView.as_view()
   - Name: 'edit_profile'
   - Description: This pattern represents the edit profile page of the website. When the 'edit_profile/' URL is accessed, it maps to the UserEditView class-based view, which allows users to edit their profile information.

3. Password:
   - Route: password/
   - View: PasswordsChangeView.as_view(template_name='registration/change_password.html')
   - Name: Not provided
   - Description: This pattern represents the password change page of the website. When the 'password/' URL is accessed, it maps to the PasswordsChangeView class-based view, which provides functionality for users to change their passwords. The template used for this view is 'registration/change_password.html'.

4. Password Success:
   - Route: password_success/
   - View: views.password_success
   - Name: 'password_success'
   - Description: This pattern represents the password change success page of the website. When the 'password_success/' URL is accessed, it maps to the views.password_success function, which displays a success message after a password change.

5. Profile:
   - Route: <int:pk>/profile/
   - View: ProfilePageView.as_view()
   - Name: 'profile_page'
   - Description: This pattern represents the user profile page of the website. It uses a dynamic integer parameter 'pk' to identify a specific user's profile. When a URL in the form of '<user_id>/profile/' is accessed, it maps to the ProfilePageView class-based view, which displays the profile information of the specified user.

6. Edit Profile Page:
   - Route: <int:pk>/edit_profile_page/
   - View: EditProfilePageView.as_view()
   - Name: 'edit_profile_page'
   - Description: This pattern represents the edit profile page of the website. It uses a dynamic integer parameter 'pk' to identify a specific user's profile. When a URL in the form of '<user_id>/edit_profile_page/' is accessed, it maps to the EditProfilePageView class-based view, which allows users to edit their profile information.

7. Create Profile Page:
   - Route: create_profile_page/
   - View: CreateProfilePageView.as_view()
   - Name: 'create_profile_page'
   - Description: This pattern represents the create profile page of the website. When the 'create_profile_page/' URL is accessed, it maps to the CreateProfilePageView class-based view, which handles the creation of a user profile page.

8. Password Reset:
   - Route: password_reset/
   - View: auth_views.PasswordResetView.as_view()
   - Name: 'password_reset'
   - Description: This pattern represents the password reset page of the website. When the 'password_reset/' URL is accessed, it maps to the auth_views.PasswordResetView class-based view, which initiates the password reset process.

9. Password Reset Done:
   - Route: password_reset/done/
   - View: auth_views.PasswordResetDoneView.as_view()
   - Name: 'password_reset_done'
   - Description: This pattern represents the password reset done page of the website. When the 'password_reset/done/' URL is accessed, it maps to the auth_views.PasswordResetDoneView class-based view, which displays a page confirming that a password reset email has been sent.

10. Password Reset Confirm:
    - Route: reset/<uidb64>/<token>/
    - View: auth_views.PasswordResetConfirmView.as_view()
    - Name: 'password_reset_confirm'
    - Description: This pattern represents the password reset confirmation page of the website. It uses dynamic parameters 'uidb64' and 'token' to identify a specific password reset request. When a URL in the form of 'reset/<uidb64>/<token>/' is accessed, it maps to the auth_views.PasswordResetConfirmView class-based view, which allows users to confirm and reset their password.

11. Password Reset Complete:
    - Route: reset/done/
    - View: auth_views.PasswordResetCompleteView.as_view()
    - Name: 'password_reset_complete'
    - Description: This pattern represents the password reset complete page of the website. When the 'reset/done/' URL is accessed, it maps to the auth_views.PasswordResetCompleteView class-based view, which displays a page confirming that a password reset has been successfully completed.

These patterns define the URLs that can be accessed in the Django project, and when a request matches a specific pattern, the corresponding 
view will be executed. The names assigned to each URL pattern can be used for reverse URL lookups, which allow you to dynamically generate 
URLs based on their names in your code.
"""