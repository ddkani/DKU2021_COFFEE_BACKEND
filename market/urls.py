from rest_framework import routers

from market.views.status import StatusViewSet
from market.views.user import UserViewSet

router = routers.DefaultRouter()
router.register('', StatusViewSet, "서버 운영 정보")
router.register('user', UserViewSet, "사용자 관리")

urlpatterns = router.urls
