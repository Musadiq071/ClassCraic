from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content  = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	auhtor = models.ForeignKey(User, on_delete=models.CASCADE )
	attachment = models.FileField(
        upload_to='post_files/', 
        blank=True, 
        null=True,)
	likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

	def total_likes(self):
		return self.likes.count() 

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    auhtor = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
    	ordering = ['-date_posted']
    def __str__(self):
        return f"{self.auhtor.username} - {self.content[:20]}"