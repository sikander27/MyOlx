from django.db import models
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    spec_options = models.JSONField(
        "Spec Options", encoder=DjangoJSONEncoder, default=dict, null=True, blank=True
    )
    # Add other category-related fields as needed

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Spec(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    spec_dump = models.JSONField(
        "Spec dump", encoder=DjangoJSONEncoder, default=dict
    )
    # Add other category-related fields as needed

    class Meta:
        abstract = True
        # verbose_name_plural = "Specs"

    # def __str__(self):
    #     return self.category


class Ad(Spec):
    user = models.ForeignKey(User, related_name='user_ads', on_delete=models.CASCADE)
    # specs = models.OneToOneField(Spec, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=150)
    price = models.FloatField('Price', default=0)
    description = models.TextField('Description', null=True, blank=True)
    sold = models.BooleanField('Sold', default=False)
    

    class Meta:
        verbose_name_plural = "Ads"

    def __str__(self):
        return self.title


class Photo(BaseModel):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    url = models.URLField(max_length=200) 
    alt_name = models.CharField("Alt name", max_length=150, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.url


# class Categories(models.Model):
#     category_name = models.CharField(max_length=100)
#     # Add other category-related fields as needed

#     class Meta:
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return self.category_name


# class Attributes(models.Model):
#     attr_name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name_plural = "Attributes"

#     def __str__(self):
#         return self.attr_name


# class Options(models.Model):
#     option_name = models.CharField(max_length=100)
#     category = models.ForeignKey(Categories, on_delete=models.CASCADE)
#     attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)
#     # Add other option-related fields as needed

#     class Meta:
#         verbose_name_plural = "Options"

#     def __str__(self):
#         return f"{self.option_name} - {self.category} - {self.attributes}"


# class Categories(models.Model):
#     category_name = models.CharField(max_length=100)
#     # Add other category-related fields as needed

#     class Meta:
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return self.category_name


# class Options(models.Model):
#     option_name = models.CharField(max_length=100)
#     category = models.ManyToManyField(Categories)
#     # Add other option-related fields as needed

#     class Meta:
#         verbose_name_plural = "Options"

#     def __str__(self):
#         return self.option_name


# class Attributes(models.Model):
#     attr_name = models.CharField(max_length=100)
#     Options = models.ManyToManyField(Options)

#     class Meta:
#         verbose_name_plural = "Attributes"

#     def __str__(self):
#         return self.attr_name
