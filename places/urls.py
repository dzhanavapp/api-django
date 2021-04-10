from rest_framework import routers

from places.views import PlacesViewSet

router = routers.DefaultRouter()
router.register(r'', PlacesViewSet)
urlpatterns = router.urls
