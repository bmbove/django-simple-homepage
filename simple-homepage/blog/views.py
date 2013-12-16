from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from blog.models import Post


class PostDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        if not kwargs['slug']:
            return redirect('/blog')
        else:
            slug = kwargs['slug']

        try:
            post = Post.objects.get(slug=slug, published=True)
        except:
            return redirect('/blog')

        template_name = 'blog/post.html'
        context = {'post': post}
        return render(request, template_name, context)


class BlogListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-created_at')
