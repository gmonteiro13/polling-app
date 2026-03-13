from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from polls import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'questions', views.QuestionAPIViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    
    # Raiz da API
    path('api/', include(router.urls)), 
    path('api/register/', views.RegisterAPIView.as_view(), name='api_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]