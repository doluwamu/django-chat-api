from rest_framework import routers
from . import views

app_name = 'account'

router = routers.DefaultRouter()
router.register('', views.AuthViewset, basename="auth")

urlpatterns = []
urlpatterns += router.urls