from django.db import models
from django.utils import timezone

class CarouselItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel/')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)  # Added field for featured item

class FeaturedItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured/')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    quote = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


