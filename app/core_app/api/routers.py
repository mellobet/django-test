from rest_framework.routers import DefaultRouter

from .views import AtendeeSerializerViewSet, EventSerializerViewSet

router = DefaultRouter()

router.register(r"atendees", AtendeeSerializerViewSet, basename="atendee")
router.register(r"events", EventSerializerViewSet, basename="event")

urlpatterns = router.urls
