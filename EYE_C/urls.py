
from django.urls import path
from EYE_C.views import index_view,about_view,contact_view
urlpatterns = [
    path('', index_view),
    path('About', about_view),
    path('Contact', contact_view)
]
