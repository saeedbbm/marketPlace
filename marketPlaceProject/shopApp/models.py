from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique product instances
from django.contrib.auth.models import User
from django.conf import settings
from datetime import date
# Create your models here.


class Category(models.Model):
    """
    Model representing Category (e.g. ...).
    """
    name = models.CharField(max_length=200, help_text="Enter a category name ")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Brand(models.Model):
    """
    Model representing Brand (e.g. ...).
    """
    name = models.CharField(max_length=200, help_text="Enter a brand name ")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Product(models.Model):
    """
    Model representing a product.
    """
    name = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because product can only have one brand, but brand can have multiple products
    # Brand as a string rather than object because it hasn't been declared yet in the file.
    category = models.ManyToManyField(Category, help_text="Select category of this product")
    # ManyToManyField used because product can have many categories. categories can contain many products.
    # Category class has already been defined so we can specify the object above.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular product instance.
        """
        # return reverse('shopApp:product', args=[str(self.id)])
        return reverse('shopApp:product', kwargs={'pk': self.pk})

    def get_add_to_cart_url(self):
        return reverse('shopApp:add-to-cart', args=[str(self.id)])
        # return reverse('shopApp:add-to-cart', kwargs={'pk': self.pk})

    def get_remove_from_cart_url(self):
        return reverse('shopApp:remove_from_cart', args=[str(self.id)])
        # return reverse('shopApp:remove_from_cart', kwargs={'pk': self.pk})

    def display_category(self):
        """
        Creates a string for the Category. This is required to display category in Admin.
        """
        return ', '.join([ category.name for category in self.category.all()[:3] ])

    display_category.short_description = 'Category'


class ProductInstance(models.Model):
    """
    Model representing a specific copy of a product (i.e. that can be bought from a store).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular product across whole store")
    store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=200)
    expiry_date = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # class Meta:
    #     ordering = ["expiry_date"]

    def __str__(self):
        return '%s (%s)' % (self.id,self.product.name)

    # @property
    # def is_overdue(self):
    #     if self.expiry_date and date.today() > self.expiry_date:
    #         return True
    #     return False


class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.item_name}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Store(models.Model):
    """
    Model representing a store.
    """
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(Product, help_text="Select products this store has")
    # ManyToManyField used because store can contain many products. products can exist in many stores.
    # Product class has already been defined so we can specify the object above.

    def __str__(self):
        return self.title


class Supplier(models.Model):
    """
    Model representing a supplier.
    """
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(Product, help_text="Select products this supplier can provide")
    store = models.ManyToManyField(Store, help_text="Select stores this supplier work with")
    # ManyToManyField used because supplier can work with many stores. stores can work with many suppliers.
    # ManyToManyField used because store can contain many products. products can exist in many stores.
    # Product and Supplier classes have already been defined so we can specify the object above.

    def __str__(self):
        return self.name
