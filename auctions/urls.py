from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:id>", views.listing, name="listing")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)