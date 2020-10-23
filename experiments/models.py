from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from TRDWLL.signals import create_redirect
from TRDWLL.utils import get_formatted_data
from django.template.loader import render_to_string

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

experiment_status = (
    ('', 'Blank'),
    ('text-gray-500', 'Unmaintained'),
    ('text-green-500', 'Active'),
    ('text-red-500', 'Abandoned')
)

class Experiment(models.Model):
    published_date = models.DateTimeField(help_text='When was this experiment created?')
    title = models.CharField(max_length=100, help_text='Title of the post.')
    description = models.CharField(max_length=500, help_text='The description of the experiment.')
    body = RichTextUploadingField()
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    status = models.CharField(max_length=32, choices=experiment_status, help_text='What\'s the status of this experiment?', default='Blank')
    tech_used = models.CharField(max_length=250, help_text='Tech that was used for this experiment.')
    learned_list = RichTextField(blank=True, help_text='Things that I learned during the development of this experiment?', config_name='experiments_sidebar')
    struggled_list = RichTextField(blank=True, help_text='Things that I struggled with during the development of this experiment?', config_name='experiments_sidebar')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('experiment_post_page', kwargs={'slug': self.slug})

    def get_experiments_formatted():
        """ Get the posts and format them for display """
        queried_experiments = get_formatted_data(Experiment.objects.filter(is_published=True).order_by('-published_date'))

        formatted_experiments = []

        for year,experiments in queried_experiments.items():
            formatted_experiments.append(render_to_string('experiments/extra/list_start.html', {'year': year}))

            for experiment in experiments:
                description = experiment.description[0:117]+'...' if len(experiment.description) > 117 else experiment.description
                formatted_experiments.append(render_to_string('experiments/extra/list_body.html', {'experiment': experiment}))
            
            # end the row
            formatted_experiments.append(render_to_string('experiments/extra/list_end.html', {}))

        return ''.join(formatted_experiments)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'experiment_entry'
        ordering = ['-published_date']
        verbose_name = 'Experiment'
        verbose_name_plural = 'Experiments'


pre_save.connect(create_redirect, sender=Experiment)