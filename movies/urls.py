from django.urls import path, include
from rest_framework import routers
from movies.views import MovieDirectorView, MovieViewSet, PersonViewSet




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('person', PersonViewSet)
router.register('movie', MovieViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('movie/<int:pk>/director/<int:director_id>/', MovieDirectorView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]