from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user', UserViewSet, basename = 'user')
router.register(r'question', QuestionViewSet, basename = 'user')
router.register(r'questionnaire', QuestionnaireViewSet, basename = 'user')
router.register(r'answer', AnswerViewSet, basename = 'user')

urlpatterns = router.urls

