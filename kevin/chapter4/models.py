import datetime

from django.contrib.auth.models import User
from django.db import models

from tagging.fields import TagField
from markdown import markdown

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	slug = models.SlugField(help_text="Suggested value automatically generated from title. Must be unique.")
	description = models.TextField()

	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories22"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/categories/%s/" % self.slug

class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    # Core fields.
    title = models.CharField(max_length=250,
                             help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True,
                               help_text="A short summary of the entry. Optional.")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Fields to store generated HTML.
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text="Suggested value automatically generated from title. Must be unique for the publication date.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
                                 help_text="Only entries with live status will be publicly displayed.")

    # Categorization.
    categories = models.ManyToManyField(Category)
    tags = TagField(help_text="Separate tags with spaces.")

    objects = models.Manager()
    live = LiveEntryManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return ('coltrane_entry_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                               'month': self.pub_date.strftime("%b").lower(),
                                               'day': self.pub_date.strftime("%d"),
                                               'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

