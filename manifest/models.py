from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from account.models import CustomUser
from datetime import timedelta
from django.db.models.signals import pre_save
from django.dispatch import receiver
import itertools


# The Manifestation model
class Manifestation(models.Model):
    STYLE_CHOICES = [
        ("moon", "Moon"),
        ("neutral", "Neutral"),
        ("nature", "Nature"),
        ("sun", "Sun"),
        ("stars", "Stars"),
        ("cosmic", "Cosmic"),
        ("witchy", "Witchy"),
        ("hearts", "Hearts"),
        ("antique", "Antique"),
        ("pastel", "Pastel"),
    ]

    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    style_choice = models.CharField(max_length=10, choices=STYLE_CHOICES)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_charged = models.DateTimeField(null=True, blank=True)
    is_charged = models.BooleanField(default=False)
    can_charge = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

#  checks if the manifestation is charged and if it can be charged
    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.last_charged:
            if now >= self.last_charged + timedelta(hours=24):
                self.is_charged = False
            else:
                self.is_charged = True
            if now >= self.last_charged + timedelta(hours=12):
                self.can_charge = True
            else:
                self.can_charge = False
        else:
            self.can_charge = True
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            for i in itertools.count(1):
                if not Manifestation.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{original_slug}-{i}"
        super().save(*args, **kwargs)

#  returns the time when the manifestation can be charged next
    def next_charge_time(self):
        if self.last_charged is None:
            return None
        return self.last_charged + timedelta(hours=12)

    def __str__(self):
        return self.title


# creates unique slugs for each manifestation
@receiver(pre_save, sender=Manifestation)
def set_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        counter = 1
        while Manifestation.objects.filter(slug=instance.slug).exists():
            instance.slug = f"{slugify(instance.title)}-{counter}"
            counter += 1
