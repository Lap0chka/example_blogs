from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    objects = models.Manager() # менеджер, применяемый по умолчанию
    published = PublishedManager() # конкретно-прикладной менеджер

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    pictures = models.ImageField(upload_to=f'post/{author}/', null=True, blank=True)

    def user_directory_path(instance, filename):
        # Добавляем к пути имя пользователя
        return 'post/user_{0}/{1}'.format(instance.author, filename)

    pictures.upload_to = user_directory_path
    tags = TaggableManager()
    view = models.PositiveIntegerField(default=114)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self): return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year, self.publish.month,self.publish.day, self.slug])

    def post_change_url(self):
        return reverse('profile:post_edit',args=[self.publish.year, self.publish.month,self.publish.day, self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']),]

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'

