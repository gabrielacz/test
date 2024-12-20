
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderTagsView
from interview.order.views import DeactivateOrderView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('deactivate/<int:pk>/', DeactivateOrderView.as_view(), name='order-deactivate'),
    path('<int:order_id>/tags/', OrderTagsView.as_view(), name='order-tags'),
]