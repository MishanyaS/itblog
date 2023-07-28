from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from . models import Post, Category, Comment, Favorite
from . forms import PostForm, EditPostForm, CommentForm, CategoryForm
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

# Create your views here.



class HomeView(ListView):
    """
    Represents the home page view that displays a list of posts.
    
    Inherits from ListView.

    Attributes:
        model (Post): The model class associated with the view.
        template_name (str): The name of the template used to render the view.
        ordering (list): The ordering of the posts.
        paginate_by (int): The number of posts to display per page.
        
    Methods:
        get_context_data(): Returns the context data for rendering the home page view.
        get_queryset(): Returns the queryset for the home page view.
    """
    model=Post
    template_name="home.html"
    ordering=['-post_date']
    paginate_by = 10
    
    def get_context_data(self, *args, **kwargs):
        """
        Retrieves the context data for rendering the home page view.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data.
        """
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        return context
    
    def get_queryset(self):
        """
        Retrieves the queryset for the home page view.

        Returns:
            QuerySet: The queryset for the home page view.
        """
        query = self.request.GET.get('q')
        if query:
            return self.model.objects.filter(post_title__icontains=query)
        else:
            return super().get_queryset()

def category_list_view(request):
    """
    View function for displaying a list of categories.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered template with the list of categories.
    """
    cat_menu_list = Category.objects.all()
    return render(request, 'categories/category_list.html', {'cat_menu_list':cat_menu_list})

def category_view(request, cats):
    """
    View function for displaying posts belonging to a specific category.

    Args:
        request (HttpRequest): The HTTP request object.
        cats (str): The category name as a string.

    Returns:
        HttpResponse: The HTTP response containing the rendered template with the category posts.
    """
    category_posts = Post.objects.filter(post_category=cats.replace('-', ' '))
    
    paginator = Paginator(category_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    cat_menu = Category.objects.all()
    
    return render(request, 'categories/categories.html', {'cats':cats.capitalize().replace('-', ' '), 'category_posts':category_posts, 'page_obj': page_obj, 'cat_menu':cat_menu})
    
class PostDetailsView(HitCountDetailView):
    """
    Represents a view for displaying detailed information about a post.
    
    Inherits from HitCountDetailView.

    Attributes:
        model (Post): The model class associated with the view.
        template_name (str): The name of the template used to render the view.
        count_hit (bool): Flag indicating whether to count the hit for the post.
        
    Methods:
        post(): Returns the HTTP POST request for saving or deleting favorites on a post.
        get_context_data(): Returns the context data for rendering the post details view.
    """
    model=Post
    template_name="posts/post_details.html"
    count_hit=True
    
    def post(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request for saving or deleting favorites on a post.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response.
        """
        post = self.get_object()
        user = request.user

        if user.is_authenticated:
            favorite, created = Favorite.objects.get_or_create(post=post, user=user)

            if created:
                pass
            else:
                favorite.delete()
                
        post.save()

        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        """
        Retrieves the context data for rendering the post details view.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data.
        """
        cat_menu = Category.objects.all()
        context = super(PostDetailsView, self).get_context_data(*args, **kwargs)
        
        post = self.get_object()
        comments_count = Comment.objects.filter(post=post).count()
        
        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        context["cat_menu"] = cat_menu
        context["comments_count"] = comments_count
        
        context["total_likes"] = total_likes
        return context
    
class LikePostView(View):
    """
    View class for handling the liking of a post.
    
    Inherits from View.

    Methods:
        post(request, *args, **kwargs): Handles the HTTP POST request for liking or unliking a post.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request for liking or unliking a post.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponseRedirect: The HTTP redirect response to the post details page.
        """
        post = Post.objects.get(pk=self.kwargs['pk'])
        user = request.user

        if user.is_authenticated:
            if 'like' in request.POST:
                if user in post.likes.all():
                    post.likes.remove(user)
                else:
                    post.likes.add(user)


        return redirect('post_details', pk=post.pk)
    
class AddPostView(CreateView):
    """
    Represents a view for adding a new post.
    
    Inherits from CreateView.

    Attributes:
        model (Post): The model class associated with the view.
        form_class (Form): The form class used for creating a new post.
        template_name (str): The name of the template used to render the view.
    """
    model=Post
    form_class=PostForm
    template_name="posts/add_post.html"
    
class AddCommentView(CreateView):
    """
    Represents a view for adding a new comment.
    
    Inherits from CreateView.

    Attributes:
        model (Comment): The model class associated with the view.
        form_class (Form): The form class used for creating a new comment.
        template_name (str): The name of the template used to render the view.
        success_url (str): The URL to redirect to after a successful form submission.
        
    Methods:
        form_valid(): Returns The HTTP response when the form is valid.
    """
    model=Comment
    form_class=CommentForm
    template_name="comments/add_comment.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        """
        Called when the form is valid and ready to be processed.

        Args:
            form (Form): The validated form.

        Returns:
            HttpResponse: The HTTP response.
        """
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
class AddCategoryView(CreateView):
    """
    Represents a view for adding a new category.
    
    Inherits from CreateView.

    Attributes:
        model (Category): The model class associated with the view.
        form_class (Form): The form class used for creating a new category.
        template_name (str): The name of the template used to render the view.
    """
    model=Category
    form_class=CategoryForm
    template_name="categories/add_category.html"
    
class EditPostView(UpdateView):
    """
    Represents a view for editing an existing post.
    
    Inherits from UpdateView.

    Attributes:
        model (Post): The model class associated with the view.
        form_class (Form): The form class used for editing the post.
        template_name (str): The name of the template used to render the view.
    """
    model=Post
    form_class=EditPostForm
    template_name="posts/edit_post.html"
    
class DeletePostView(DeleteView):
    """
    Represents a view for deleting an existing post.
    
    Inherits from DeleteView.

    Attributes:
        model (Post): The model class associated with the view.
        template_name (str): The name of the template used to render the view.
        success_url (str): The URL to redirect to after a successful deletion.
    """
    model=Post
    template_name="posts/delete_post.html"
    success_url = reverse_lazy("home")
    
def help(request):
    """
    View function for rendering the help page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered help page.
    """
    return render(request, 'help/help.html', {})

def contacts(request):
    """
    View function for handling contact form submission and rendering the contacts page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered contacts page or a success page upon form submission.
    """
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = email
            recipient_list = [settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'contacts/success.html')
    else:
        form = EmailForm()

    return render(request, 'contacts/contacts.html', {'form': form})

class FavoriteListView(LoginRequiredMixin, ListView):
    """
    Represents a view for displaying a list of favorite items.
    
    Inherits from LoginRequiredMixin, ListView.

    Attributes:
        model (Favorite): The model class associated with the view.
        template_name (str): The name of the template used to render the view.
        context_object_name (str): The name of the variable used to pass the list of favorite items to the template.
        paginate_by (int): The number of items to display per page.
    """
    model = Favorite
    template_name = "favorite/favorite_list.html"
    context_object_name = "favorites"
    paginate_by = 10

    def get_queryset(self):
        """
        Returns the queryset of favorite items for the currently logged-in user.

        Returns:
            QuerySet: The queryset of favorite items.
        """
        return Favorite.objects.filter(user=self.request.user).select_related("post").order_by("-pk")

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