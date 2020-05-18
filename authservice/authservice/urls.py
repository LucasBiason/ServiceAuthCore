from django.urls import path, include
    
urlpatterns = [
    path('auth/v1/token/', include('authentication.urls')),
    path('api/v1/users/', include('users.urls')),
]
