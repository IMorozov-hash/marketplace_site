from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_home, name='product-home'),
    path('create/', views.create, name='product-create'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update', views.ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete', views.ProductDeleteView.as_view(), name='product-delete')
]