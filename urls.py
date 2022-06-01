from django.urls import path
from orders.views.order_views import *
from orders.views.order_rate_lookup_views import *

app_name = 'orders'

urlpatterns = [
    path('list/', OrderShipmentsAllListView.as_view(), name='all-orders-shipments-list'),
    path('detail/<str:o_Order_ID>/', OrderDetailView.as_view(), name='order-detail'),
    path('rate-lookup/', OrderRateLookupView.as_view(), name='order-rate-lookup'),
]

