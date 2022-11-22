from rest_framework import routers
from . import views

app_name = 'chat'

router = routers.DefaultRouter()
router.register('message', views.MessageViewset, basename="message")

urlpatterns = []
urlpatterns += router.urls