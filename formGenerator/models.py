from pyexpat import model
from django.db import models
from random import randint
import shortuuid


def GenerateRandom():
    return randint(352452,75566263)

def GenerateUiid():
    return shortuuid.uuid()
# Create your models here.

class MainForm(models.Model):
    Name = models.CharField(max_length=500)
    InviteKey = models.TextField(default=GenerateUiid())
    def __str__(self) -> str:
        return self.Name

class Forms(models.Model):
    formParent = models.ForeignKey(MainForm, on_delete=models.SET_NULL, null=True)
    label = models.CharField(max_length=50)
    formtype = models.CharField(max_length=30)
    formName = models.CharField(max_length=50,default='')
    parentID = models.CharField(max_length=500,default=GenerateRandom())
    required = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.formName
    # def save(self)


class FormStore(models.Model):
    form = models.ForeignKey(MainForm, on_delete=models.SET_NULL, null=True)
    fieldName = models.CharField(max_length=500)
    fieldData = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.fieldName

