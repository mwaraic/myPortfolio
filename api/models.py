from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import User
# Create your models here.

class Test(models.Model):
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resume=RichTextUploadingField()