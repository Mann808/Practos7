from django.contrib import admin
from .models import (OrderStatus, PaymentMethod, Role, User, Product, Category,
                     Order, Cart, Warehouse, Review, WhatInOrder, ProductsOnWarehouse)

admin.site.register(OrderStatus)
admin.site.register(PaymentMethod)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Warehouse)
admin.site.register(Review)
admin.site.register(WhatInOrder)
admin.site.register(ProductsOnWarehouse)
