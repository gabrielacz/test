from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.utils.dateparse import parse_datetime

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        embargo_date = self.request.query_params.get('embargo_date', None)
        
        if start_date:
            start_date = parse_datetime(start_date)
            if start_date:
                queryset = queryset.filter(created_at__gte=start_date)
        
        if embargo_date:
            embargo_date = parse_datetime(embargo_date)
            if embargo_date:
                queryset = queryset.filter(created_at__lte=embargo_date)
        
        return queryset

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class DeactivateOrderView(APIView):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.is_active = False
        order.save()
        return Response({'status': 'Order deactivated'}, status=status.HTTP_200_OK)