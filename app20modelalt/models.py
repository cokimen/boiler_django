from django.db import models

# Create your models here.
from uuid import uuid4
from django.db import models


class Property(models.Model):

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    property_address = models.CharField(max_length=128, unique=True)

    host_uuid = models.UUIDField(
        primary_key=False,
        default=uuid4,
        editable=False
    )

    current_certificate_uuid = models.UUIDField(
        primary_key=False,)

    created_at = models.DateField(auto_now_add=True)

    is_active = models.BooleanField()

    property_type = models.CharField(max_length=128)

    description = models.TextField(max_length=256)

    amenities = models.JSONField()

    total_bedrooms = models.PositiveSmallIntegerField()

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=7
    )

    max_guests = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.property_address

    class Meta:
        verbose_name = "property"
        verbose_name_plural = "properties"
