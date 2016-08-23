from django.db import models
from enumfields import EnumIntegerField
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport


# Create your models here.


class GenderEnum(Enum):
    MALE = 1
    FEMALE = 2

    class Labels:
        MALE = 'Male'
        FEMALE = 'Female'


class Breed(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class CatColor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cat(models.Model):
    breed = models.ForeignKey(Breed)
    sex = EnumIntegerField(GenderEnum)
    cat_color = models.ForeignKey(CatColor)
    date = models.DateField()
    desc = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='cats')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.id