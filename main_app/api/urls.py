from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import AnswerViewSet, QuestionViewSet

router_v1 = DefaultRouter()
router_v1.register(
    'questions',
    QuestionViewSet,
    basename='questions'
)
router_v1.register(
    r'questions/(?P<post_id>\d+)/answers',
    AnswerViewSet,
    basename='answers'
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]
