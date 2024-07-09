from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from polls.views import PollViewSet, QuestionViewSet, user_polls, AnswerViewSet
from debug_toolbar import urls as debug_toolbar_urls

router = routers.DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('user-polls/<int:user_id>/', user_polls, name='user_polls'),
    path('__debug__/', include(debug_toolbar_urls)),
]
