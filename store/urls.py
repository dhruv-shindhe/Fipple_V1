from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import StoreCreateView, StoreDetailView, StoreDeleteView, StoreUpdateView


urlpatterns = [
    path('<str:name>/store', views.mystore,name='my-store'),
    path('', views.home, name='store-home'),
    path('new/', StoreCreateView.as_view(), name='store-create'),
    path('<int:pk>', StoreDetailView.as_view(), name='store-detail'),
    path('<int:pk>/delete', StoreDeleteView.as_view(), name='store-delete'),
    path('<int:pk>/update', StoreUpdateView.as_view(), name='store-update'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('home/', views.home_1, name='intro_home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
