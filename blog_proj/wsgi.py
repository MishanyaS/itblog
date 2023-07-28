"""
WSGI config for blog_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

"""
This code is the WSGI (Web Server Gateway Interface) configuration for the "blog_proj" project. It prepares the application to be run by a WSGI server. Here's a breakdown of the code:

- `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_proj.settings')`: Sets the `DJANGO_SETTINGS_MODULE` environment variable to specify the project's settings module. In this case, it is set to `'blog_proj.settings'`, indicating that the project's settings are located in the `settings.py` module within the `blog_proj` package.

- `application = get_wsgi_application()`: Retrieves the WSGI application object using the `get_wsgi_application()` function provided by Django's `django.core.wsgi` module. This function loads the WSGI application defined in the project's settings module and returns it. The `application` variable holds a reference to the WSGI application.

Overall, this code sets up the WSGI application for the "blog_proj" project, allowing it to be deployed and run by a WSGI server, such as Gunicorn or uWSGI.
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_proj.settings')
application = get_wsgi_application()
