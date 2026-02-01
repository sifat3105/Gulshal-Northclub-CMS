from django.urls import path
from .views import FooterFullDataView

urlpatterns = [
    path("footer-all/", FooterFullDataView.as_view(), name="footer-full-data"),
]
