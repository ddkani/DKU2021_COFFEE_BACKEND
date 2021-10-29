from rest_framework import routers

from market.views.market import MarketViewSet
from market.views.status import StatusViewSet
from market.views.user import UserViewSet

router = routers.DefaultRouter()
router.register('', StatusViewSet, "서버 운영 정보")
router.register('users', UserViewSet, "사용자 관리")
router.register('markets', MarketViewSet, "마켓 데이터 정보")


urlpatterns = router.urls
