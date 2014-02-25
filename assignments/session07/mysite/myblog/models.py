from django.db import models
from django.contrib.auth.models import User

# STATUS_CHOICES = (
#     ('d', 'Draft'),
#     ('p', 'Published'),
# )

class Post(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField(blank=True)
	author = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(blank=True, null=True)
	# I'm sorting out some errors before doing second submission.
	#status = models.CharField(max_length=1, choices=STATUS_CHOICES)

	def __unicode__(self):
		return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, null=True,
                                   related_name='categories')

    def __unicode__(self):
        return self.name

    class Meta():
    	verbose_name_plural = 'Categories'

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3)
#     created_date = models.DateTimeField(auto_now_add=True)
#     def __unicode__(self):
#     	return self.name
