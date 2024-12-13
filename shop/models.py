from django.db import models
from django.db.models import Avg
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class OrderStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name="Статус заказа")  

    def __str__(self):
        return self.status

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=100, verbose_name="Способ оплаты")  

    def __str__(self):
        return self.payment_method

class UserManager(BaseUserManager):
    def create_user(self, user_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user = self.model(user_name=user_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(user_name, email, password, **extra_fields)


class Role(models.Model):
    role_name = models.CharField(max_length=100, verbose_name="Роль") 

    def __str__(self):
        return self.role_name


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=100, unique=True, verbose_name="Имя пользователя")  
    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронная почта")  
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Роль")  
    is_active = models.BooleanField(default=True, verbose_name="Активен")  
    is_staff = models.BooleanField(default=False, verbose_name="Сотрудник")  
    date_joined = models.DateTimeField(default=now, verbose_name="Дата регистрации") 

    objects = UserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.user_name

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.cat_name



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара") 
    description = models.TextField(verbose_name="Описание товара") 
    cost = models.IntegerField(verbose_name="Цена")  
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория") 
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name="Изображение товара") 

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        avg = self.review_set.aggregate(Avg('rating'))['rating__avg']
        return avg if avg else 0

class Warehouse(models.Model):
    address = models.CharField(max_length=100, verbose_name="Адрес склада")  
    phonenumber = models.CharField(max_length=100, verbose_name="Номер телефона")  

    def __str__(self):
        return self.address

class ProductsOnWarehouse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='warehouse_records', verbose_name="Товар")  
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, verbose_name="Склад")
    quantity = models.IntegerField(default=0, verbose_name="Количество")  

    def __str__(self):
        return f"{self.product.name} на складе {self.warehouse.address}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")  
    date_order = models.DateField(verbose_name="Дата заказа")  
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name="Статус заказа")  
    address_order = models.CharField(max_length=100, verbose_name="Адрес доставки") 
    finish_cost = models.IntegerField(verbose_name="Итоговая стоимость")  
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, verbose_name="Способ оплаты") 

    def __str__(self):
        return f"Заказ {self.id} от {self.user.user_name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")  
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")  
    quantity = models.IntegerField(default=1, verbose_name="Количество")  

    def __str__(self):
        return f"Корзина {self.user.user_name}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")  
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")  
    content = models.TextField(verbose_name="Отзыв")
    rating = models.IntegerField(verbose_name="Рейтинг")  

    def save(self, *args, **kwargs):
        if not (1 <= self.rating <= 5):
            raise ValueError("Рейтинг должен быть от 1 до 5.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Отзыв от {self.user.user_name} на {self.product.name}"

class WhatInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар") 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    quantity = models.PositiveIntegerField(verbose_name="Количество")  
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")  
    def __str__(self):
        return f"{self.quantity} x {self.product.name} в заказе {self.order.id}"


class SupportMessage(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь")  
    subject = models.CharField(max_length=255, verbose_name="Тема")  
    message = models.TextField(verbose_name="Текст сообщения")  
    response = models.TextField(blank=True, null=True, verbose_name="Ответ техподдержки") 
    is_resolved = models.BooleanField(default=False,verbose_name="Статус сообщения")  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Дата обновления")  

    def __str__(self):
        return f"{self.subject} (Resolved: {self.is_resolved})"
