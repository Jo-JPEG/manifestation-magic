from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from account.models import CustomUser
from datetime import timedelta

class Manifestation(models.Model):
    STYLE_CHOICES = [
        ('moon', 'Moon'),
        ('neutral', 'Neutral'),
        ('nature', 'Nature'),
        ('sun', 'Sun'),
        ('stars', 'Stars'),
        ('cosmic', 'Cosmic'),
        ('witchy', 'Witchy'),
        ('hearts', 'Hearts'),
        ('antique', 'Antique'),
        ('pastel', 'Pastel'),
    ]

    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    style_choice = models.CharField(max_length=10, choices=STYLE_CHOICES)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_charged = models.DateTimeField(null=True, blank=True)
    is_charged = models.BooleanField(default=False)
    can_charge = models.BooleanField(default=True)  # New field
    is_public = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            while Manifestation.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{counter}"
                counter += 1
        if self.last_charged and timezone.now() >= self.last_charged + timedelta(minutes=1):
            self.can_charge = True
        else:
            self.can_charge = not self.is_charged
        super().save(*args, **kwargs)

    def next_charge_time(self):
        # Assuming the recharge period is 24 hours
        return self.last_charged + timedelta(minutes=1)

    def __str__(self):
        return self.title

