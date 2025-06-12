from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import (
    Product, Service, TrainingEvent, BlogPost,
    Journal, CaseStudy, TeamMember, ContactMessage
)
from .serializers import (
    UserSerializer, ProductSerializer, ServiceSerializer,
    TrainingEventSerializer, BlogPostSerializer, JournalSerializer,
    CaseStudySerializer, TeamMemberSerializer, ContactMessageSerializer
)
from rest_framework import status

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

class TrainingEventViewSet(viewsets.ModelViewSet):
    queryset = TrainingEvent.objects.all()
    serializer_class = TrainingEventSerializer
    permission_classes = [permissions.AllowAny]

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [permissions.AllowAny]

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.AllowAny]

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

@api_view(['POST'])
def contact_submit(request):
    try:
        contact = ContactMessage.objects.create(
            name=request.data.get('name'),
            email=request.data.get('email'),
            subject=request.data.get('inquiryType'),  # Using inquiryType as subject
            message=request.data.get('message')
        )
        return Response({
            'message': 'Thank you for your message. We will get back to you soon.',
            'id': contact.id
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({
            'message': 'Failed to submit contact form. Please try again.'
        }, status=status.HTTP_400_BAD_REQUEST)
