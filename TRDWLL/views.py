from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View, ListView

from blog.models import Post
from .models import About

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        # post = Post.objects.filter(is_published=True).order_by('-published_date')[0]

        # return redirect('blog_post_page', slug=post.slug)

        return render(request, self.template_name)


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        text = About.objects.all().first()

        return render(request, self.template_name, {'about_text': text})