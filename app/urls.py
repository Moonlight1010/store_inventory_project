from .views import order_records, orderform, add_new_product, warehouse_stock, staffs, stocks_pricelist, staff_dashboard, admin_dashboard
from django.urls import path

urlpatterns = [
    path('records/', order_records, name='order_records-page'),
    path('order/', orderform, name='orderform-page'),
    path('add_new/', add_new_product, name='add_new-page'),
    path('warehouse/', warehouse_stock, name='warehouse_stock-page'),
    path('staffs/', staffs, name='staffs-page'),
    path('stocks_pricelist/', stocks_pricelist, name='stocks_pricelist-page'),
    path('', staff_dashboard, name='staff_dashboard-page'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard-page'),
]