from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.template.loader import render_to_string

from TRDWLL.signals import create_redirect
from TRDWLL.utils import get_formatted_data

from ckeditor_uploader.fields import RichTextUploadingField

import operator

class Category(models.Model):
    title = models.CharField(max_length=100, help_text='Title of the category.')
    description = models.CharField(max_length=200, blank=True, help_text='A short description for the category.')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_category_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_posts_formatted(slug):
        """ Get the posts and format them for display """
        queried_posts = get_formatted_data(Post.objects.filter(is_published=True, category=Category.objects.filter(slug__iexact=slug).first()).order_by('-published_date'))
        
        formatted_posts = []

        for i, (year,posts) in enumerate(queried_posts.items()):
            formatted_posts.append(render_to_string('blog/extra/post-home/post_start.html', {'year': year, 'index': i}))

            for count, post in enumerate(posts, 1):
                formatted_posts.append(render_to_string('blog/extra/post-home/post_body.html', {'post': post, 'index': count}))
            
            formatted_posts.append('</ul>')
        return ''.join(formatted_posts)
        #     formatted_posts.append()

        #     for post in posts:
        #         formatted_posts.append('<li><span class="post-date archive-date">'+str(post.published_date.strftime('%b %d'))+'</span><a href="'+post.get_absolute_url()+'" class="archive-title">'+post.title+'</a></li>')
        #     formatted_posts.append('</ul>')
        
        # return ''.join(formatted_posts)

    class Meta:
        db_table = 'blog_category'
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    published_date = models.DateTimeField()
    title = models.CharField(max_length=200, help_text='Title of the post.')
    body = RichTextUploadingField()
    description = models.CharField(max_length=100, help_text='A short tagline that describes what the reader will be reading about.')
    category = models.ManyToManyField(Category, help_text='The category that the post will be listed under.')
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_post_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_categories_formatted_sidebar():
        """ Get the categories and format them for display on the sidebar """
        categories = []
        cats = {}

        # sort through all categories and add them to a dictionary
        for tmp in Category.objects.all():
            count = tmp.post_set.filter(is_published=True).count()
            if count >= 1:
                cats.update({tmp:count})

        # sort the dictionary by value
        cats = dict(sorted(cats.items(), key=operator.itemgetter(1),reverse=True))

        # create the html format for the sidebar
        categories.append(render_to_string('blog/extra/sidebar/categories_start.html', {}))
        for k,v in cats.items():
            categories.append(render_to_string('blog/extra/sidebar/categories_body.html', {'category': k, 'category_count': v}))
        categories.append(render_to_string('blog/extra/sidebar/categories_end.html', {}))

        return ''.join(categories)

    def get_categories_formatted_post(self):
        """ Get the categories and format them for display """
        categories = [] 

        for tmp in self.category.all():
            categories.append(render_to_string('blog/extra/post-home/categories_list.html', {'category': tmp}))

        categories.sort() # sort the categories to be alphabetical order
        return ''.join(categories)

    def get_posts_formatted():
        """ Get the posts and format them for display """
        queried_posts = get_formatted_data(Post.objects.filter(is_published=True).order_by('-published_date'))

        formatted_posts = []

        for i, (year,posts) in enumerate(queried_posts.items()):
            formatted_posts.append(render_to_string('blog/extra/post-home/post_start.html', {'year': year, 'index': i}))

            for count, post in enumerate(posts, 1):
                formatted_posts.append(render_to_string('blog/extra/post-home/post_body.html', {'post': post, 'index': count}))
            
            formatted_posts.append('</ul>')
        return ''.join(formatted_posts)

    def categories(self):
        return ", ".join([str(p.title) for p in self.category.all()])

    class Meta:
        db_table = 'blog_post'
        ordering = ['-published_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


pre_save.connect(create_redirect, sender=Post)
pre_save.connect(create_redirect, sender=Category)