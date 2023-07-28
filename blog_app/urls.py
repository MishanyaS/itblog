from django.urls import path
from .views import HomeView, PostDetailsView, AddPostView, EditPostView, DeletePostView, AddCategoryView, category_view, category_list_view, AddCommentView, help, contacts, FavoriteListView, LikePostView



urlpatterns = [
    path(route='', view=HomeView.as_view(), name="home"),
    path(route='post/<int:pk>', view=PostDetailsView.as_view(), name="post_details"),
    path(route='add_post/', view=AddPostView.as_view(), name='add_post'),
    path(route='add_category/', view=AddCategoryView.as_view(), name='add_category'),
    path(route='post/edit/<int:pk>', view=EditPostView.as_view(), name="edit_post"),
    path(route='post/delete/<int:pk>', view=DeletePostView.as_view(), name="delete_post"),
    path(route='category/<str:cats>/', view=category_view, name="category"),
    path(route='category_list/', view=category_list_view, name="category_list"),
    path(route='post/<int:pk>/add_comment/', view=AddCommentView.as_view(), name='add_comment'),
    path(route='help/', view=help, name='help'),
    path(route='contacts/', view=contacts, name='contacts'),
    path(route='favorites/', view=FavoriteListView.as_view(), name='favorite_list'),
    path(route='post/<int:pk>/like/', view=LikePostView.as_view(), name="like_post"),
]
"""
Defines the URL patterns for routing requests to the corresponding views.

Each path() function represents a URL pattern with a specific route, view, and name.
The route is the URL pattern to match.
The view is the corresponding view function or class-based view.
The name is the unique name assigned to the URL pattern for reverse URL lookups.

The `urlpatterns` variable is a list that contains the URL patterns for routing requests to the corresponding views in a Django project. Each element in the list is created using the `path()` function, which takes three arguments: `route`, `view`, and `name`. Here's a breakdown of each path in the provided code:

1. Home page:
   - Route: ''
   - View: HomeView.as_view()
   - Name: 'home'
   - Description: This pattern represents the home page of the website. When the root URL is accessed, it maps to the HomeView class-based view, which is responsible for displaying a list of posts on the home page.

2. Post details:
   - Route: 'post/<int:pk>'
   - View: PostDetailsView.as_view()
   - Name: 'post_details'
   - Description: This pattern handles the display of detailed information about a specific post. It includes a URL parameter <int:pk> to capture the primary key of the post. The view PostDetailsView is responsible for rendering the post details.

3. Add post:
   - Route: 'add_post/'
   - View: AddPostView.as_view()
   - Name: 'add_post'
   - Description: This pattern maps to the AddPostView class-based view, which provides functionality for adding a new post to the website. When this URL is accessed, the corresponding view renders a form for creating a new post.

4. Add category:
   - Route: 'add_category/'
   - View: AddCategoryView.as_view()
   - Name: 'add_category'
   - Description: This pattern corresponds to the AddCategoryView class-based view, allowing users to add new categories to the website. When accessed, the view renders a form for creating a new category.

5. Edit post:
   - Route: 'post/edit/<int:pk>'
   - View: EditPostView.as_view()
   - Name: 'edit_post'
   - Description: This pattern handles the editing of an existing post. It includes a URL parameter <int:pk> to capture the primary key of the post to be edited. The EditPostView class-based view is responsible for rendering the form for editing the post.

6. Delete post:
   - Route: 'post/delete/<int:pk>'
   - View: DeletePostView.as_view()
   - Name: 'delete_post'
   - Description: This pattern allows users to delete a specific post. It includes a URL parameter <int:pk> to capture the primary key of the post to be deleted. The DeletePostView class-based view is responsible for confirming the deletion of the post.

7. Category view:
   - Route: 'category/<str:cats>/'
   - View: category_view
   - Name: 'category'
   - Description: This pattern handles the display of posts belonging to a specific category. It includes a URL parameter <str:cats> to capture the category name. The category_view function-based view is responsible for fetching and rendering the relevant posts.

8. Category list view:
   - Route: 'category_list/'
   - View: category_list_view
   - Name: 'category_list'
   - Description: This pattern maps to the category_list_view function-based view, which displays a list of all available categories on the website.

9. Add comment:
   - Route: 'post/<int:pk>/add_comment/'
   - View: AddCommentView.as_view()
   - Name: 'add_comment'
   - Description: This pattern allows users to add comments to a specific post. It includes a URL parameter <int:pk> to capture the primary key of the post. The AddCommentView class-based view handles the rendering of the comment form and the creation of new comments.

10. Help page:
    - Route: 'help/'
    - View: help
    - Name: 'help'
    - Description: This pattern maps to the help function-based view, which renders the help page of the website, providing assistance or information to the users.

11. Contacts page:
    - Route: 'contacts/'
    - View: contacts
    - Name: 'contacts'
    - Description: This pattern maps to the contacts function-based view, which displays the contacts page. It handles the rendering of a form for users to submit their contact information or queries.

12. Favorite list:
    - Route: 'favorites/'
    - View: FavoriteListView.as_view()
    - Name: 'favorite_list'
    - Description: This pattern corresponds to the FavoriteListView class-based view, which displays a list of posts that the user has marked as favorites. When accessed, the view retrieves the user's favorite posts and renders them.

13. Like post:
    - Route: 'post/<int:pk>/like/'
    - View: LikePostView.as_view()
    - Name: 'like_post'
    - Description: This pattern allows users to like or unlike a specific post. It includes a URL parameter <int:pk> to capture the primary key of the post. The LikePostView class-based view handles the logic for adding or removing likes on the post.

These patterns define the URLs that can be accessed in the Django project, and when a request matches a specific pattern, the corresponding 
view will be executed. The names assigned to each URL pattern can be used for reverse URL lookups, which allow you to dynamically generate 
URLs based on their names in your code.
"""