from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from polls.views import PollViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
