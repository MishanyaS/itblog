"""
ASGI config for blog_proj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

"""
This code is the standard entry point for running a Django application using ASGI (Asynchronous Server Gateway Interface). Here's a breakdown of the code:

- `import os`: Imports the `os` module, which provides a way to interact with the operating system.

- `from django.core.asgi import get_asgi_application`: Imports the `get_asgi_application` function from `django.core.asgi` module. This function returns the ASGI application object for the Django project.

- `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_proj.settings')`: Sets the default value for the `'DJANGO_SETTINGS_MODULE'` environment variable to `'blog_proj.settings'`. This specifies the settings module for the Django project.

- `application = get_asgi_application()`: Retrieves the ASGI application object for the Django project using the `get_asgi_application` function and assigns it to the `application` variable. This object represents the Django application and can be used to run the project using an ASGI server.

Overall, this code sets up the necessary environment and retrieves the ASGI application object to run the Django project using ASGI.
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_proj.settings')
application = get_asgi_application()
