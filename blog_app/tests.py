from django.test import TestCase, LiveServerTestCase
from blog_app.models import Profile, Post, Category, Comment, Favorite
from django.contrib.auth.models import User
from django.urls import reverse
from blog_app.forms import PostForm, EditPostForm, CommentForm, CategoryForm, EmailForm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create your tests here.

class ProfileModelTest(TestCase):
    """
    A test case for the Profile model.

    Attributes:
        user (User): A User instance representing the user associated with the profile.
        profile (Profile): A Profile instance created for testing.

    Methods:
        setUp(): Set up the necessary objects for the test case.
        test_profile(): Test the profile's user username.
    """
    def setUp(self):
        """
        Set up the necessary objects for the test case.

        Meta:
            Creates a User instance with the username "user" and a corresponding Profile instance.
        """
        self.user = User.objects.create(username="user")
        self.profile = Profile.objects.create(user=self.user)

    def test_profile(self):
        """
        Test the profile's user username.
        """
        self.assertEqual(self.profile.user.username, "user")
        
class PostModelTest(TestCase):
    """
    A test case for the Post model.

    Attributes:
        user (User): A User instance representing the user associated with the post.
        post (Post): A Post instance created for testing.

    Methods:
        setUp(): Set up the necessary objects for the test case.
        test_post(): Test the post's title.
    """
    def setUp(self):
        """
        Set up the necessary objects for the test case.

        Meta:
            Creates a User instance with the username "user" and a corresponding Post instance with a title.
        """
        self.user = User.objects.create(username="user")
        self.post = Post.objects.create(post_title="post title", post_author=self.user)

    def test_post(self):
        """
        Test the post's title.
        """
        self.assertEqual(self.post.post_title, "post title")
        
class CategoryModelTest(TestCase):
    """
    A test case for the Category model.

    Attributes:
        category (Category): A Category instance created for testing.

    Methods:
        setUp(): Set up the necessary objects for the test case.
        test_category(): Test the category's name.
    """
    def setUp(self):
        """
        Set up the necessary objects for the test case.

        Meta:
            Creates a Category instance with a name.
        """
        self.category = Category.objects.create(name="category")

    def test_category(self):
        """
        Test the category's name.
        """
        self.assertEqual(self.category.name, "category")

class CommentModelTest(TestCase):
    """
    A test case for the Comment model.

    Attributes:
        user (User): A User instance representing the user associated with the comment.
        post (Post): A Post instance associated with the comment.
        comment (Comment): A Comment instance created for testing.

    Methods:
        setUp(): Set up the necessary objects for the test case.
        test_comment(): Test the comment's name and content.
    """
    def setUp(self):
        """
        Set up the necessary objects for the test case.

        Meta:
            Creates a User instance with the username "user", a corresponding Post instance, and a Comment instance with a name and content.
        """
        self.user = User.objects.create(username="user")
        self.post = Post.objects.create(post_title="post title", post_author=self.user)
        self.comment = Comment.objects.create(post=self.post, name="name", comment_content="comment1")

    def test_comment(self):
        """
        Test the comment's name and content.
        """
        self.assertEqual(self.comment.name, "name")
        self.assertEqual(self.comment.comment_content, "comment1")
        
class FavoriteModelTest(TestCase):
    """
    A test case for the Favorite model.

    Attributes:
        user (User): A User instance representing the user associated with the favorite.
        post (Post): A Post instance associated with the favorite.
        favorite (Favorite): A Favorite instance created for testing.

    Methods:
        setUp(): Set up the necessary objects for the test case.
        test_favorite(): Test the favorite's user and post.
    """
    def setUp(self):
        """
        Set up the necessary objects for the test case.

        Meta:
            Creates a User instance with the username "user", a corresponding Post instance, and a Favorite instance linking the user and post.
        """
        self.user = User.objects.create(username="user")
        self.post = Post.objects.create(post_title="post title", post_author=self.user)
        self.favorite = Favorite.objects.create(post=self.post, user=self.user)

    def test_favorite(self):
        """
        Test the favorite's user and post.
        """
        self.assertEqual(self.favorite.user.username, "user")
        self.assertEqual(self.favorite.post.post_title, "post title")

#----------------------------------------------------View for Blog---------------------------------------------------

class HomeViewTest(TestCase):
    """
    A test case for the HomeView.

    Methods:
        test_home_view(): Test the home view.
    """
    def test_home_view(self):
        """
        Test the home view.
        """
        url = reverse('home')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
class CategoryListViewTest(TestCase):
    """
    A test case for the CategoryListView.

    Methods:
        test_category_list_view(): Test the category list view.
    """
    def test_category_list_view(self):
        """
        Test the category list view.
        """
        url = reverse('category_list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/category_list.html')
        
class CategoryViewTest(TestCase):
    """
    A test case for the CategoryView.

    Methods:
        test_category_view(): Test the category view.
    """
    def test_category_view(self):
        """
        Test the category view.
        """
        url = reverse('category', kwargs={'cats': 'category'})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/categories.html')

class PostDetailsViewTest(TestCase):
    """
    A test case for the PostDetailsView.

    Methods:
        test_category_view(): Test the post details view.
    """
    def test_category_view(self):
        """
        Test the post details view.
        """
        user = User.objects.create(username='testuser')
        post = Post.objects.create(post_title='Test Post', post_author=user)
        url = reverse('profile_page', args=[post.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'posts/post_details.html')

class LikePostViewTest(TestCase):
    """
    A test case for the LikePostView.

    Methods:
        test_like_post_view(): Test the like post view.
    """
    def test_like_post_view(self):
        """
        Test the like post view.
        """
        user = User.objects.create(username='testuser')
        post = Post.objects.create(post_title='Test Post', post_author=user)
        url = reverse('like_post', args=[post.pk])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 302)
        
class AddPostViewTest(TestCase):
    """
    A test case for the AddPostView.

    Methods:
        test_add_post_view(): Test the add post view.
    """
    def test_add_post_view(self):
        """
        Test the add post view.
        """
        user = User.objects.create(username='testuser')
        url = reverse('add_post')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/add_post.html')
        
class AddCommentViewTest(TestCase):
    """
    A test case for the AddCommentView.

    Methods:
        test_add_comment_view(): Test the add comment view.
    """
    def test_add_comment_view(self):
        """
        Test the add comment view.
        """
        user = User.objects.create(username='testuser')
        post = Post.objects.create(post_title='Test Post', post_author=user)
        url = reverse('add_comment', args=[post.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/add_comment.html')
        
class AddCategoryViewTest(TestCase):
    """
    A test case for the AddCategoryView.

    Methods:
        test_add_category_view(): Test the add category view.
    """
    def test_add_category_view(self):
        """
        Test the add category view.
        """
        url = reverse('add_category')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/add_category.html')
        
class EditPostViewTest(TestCase):
    """
    A test case for the EditPostView.

    Methods:
        test_edit_post_view(): Test the edit post view.
    """
    def test_edit_post_view(self):
        """
        Test the edit post view.
        """
        user = User.objects.create(username='testuser')
        post = Post.objects.create(post_title='Test Post', post_author=user)
        url = reverse('edit_post', args=[post.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/edit_post.html')
        
class DeletePostViewTest(TestCase):
    """
    A test case for the DeletePostView.

    Methods:
        test_delete_post_view(): Test the delete post view.
    """
    def test_delete_post_view(self):
        """
        Test the delete post view.
        """
        user = User.objects.create(username='testuser')
        post = Post.objects.create(post_title='Test Post', post_author=user)
        url = reverse('delete_post', args=[post.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/delete_post.html')
        
class HelpViewTest(TestCase):
    """
    A test case for the HelpView.

    Methods:
        test_help_view(): Test the help view.
    """
    def test_help_view(self):
        """
        Test the help view.
        """
        url = reverse('help')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'help/help.html')
        
class ContactsViewTest(TestCase):
    """
    A test case for the ContactsView.

    Methods:
        test_contacts_view(): Test the contacts view.
    """
    def test_contacts_view(self):
        """
        Test the contacts view.
        """
        url = reverse('contacts')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contacts.html')
        
class FavoriteListViewTest(TestCase):
    """
    A test case for the FavoriteListView.

    Attributes:
        user (User): A User instance created for testing.

    Methods:
        setUp(): Set up the necessary objects for the test case.
        test_favorite_list_view(): Test the favorite list view.
    """
    def setUp(self):
        """
        Set up the necessary objects for the test case.
        """
        self.user = User.objects.create(username='testuser')
        self.client.force_login(self.user)
        
    def test_favorite_list_view(self):
        """
        Test the favorite list view.
        """
        url = reverse('favorite_list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorite/favorite_list.html')
        
#----------------------------------------------------Forms for Blog---------------------------------------------------

class PostFormTest(TestCase):
    """
    A test case for the PostForm.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """

    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='category')
        
        form_data = {'post_title': 'Post 1', 'post_content': 'Post 1 content', 'post_category': category, 'post_author': user.pk}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        form_data = {'post_title': '', 'post_content': '', 'post_category': '', 'post_author': ''}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)


class EditPostFormTest(TestCase):
    """
    A test case for the EditPostForm.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """

    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='category')
        
        form_data = {'post_title': 'Post 1', 'post_content': 'Post 1 content', 'post_category': category, 'post_author': user.pk}
        form = EditPostForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        form_data = {'post_title': '', 'post_content': '', 'post_category': '', 'post_author': ''}
        form = EditPostForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)


class CommentFormTest(TestCase):
    """
    A test case for the CommentForm.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """
    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        user = User.objects.create(username='testuser')
        
        form_data = {'name': user.username, 'comment_content': 'Comment 1'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        form_data = {'name': '', 'comment_content': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)


class CategoryFormTest(TestCase):
    """
    A test case for the CategoryForm.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """
    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        form_data = {'name': 'java', 'description': 'Java programming language'}
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        form_data = {'name': '', 'description': ''}
        form = CategoryForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)


class EmailFormTest(TestCase):
    """
    A test case for the EmailForm.

    Methods:
        test_form_valid_data(): Test the form with valid data.
        test_form_invalid_data(): Test the form with invalid data.
    """
    def test_form_valid_data(self):
        """
        Test the form with valid data.
        """
        form_data = {'email': 'user1@mail.com','subject': 'Subject','message': 'Text'}
        form = EmailForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalid_data(self):
        """
        Test the form with invalid data.
        """
        form_data = {'email': '','subject': '','message': ''}
        form = EmailForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)

#----------------------------------------------------Selenium tests---------------------------------------------------

# Test will not be completed because user is not authorized
class CategoryFormsTest(LiveServerTestCase):
    """
    A test case for category forms.

    Methods:
        testAddCategoryForm(): Test adding a category form.
    """
    def testAddCategoryForm(self):
        """
        Test adding a category form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/add_category/')
        
        time.sleep(5)
        
        name = selenium.find_element('id', 'name_id')
        description = selenium.find_element('id', 'description_id')
        icon = selenium.find_element('id', 'icon_id')
        svg_icon = selenium.find_element('id', 'svg_icon_id')

        submit = selenium.find_element('id', 'add_category_button_id')

        name.send_keys('category')
        description.send_keys('category description')
        icon.send_keys(None)
        svg_icon.send_keys(None)
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)

# Test will not be completed because user is not authorized
class CommentFormTest(LiveServerTestCase):
    """
    A test case for comment forms.

    Methods:
        testAddCommentForm(): Test adding a comment form.
    """
    def testAddCommentForm(self):
        """
        Test adding a comment form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/post/24/add_comment/')
        
        time.sleep(5)
        
        name = selenium.find_element('id', 'comment_author_id')
        comment_content = selenium.find_element('id', 'comment_content_id')

        submit = selenium.find_element('id', 'add_comment_button_id')

        name.send_keys(None)
        comment_content.send_keys('comment')
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)

# Test will be completed
class ContactFormTest(LiveServerTestCase):
    """
    A test case for the contact form.

    Methods:
        testContactForm(): Test the contact form.
    """
    def testContactForm(self):
        """
        Test the contact form.
        """
        selenium = webdriver.Chrome()
        selenium.get(self.live_server_url + '/contacts/')

        wait = WebDriverWait(selenium, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, "send_email_button_id")))

        element.click()
        
        time.sleep(5)

        email = selenium.find_element(By.ID, 'email_id')
        subject = selenium.find_element(By.ID, 'subject_id')
        message = selenium.find_element(By.ID, 'message_id')

        submit = selenium.find_element(By.ID, 'send_button_id')

        email.send_keys('user1@mail.com')
        subject.send_keys('subject')
        message.send_keys('message')

        time.sleep(5)

        submit.send_keys(Keys.RETURN)

        selenium.quit()

# Test will not be completed because user is not authorized
class PostFormTest(LiveServerTestCase):
    """
    A test case for post forms.

    Methods:
        testAddPostForm(): Test adding a post form.
        testEditPostForm(): Test editing a post form.
    """
    def testAddPostForm(self):
        """
        Test adding a post form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/add_post/')
        
        time.sleep(5)
        
        post_title = selenium.find_element('id', 'post_title_id')
        post_image = selenium.find_element('id', 'post_image_id')
        post_content = selenium.find_element('id', 'post_content_id')
        post_category = selenium.find_element('id', 'post_category_id')
        post_author = selenium.find_element('id', 'post_author_id')

        submit = selenium.find_element('id', 'add_post_button_id')

        post_title.send_keys('post')
        post_image.send_keys(None)
        post_content.send_keys('post content')
        post_category.send_keys(None)
        post_author.send_keys(None)
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)
        
    def testEditPostForm(self):
        """
        Test editing a post form.
        """
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/post/edit/24')
        
        time.sleep(5)
        
        post_title = selenium.find_element('id', 'post_title_id')
        post_image = selenium.find_element('id', 'post_image_id')
        post_content = selenium.find_element('id', 'post_content_id')
        post_category = selenium.find_element('id', 'post_category_id')
        post_author = selenium.find_element('id', 'post_author_id')

        submit = selenium.find_element('id', 'edit_post_button_id')

        post_title.send_keys('post')
        post_image.send_keys(None)
        post_content.send_keys('post content')
        post_category.send_keys(None)
        post_author.send_keys(None)
        
        time.sleep(5)

        submit.send_keys(Keys.RETURN)      

