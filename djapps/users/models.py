from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class CustomUser(AbstractUser, BaseModel):
    """Custom user model that extends AbstractUser and BaseModel.

    Args:
        AbstractUser (_type_): Django's built-in user model.
        BaseModel (_type_): A base model that includes created_at and updated_at fields.

    Returns:
        _type_: A custom user model with additional fields.
    """
    
    phone_number = PhoneNumberField(_("user's phone number"), null=True, blank=True)

    
    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"