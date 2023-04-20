from django.shortcuts import get_object_or_404
from datetime import date
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
class MeasurementCreateView(ListCreateAPIView):
      queryset = Measurement.objects.all()
      serializer_class = MeasurementSerializer
      
      def perform_create(self, serializer_class):
        sensor_id = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        return serializer_class.save(sensor_id = sensor_id)


      

      
      
