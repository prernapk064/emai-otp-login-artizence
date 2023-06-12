from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *

# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'Registration successfully. Please check your email for the OTP.',
                    'data': serializer.data,
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal server error',
                'data': None
            })

        
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)
            
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                
                user = User.objects.filter(email=email).first()
                if not user:
                    return Response({
                        'status': 400,
                        'message': 'Invalid email',
                        'data': None
                    })
                    
                if user.otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'Wrong OTP',
                        'data': None
                    })
                
                user.is_verified = True
                user.save()
                
                return Response({
                    'status': 200,
                    'message': 'Account verified successfully',
                    'data': None
                })
        
            else:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'data': serializer.errors
                })
            
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal server error',
                'data': None
            })
