from rest_framework import routers

from market.views.status import StatusViewSet

router = routers.DefaultRouter()
router.register('', StatusViewSet, "서버 운영 정보 확인")



urlpatterns = router.urls
