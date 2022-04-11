from django.conf.urls import url
from rest_framework import routers
from .views import ElectionViewSet

# router = routers.DefaultRouter()
# router.register(r'electionresults', APIView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('electionapi', ElectionViewSet.as_view()),
]