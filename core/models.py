from django.db import models
from users.models import User
from django.db.models import Q 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

COLOR_CHOICES = {
    ('LightSkyBlue', 'LightSkyBlue'),
    ('PaleGreen', 'PaleGreen'),
    ('Lavender', 'Lavender'),
    ('LightSalmon', 'LightSalmon'),
}

FONT_CHOICES = {
    ('Perpetua', 'Perpetua'),
    ('Copperplate', 'Copperplate'),
    ('Cambria', 'Cambria'),
    ('Arial', 'Arial'),
    ('Verdana', 'Verdana'),
}

BORDER_CHOICES = {
    ('NoBorder', 'NoBorder'),
    ('DottedBorder', 'DottedBorder'),
    ('DashedBorder', 'DashedBorder'),
    ('SolidBorder', 'SolidBorder'),
}


# Create your models here.

class Card(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cards', null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(max_length=500, blank=True, null=True, help_text="Type a greeting here")
    date_field = models.DateTimeField(auto_now_add=True)
    background_color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='')
    border = models.CharField(max_length=20, choices=BORDER_CHOICES, default='')
    font = models.CharField(max_length=20, choices=FONT_CHOICES, default='')
    image = models.ImageField(default='default.jpg', upload_to="card_images")

    # def __str__(self):
    #     return self.user


def get_available_cards_for_user(queryset, user):
    if user.is_authenticated:
        cards = queryset.filter(Q(user=user))
    else:
        cards = None
    return cards 