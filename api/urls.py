from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'training-events', views.TrainingEventViewSet)
router.register(r'blog-posts', views.BlogPostViewSet)
router.register(r'journals', views.JournalViewSet)
router.register(r'case-studies', views.CaseStudyViewSet)
router.register(r'team-members', views.TeamMemberViewSet)
router.register(r'contact-messages', views.ContactMessageViewSet)

from .views import contact_submit

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', contact_submit, name='contact-submit'),
] 