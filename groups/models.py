from django.db import models
from django.utils.text import slugify #remove any characters that are not alphanuermica, /'s, or -'s
from django.core.urlresolvers import reverse

# Create your models here.

import misaka #link embedding, install using pip install misaka

from django.contrib.auth import get_user_model
User=get_user_model()

from django import template
register=template.Library()

class Group(models.Model):
    name=models.CharField(max_length = 256, unique=True)
    slug=models.SlugField(allow_unicode=True, unique=True)
    description=models.TextField(blank=False, default='') #when blank False, it CANNOT be blank
    description_html=models.TextField(editable=False, default='', blank=True)
    members=models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering=['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')
