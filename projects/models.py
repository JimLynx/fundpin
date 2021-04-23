from django.db import models
from richtext.fields import RichTextField


class Category(models.Model):

    class Meta:
        # adjust verbose name from the Django defaults
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        string method to return category name 
        """
        return self.name

    def get_friendly_name(self):
        """
        string method to return category friendly name 
        """
        return self.friendly_name


class Country(models.Model):
    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        string method to return category name 
        """
        return self.name

    def get_friendly_name(self):
        """
        string method to return category friendly name 
        """
        return self.friendly_name


class Project(models.Model):
    pin_id = models.CharField(max_length=20, null=True, blank=False, unique=True)
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(
        'Country', null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = RichTextField(blank=False, null=True)
    needs = RichTextField(blank=False, null=True)
    longitude = models.FloatField(max_length=20, null=True)
    latitude = models.FloatField(max_length=20, null=True)
    is_featured = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        string method to return category name 
        """
        return self.name