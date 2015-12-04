from django.db import models
from django.utils import timezone
import datetime
import uuid

from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager

@python_2_unicode_compatible
class Paper(models.Model):
    uuid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    author = models.CharField(max_length=100, verbose_name = u"author")
    title = models.CharField(max_length=200, verbose_name = u"title")
    description = models.CharField(max_length=5000)
    breif_description= models.CharField(max_length=500)
    version=models.CharField(max_length=5)
    category=models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    pubdate = models.DateTimeField('date published')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pubdate <= now

    def current_version(self):
        return self.version


class CodeLink(models.Model):
    repolink = models.CharField(max_length=100)
    usage = models.TextField()


