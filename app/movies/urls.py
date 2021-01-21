# app/movies/urls.py

from rest_framework.routers import DefaultRouter

from .views import MovieViewSet

router = DefaultRouter()

router.register(prefix=r"api/movies", viewset=MovieViewSet, basename="movie")

urlpatterns = router.urls
