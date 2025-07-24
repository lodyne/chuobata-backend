from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseModel(models.Model):
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
    # TODO : Modify the phone field to allow max_length of 15 characters. use phone_number_field package
    # from phone_number_field import PhoneNumberField
    # phone_number = PhoneNumberField(_("user's phone number"), null=True, blank=True)
    # For simplicity, we will use a CharField for now.
    phone_number = models.CharField(_("user's phone number"), max_length=50, null=True, blank=True)
    

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"