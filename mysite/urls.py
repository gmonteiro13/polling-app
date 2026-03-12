from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from polls import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
] + debug_toolbar_urls()