from .views import RegisterUserDetailsViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'registeruserlist', RegisterUserDetailsViewsets, basename='registeruserlist')
urlpatterns = router.urls