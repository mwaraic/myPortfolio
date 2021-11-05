from django.urls import path,include
from .views import TestView, OpenView

urlpatterns = [
    path('api/resume/', TestView.as_view({'get':'list'})),
    path('api/resume/<int:pk>', TestView.as_view({'put':'update'})),
    path('api/open/<str:name>', OpenView.as_view({'get':'list'})),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]