"""blog_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from blog_app.views import set_language



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),    
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
Defines the URL patterns for routing requests to the corresponding views.

Each path() function represents a URL pattern with a specific route, view, and name.
The route is the URL pattern to match.
The view is the corresponding view function or class-based view.
The name is the unique name assigned to the URL pattern for reverse URL lookups.

The `urlpatterns` variable is a list that contains the URL patterns for routing requests to the corresponding views in a Django project. Each element in the list is created using the `path()` function, which takes three arguments: `route`, `view`, and `name`. Here's a breakdown of each path in the provided code:

1. Admin:
   - Route: 'admin/'
   - View: include('blog_app.urls')
   - Name: -
   - Description: This path is used for the Django admin interface. It maps the URL 'admin/' to the built-in Django admin URLs provided by admin.site.urls. It allows authorized users to access and manage the administration area of the website.

2. Blog app URLs:
   - Route: ''
   - View: include('blog_app.urls')
   - Name: -
   - Description: This path includes the URLs defined in the 'blog_app.urls' module. It allows for routing to specific paths within the blog app, which may include features such as blog posts, categories, or post details.

3. User authentication URLs:
   - Route: 'users/'
   - View: include('django.contrib.auth.urls')
   - Name: -
   - Description: This path includes the built-in Django authentication URLs provided by django.contrib.auth.urls. It allows for user authentication-related functionality, such as login, logout, password reset, etc.

4. User-specific URLs:
   - Route: 'users'
   - View: include('users.urls')
   - Name: -
   - Description: This path includes the URLs defined in the 'users.urls' module. It allows for routing to user-specific paths, which may include user profiles, account settings, or other user-related features.
   
5. Media files serving:
   - Route: static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   - View: None (static files serving)
   - Name: -
   - Description: This path is used for serving media files during development. It enables the web server to serve files from the 'MEDIA_ROOT' directory when their URLs match the 'MEDIA_URL' specified in the Django settings.

These patterns define the URLs that can be accessed in the Django project, and when a request matches a specific pattern, the corresponding 
view will be executed. The names assigned to each URL pattern can be used for reverse URL lookups, which allow you to dynamically generate 
URLs based on their names in your code.
"""

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
     path("set_language/<str:language>", set_language, name="set_language"),
]
"""
Defines the URL patterns for routing requests to the corresponding views.

Each path() function represents a URL pattern with a specific route, view, and name.
The route is the URL pattern to match.
The view is the corresponding view function or class-based view.
The name is the unique name assigned to the URL pattern for reverse URL lookups.

The `urlpatterns` variable is a list that contains the URL patterns for routing requests to the corresponding views in a Django project. Each element in the list is created using the `path()` function, which takes three arguments: `route`, `view`, and `name`. Here's a breakdown of each path in the provided code:

1. Internationalization patterns:
   - Route: (Dynamic based on language prefix)
   - View: (Dynamic based on language prefix)
   - Name: -
   - Description: This pattern utilizes the i18n_patterns() function to enable internationalization for the URLs defined in the urlpatterns list passed as an argument. The language prefix is dynamically added to the URLs based on the user's selected language. The prefix_default_language=False parameter ensures that the default language code is not included in the URL prefixes.

2. Language switching:
   - Route: 'set_language/str:language'
   - View: set_language
   - Name: 'set_language'

These patterns define the URLs that can be accessed in the Django project, and when a request matches a specific pattern, the corresponding 
view will be executed. The names assigned to each URL pattern can be used for reverse URL lookups, which allow you to dynamically generate 
URLs based on their names in your code.
"""
