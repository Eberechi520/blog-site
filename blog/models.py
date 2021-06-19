from django.db import models

from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
        )

    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to = 'blog/', blank=True, null=True)
    excerpt = models.TextField(max_length=500)
    body = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='draft')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("post_detail", args=[

                self.date_created.year,
                self.date_created.month,
                self.date_created.day,
                self.slug
            ]
        )

class Comment(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.comment} for {self.blog.title}'
    