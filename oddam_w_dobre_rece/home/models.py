from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
TYPE = ((1, 'fundacja'),
        (2, 'organizacja pozarządowa'),
        (3, 'zbiórka lokalna'),
        (4, 'domyślna fundacja'))

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE)
    categories = models.ManyToManyField(Category,)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, )
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, help_text="ulica i numer domu")
    phone_number = models.CharField(max_length=16, blank=True, null=True,
                                    validators=[RegexValidator(regex=r"^\+?1?\d{8,15}$")])
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=8, help_text="XX-XXX")
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.institution.name






