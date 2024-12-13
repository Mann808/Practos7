from django.contrib import admin
from django.urls import path
from shop import views
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render  
from  shop.views import import_orders
urlpatterns = [
    path('admin/', views.admin_console, name='admin_console'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/buyer/', views.buyer_dashboard, name='buyer_dashboard'),
    path('dashboard/seller/', views.seller_dashboard, name='seller_dashboard'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('profile/', views.profile, name='profile'),
    path('staff_profile/', views.staff_profile, name='staff_profile'), 
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('seller/orders/', views.seller_orders, name='seller_orders'),
    path('seller/orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('cart/update/<int:cart_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('warehouse/', views.warehouse_dashboard, name='warehouse_dashboard'),
    path('warehouse/update_stock/<int:product_id>/', views.update_stock, name='update_stock'),
    path('warehouse/orders/', views.warehouse_manage_orders, name='warehouse_manage_orders'),
    path('support/request/', views.support_request, name='support_request'),
    path('support/dashboard/', views.support_dashboard, name='support_dashboard'),
    path('support/reply/<int:message_id>/', views.support_reply, name='support_reply'),
    path('support/success/', lambda request: render(request, 'shop/support_success.html'), name='support_success'),

    path('admin/save_database/', views.save_database, name='save_database'),
    path('admin/view_database/', views.view_database, name='view_database'),
    path('admin/manage/<str:table_name>/', views.manage_table, name='manage_table'),
    path('admin/add/<str:table_name>/', views.add_object, name='add_object'),
    path('admin/edit/<str:table_name>/<int:object_id>/', views.edit_object, name='edit_object'),
    path('admin/delete/<str:table_name>/<int:object_id>/', views.delete_object, name='delete_object'),

    path('order/<int:order_id>/qr/', views.generate_order_qr, name='generate_qr_code'),
    path('admin/load_database/', views.load_database, name='load_database'),
    path('product/<int:product_id>/cr_review/', views.add_review, name='cr_review'),
    path('product/<int:product_id>/reviews/', views.product_reviews, name='product_reviews'),
    path('export_sales/', views.export_sales_report, name='export_sales'),
    path('admin/sales_chart/', views.sales_chart, name='sales_chart'),

    path('admin/import_orders/', import_orders, name='import_orders'),
    path('export_sales_csv/', views.export_sales_report_csv, name='export_sales_csv'),

]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
