# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Tag(models.Model):
        name = models.CharField(u'名称', max_length = 20)
        def __str__(self):
                return self.name;

class Category(models.Model):
        name = models.CharField(u'名称', max_length = 20)
        def __str__(self):
                return self.name;
class Articles(models.Model):
        title = models.CharField(u'标题',max_length = 150)
        content = models.TextField(u'正文', blank=True, null=True)
        date_time = models.DateTimeField(u'发布时间', auto_now_add = True)
        category = models.ForeignKey(Category, verbose_name=u'分类', on_delete=models.CASCADE)
        tags = models.ManyToManyField(Tag, verbose_name = u'标签', blank=True)
        # models.ForeignKey表示一个Article有一个Category
        # models.ManyToManyField表示一个Article有多个Tag，blank=True表示可以为空
        def __str__(self):
                return self.title
        class Meta:     #Descending by time
                ordering = ['-date_time']

