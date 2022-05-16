from django.contrib import admin
from django.urls import include, path
from escola.views import AlunosViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos',AlunosViewset)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
