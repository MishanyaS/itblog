from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from users.forms import ProfilePageForm, SignUpForm, EditProfileForm, PasswordChangingForm
from datetime import datetime
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.

#----------------------------------------------------Views for Users---------------------------------------------------

class CreateProfilePageViewTest(TestCase):
    """
    A test case for the create profile page view.

    Methods:
        test_create_profile_page_view(): Test the create profile page view.
    """
    def test_create_profile_page_view(self):
        """
        Test the create profile page view.
        """
        # user = User.objects.create(username='testuser')
        url = reverse('create_profile_page')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/create_profile_page.html')
        
class EditProfilePageViewTest(TestCase):
    """
    A test case for the edit profile page view.

    Methods:
        test_edit_profile_page_view(): Test the edit profile page view.
    """
    def test_edit_profile_page_view(self):
        """
        Test the edit profile page view.
        """
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        url = reverse('edit_profile_page', kwargs={'pk': user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
        #self.assertTemplateUsed(response, 'registration/edit_profile_page.html')
        
class ProfilePageViewTest(TestCase):
    """
    A test case for the profile page view.

    Methods:
        test_profile_page_view(): Test the profile page view.
    """
    def test_profile_page_view(self):
        """
        Test the profile page view.
        """
        user = User.objects.create(username='testuser')
        url = reverse('profile_page', kwargs={'pk': user.pk})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 404)
        #self.assertTemplateUsed(response, 'registration/profile.html')
        
class PasswordsChangeViewTest(TestCase):
    """
    A test case for the password change view.

    Methods:
        test_password_success_view(): Test the password success view.
    """
    def test_password_success_view(self):
        """
        Test the password success view.
        """
        # user = User.objects.create(username='testuser')
        url = reverse('password_success')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_success.html')
        
class UserRegisterViewTest(TestCase):
    """
    A test case for the user registration view.

    Methods:
        test_registration_view(): Test the registration view.
    """
    def test_registration_view(self):
        """
        Test the registration view.
        """
        # user = User.objects.create(username='testuser')
        url = reverse('registration')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')
        
class UserEditViewTest(TestCase):
    """
    A test case for the user edit view.

    Methods:
        test_registration_view(): Test the registration view.
    """
    def test_registration_view(self):
        """
        Test the registration view.
        """
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        url = reverse('edit_profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/edit_profile.html')
        
#----------------------------------------------------Forms for Users---------------------------------------------------

class ProfilePageFormTest(TestCase):
    """
    A test case for the profile page form.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """
    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        user = User.objects.create(username='testuser')
                
        form_data = {'user': user.pk, 'user_description': 'User', 'phone': '1234567890', 'user_link': 'https://www.google.com.ua', 'user_birth_date': datetime.strptime('01.01.2000', '%d.%m.%Y'), 'user_github_url': 'https://github.com/MishanyaS'}  # Enter values for the form fields
        form = ProfilePageForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        user = User.objects.create(username='testuser')
        
        form_data = {'user': user.pk, 'user_description': 'User', 'phone': '12345678', 'user_link': 'https://www.google.com.ua', 'user_birth_date': '01.01.2000', 'user_github_url': 'https://github.com/MishanyaS'}  # Enter invalid values for the form fields
        form = ProfilePageForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)


class SignUpFormTest(TestCase):
    """
    A test case for the sign-up form.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """
    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        #user = User.objects.create(username='testuser')
        form_data = {'username': 'username', 'first_name': 'firstname10', 'last_name': 'lastname10', 'email': 'user@mail.com', 'password1': 'Pass12345', 'password2': 'Pass12345'}  # Enter values for the form fields
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        #user = User.objects.create(username='testuser')
        form_data = {'username': '', 'first_name': '', 'last_name': '', 'email': '', 'password1': '', 'password2': ''}  # Enter invalid values for the form fields
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)


class EditProfileFormTest(TestCase):
    """
    A test case for the edit profile form.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """
    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        form_data = {'username': 'username', 'first_name': 'firstname10', 'email': 'user@mail.com', 'last_name': 'lastname10', 'password': 'Pass12345', 'last_login': datetime.today(), 'date_joined': datetime.strptime('01.01.2000', '%d.%m.%Y')}  # Enter values for the form fields
        form = EditProfileForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        form_data = {'username': '', 'first_name': '', 'email': '', 'last_name': '', 'password': '', 'last_login': '', 'date_joined': ''}  # Enter invalid values for the form fields
        form = EditProfileForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)


class PasswordChangingFormTest(TestCase):
    """
    A test case for the password changing form.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """
    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        user = User.objects.create(username='user1')
        user.set_password('Pass12345')
        user.save()

        form_data = {'old_password': 'Pass12345', 'new_password1': 'Passw54321', 'new_password2': 'Passw54321'}
        form = PasswordChangingForm(user=user, data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        user = User.objects.create(username='user1')
        user.set_password('Pass12345')
        user.save()

        form_data = {'user': '', 'old_password': '', 'new_password1': '', 'new_password2': ''}
        form = PasswordChangingForm(user=user, data=form_data)
        self.assertFalse(form.is_valid(), form.errors)

#----------------------------------------------------Selenium tests---------------------------------------------------

# Test will completed if user is not authorized
class RegAuthFormsTest(LiveServerTestCase):
    """
    A test case for registration and authentication forms.

    Methods:
        testRegForm(): Test the registration form.
        testAuthForm(): Test the authentication form.
    """
    def testRegForm(self):
        """
        Test the registration form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/users/registration/')
        
        time.sleep(5)
        
        username = selenium.find_element('id', 'username_id')
        first_name = selenium.find_element('id', 'first_name_id')
        last_name = selenium.find_element('id', 'last_name_id')
        email = selenium.find_element('id', 'email_id')
        password1 = selenium.find_element('id', 'password1_id')
        password2 = selenium.find_element('id', 'password2_id')

        submit = selenium.find_element('id', 'register_button_id')

        username.send_keys('user3')
        first_name.send_keys('First Name3')
        last_name.send_keys('Last Name3')
        email.send_keys('user3@mail.com')
        password1.send_keys('user312345')
        password2.send_keys('user312345')
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)
    
    def testAuthForm(self):
        """
        Test the authentication form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/users/login/')
        
        time.sleep(5)
        
        username = selenium.find_element('id', 'username_id')
        password1 = selenium.find_element('id', 'password_id')

        submit = selenium.find_element('id', 'login_button_id')

        username.send_keys('user1')
        password1.send_keys('user112345')
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)

class ProfileSettingsFormsTest(LiveServerTestCase):
    """
    A test case for profile settings forms.

    Methods:
        testChangePasswordForm(): Test the change password form.
        testCreateProfilePageForm(): Test the create profile page form.
        testEditProfilePageForm(): Test the edit profile page form.
        testEditProfileForm(): Test the edit profile form.
    """
    # Will not work
    def testChangePasswordForm(self):
        """
        Test the change password form.
        """
        #For this test you have to login as user1
        
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/users/password/')
        
        time.sleep(5)
        
        old_password = selenium.find_element('id', 'old_password_id')
        new_password1 = selenium.find_element('id', 'new_password1_id')
        new_password2 = selenium.find_element('id', 'new_password2_id')

        submit = selenium.find_element('id', 'change_password_button_id')

        old_password.send_keys('user112345')
        new_password1.send_keys('user154321')
        new_password2.send_keys('user154321')
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)
    #+
    def testCreateProfilePageForm(self):
        """
        Test the create profile page form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/users/create_profile_page/')
        
        time.sleep(5)
        
        user_photo = selenium.find_element('id', 'user_photo_id')
        user_description = selenium.find_element('id', 'user_description_id')
        phone = selenium.find_element('id', 'phone_id')
        user_link = selenium.find_element('id', 'user_link_id')
        user_birth_date = selenium.find_element('id', 'user_birth_date_id')
        user_github_url = selenium.find_element('id', 'user_github_url_id')

        submit = selenium.find_element('id', 'create_profile_page_button_id')

        user_photo.send_keys(None)
        user_description.send_keys('user')
        phone.send_keys('12345678')
        user_link.send_keys('https://www.google.com.ua/')
        user_birth_date.send_keys(datetime.strptime('01.01.2000', '%d.%m.%Y'))
        user_github_url.send_keys('https://github.com/MishanyaS')
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)
    #+    
    def testEditProfilePageForm(self):
        """
        Test the edit profile page form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/users/1/edit_profile_page/')
        
        time.sleep(5)
        
        user_photo = selenium.find_element('id', 'user_photo_id')
        user_description = selenium.find_element('id', 'user_description_id')
        phone = selenium.find_element('id', 'phone_id')
        user_link = selenium.find_element('id', 'user_link_id')
        user_birth_date = selenium.find_element('id', 'user_birth_date_id')
        user_github_url = selenium.find_element('id', 'user_github_url_id')

        submit = selenium.find_element('id', 'edit_profile_page_button_id')

        user_photo.send_keys(None)
        user_description.send_keys('user')
        phone.send_keys('12345678')
        user_link.send_keys('https://www.google.com.ua/')
        user_birth_date.send_keys(datetime.strptime('01.01.2000', '%d.%m.%Y'))
        user_github_url.send_keys('https://github.com/MishanyaS')
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)
    # Will not work
    def testEditProfileForm(self):
        """
        Test the edit profile form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/users/edit_profile/')
        
        time.sleep(5)
        
        username = selenium.find_element('id', 'username_id')
        first_name = selenium.find_element('id', 'first_name_id')
        email = selenium.find_element('id', 'email_id')
        last_name = selenium.find_element('id', 'last_name_id')
        password = selenium.find_element('id', 'password_id')

        submit = selenium.find_element('id', 'edit_profile_button_id')

        username.send_keys('user11')
        first_name.send_keys('First Name11')
        email.send_keys('user11@mail.com')
        last_name.send_keys('Last Name11')
        password.send_keys('user11234554321')
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)
        
