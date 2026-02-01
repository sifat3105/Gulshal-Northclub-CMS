from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactPageImage, Appointment
from .serializers import ContactPageImageSerializer, AppointmentSerializer
from django.core.mail import send_mail




class ContactPageImageListAPIView(APIView):
    def get(self, request):
        images = ContactPageImage.objects.first()
        serializer = ContactPageImageSerializer(images)
        return Response({
            'status': 'success',
            'message': 'Contact page images fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })





# Create Appointment (User)

class AppointmentCreateAPIView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Appointment submitted successfully',
                'status_code': status.HTTP_201_CREATED,
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'status': 'error',
            'message': 'Validation failed',
            'status_code': status.HTTP_400_BAD_REQUEST,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


#  List Appointments (Admin)

class AppointmentListAPIView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all().order_by('-created_at')
        serializer = AppointmentSerializer(appointments, many=True)

        return Response({
            'status': 'success',
            'message': 'Appointments fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        }, status=status.HTTP_200_OK)



# Reply to User Email (Admin)

class AppointmentReplyAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        if not email or not subject or not message:
            return Response({
                'status': 'error',
                'message': 'email, subject and message are required',
                'status_code': status.HTTP_400_BAD_REQUEST,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)

        send_mail(
            subject,
            message,
            "admin@yourwebsite.com",  # From email
            [email]
        )

        return Response({
            'status': 'success',
            'message': 'Email sent successfully',
            'status_code': status.HTTP_200_OK,
            'data': {
                'email': email,
                'subject': subject,
                'message': message
            }
        }, status=status.HTTP_200_OK)
