from django.urls import path
from .views import (
    ContactPageImageListAPIView,
    AppointmentCreateAPIView,
    AppointmentListAPIView,
    AppointmentReplyAPIView
)

urlpatterns = [
    path('image-baground/', ContactPageImageListAPIView.as_view(), name='image-baground'),
    path('create/', AppointmentCreateAPIView.as_view(), name='appointment_create'),
    path('list/', AppointmentListAPIView.as_view(), name='appointment_list'),
    path('reply/', AppointmentReplyAPIView.as_view(), name='appointment_reply'),
]
