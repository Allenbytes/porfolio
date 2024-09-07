# projects/models.py
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    date_posted = models.DateTimeField(auto_now_add=True)
    project_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inquiry from {self.full_name} - {self.subject}'

    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"