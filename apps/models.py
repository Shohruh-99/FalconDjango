from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, IntegerField, TextField, \
    ForeignKey, CASCADE, DateTimeField, SlugField, FloatField
from django.utils.text import slugify


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)


class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'Categories'

    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = CharField(max_length=100)
    price = FloatField()
    description = TextField()
    quantity = IntegerField()
    shipping_cost = FloatField()
    discount = IntegerField()
    category = ForeignKey('Category', on_delete=CASCADE, related_name='products')

    @property
    def discount_price(self):
        return self.price * (1-self.discount/100)

    def __str__(self):
        return self.name


class Specification(Model):
    key = CharField(max_length=100)
    value = CharField(max_length=255)
    product = ForeignKey('Product', on_delete=CASCADE, related_name='specifications')

    def __str__(self):
        return self.key


class ProductImage(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('Product', on_delete=CASCADE, related_name='images')

class User(AbstractUser):
    phone_number = CharField(max_length=13, null=True)
    image = ImageField(upload_to='users/', null= True)

