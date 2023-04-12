from django.urls import path
from . import views

app_name = 'app1'  # Replace with the name of your app

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page view
    
    path('carousel-items/', views.carousel_items, name='carousel_items'),  # View for displaying all carousel items
    path('featured-items/', views.featured_items, name='featured_items'),  # View for displaying all featured items
    path('testimonials/', views.testimonials, name='testimonials'),  # View for displaying all testimonials
    
    path('featured-item/<int:pk>/', views.featured_item_detail, name='featured_item_detail'),  # View for displaying details of a specific featured item
    path('testimonial/<int:pk>/', views.testimonial_detail, name='testimonial_detail'),  # View for displaying details of a specific testimonial
    
    path('carousel-item/create/', views.carousel_item_create, name='carousel_item_create'),  # View for creating a new carousel item
    path('featured-item/create/', views.featured_item_create, name='featured_item_create'),  # View for creating a new featured item
    path('testimonial/create/', views.testimonial_create, name='testimonial_create'),  # View for creating a new testimonial
    
    path('carousel-item/update/<int:pk>/', views.carousel_item_update, name='carousel_item_update'),  # View for updating a carousel item
    path('featured-item/update/<int:pk>/', views.featured_item_update, name='featured_item_update'),  # View for updating a featured item
    path('testimonial/update/<int:pk>/', views.testimonial_update, name='testimonial_update'),  # View for updating a testimonial
    
    path('carousel-item/delete/<int:pk>/', views.carousel_item_delete, name='carousel_item_delete'),  # View for deleting a carousel item
    path('featured-item/delete/<int:pk>/', views.featured_item_delete, name='featured_item_delete'),  # View for deleting a featured item
    
    path('logout/', views.logout_view, name='logout'),  # View for handling user logout
    
    path('carousel/item/<int:pk>/', views.CarouselItemDetailView.as_view(), name='carousel_item_detail'),  # View for displaying details of a specific carousel item using Django's class-based views
    
    path('carousel/items/delete_all/', views.carousel_items, name='carousel_items_delete_all'),  # View for deleting all carousel items
    path('carousel_items/make_featured/', views.make_featured, name='carousel_item_make_featured'),

    path('featured_item_detail/<int:pk>/', views.featured_item_detail, name='featured_item_detail'),

]
