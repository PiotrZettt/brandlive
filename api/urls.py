from django.urls import path
from .views import candidate_api, candidate_detail


urlpatterns = [
    path('', candidate_api, name='candidate'),
    path('candidates/<int:pk>', candidate_detail, name='candidate_detail')
    ]

