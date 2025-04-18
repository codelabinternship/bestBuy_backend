from django.db import models
from django.utils import timezone









class RoleChoices(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    CUSTOMER = 'Customer', 'Customer'
    EMPLOYEE = 'Employee', 'Employee'

class TransactionTypeChoices(models.TextChoices):
    ACCRUAL = 'accrual', 'Accrual'
    DEDUCTION = 'deduction', 'Deduction'

class DiscountTypeChoices(models.TextChoices):
    PERCENTAGE = 'percentage', 'Percentage'
    FIXED = 'fixed', 'Fixed'









class ChannelPosts(models.Model):
    post_id = models.AutoField(primary_key=True)  # ���������� ������������� �����
    content = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Post #{self.post_id} - {'Active' if self.status else 'Inactive'}"








class LoyaltyProgram(models.Model):
    loyalty_id = models.AutoField(primary_key=True)  # ������������� ID
    user_id = models.IntegerField()
    points_balance = models.IntegerField()
    transaction_type = models.CharField(
        max_length=10,
        choices=TransactionTypeChoices.choices
    )
    points_changed = models.IntegerField()
    transaction_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"Loyalty #{self.loyalty_id} - User {self.user_id} - {self.transaction_type}"










class UserActivityLogs(models.Model):
    log_id = models.AutoField(primary_key=True)  # �������������� ID
    user_id = models.IntegerField()
    activity_type = models.CharField(max_length=255)
    activity_details = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Log #{self.log_id} for User {self.user_id} - {self.activity_type}"






class DeliveryMethods(models.Model):
    delivery_method_id = models.AutoField(primary_key=True)  # ���������� ID
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {'Active' if self.status else 'Inactive'}"



class Promocodes(models.Model):
    promocode_id = models.AutoField(primary_key=True)  # ���������� ID
    code = models.CharField(max_length=100, unique=True)
    discount_type = models.CharField(
        max_length=10,
        choices=DiscountTypeChoices.choices
    )
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    usage_limit = models.IntegerField()
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({self.discount_type})"







class Branches(models.Model):
    branch_id = models.AutoField(primary_key=True)  # ���������� �������������
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=555)
    phone = models.CharField(max_length=50)
    working_hours = models.CharField(max_length=255)
    description = models.TextField()
    geo_location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.address}"






class PaymentMethods(models.Model):
    payment_method_id = models.AutoField(primary_key=True)  # ���������� �������������
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {'Active' if self.status else 'Inactive'}"


class Variations(models.Model):
    variation_id = models.AutoField(primary_key=True)  # ���������� ID ��������
    product_id = models.IntegerField()
    option_name = models.CharField(max_length=255)
    option_value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.option_name}: {self.option_value} (Product {self.product_id})"





class BotConfiguration(models.Model):
    bot_id = models.AutoField(primary_key=True)  # ���������� ID ����
    bot_token = models.CharField(max_length=255)
    bot_name = models.CharField(max_length=255)
    settings = models.JSONField()  # ������ ��������� � ������� JSON
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.bot_name} - {'Active' if self.status else 'Inactive'}"





class SMSCampaigns(models.Model):
    campaign_id = models.AutoField(primary_key=True)  # ���������� ID ��������
    name = models.CharField(max_length=255)
    message = models.TextField()
    scheduled_time = models.DateTimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {'Scheduled' if self.status else 'Inactive'}"




class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)  # ���������� ID ������
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review {self.review_id} - Product {self.product_id} - User {self.user_id}"



class ExportHistory(models.Model):
    export_id = models.AutoField(primary_key=True)  # ���������� ID ��������
    file_name = models.CharField(max_length=255)
    export_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return f"{self.file_name} ({self.status})"



#�������� ������:


class User(models.Model):
    user_name = models.CharField(max_length=250)
    user_id = models.IntegerField(unique=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.CUSTOMER
    )
    address = models.CharField(max_length=300)
    password = models.TextField(max_length=15)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_status = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_method_id = models.IntegerField()
    payment_method_id = models.IntegerField()
    branch_id = models.IntegerField()

    def __str__(self):
        return f"Order #{self.id} by {self.user.user_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_time = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order #{self.order.id}"


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name='products')
    brand = models.CharField(max_length=255)
    media_url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=500)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name








# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     image_url = models.CharField(max_length=500, blank=True, null=True)
#     status = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     stock_quantity = models.IntegerField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     brand = models.CharField(max_length=255, blank=True, null=True)
#     media_url = models.CharField(max_length=500, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name







def category_image_upload_path(instance, filename):
    return f'categories/{instance.name}/{filename}'

def product_media_upload_path(instance, filename):
    return f'products/{instance.name}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=category_image_upload_path, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.CharField(max_length=255, blank=True, null=True)
    media = models.ImageField(upload_to=product_media_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
