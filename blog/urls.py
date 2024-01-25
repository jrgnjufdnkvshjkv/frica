from django.urls import path
from .views import index, contact, computers, man_clothes, womans_clothes,  computersDetailView, manDetailView, womansDetailView, ComputersUpdateView, ComputersCreateView, computersDetailView, ComputersDeleteView



urlpatterns = [
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('computers/', computers, name='computers'),
    path('man-clothes/', man_clothes, name='man_clothes'),
    path('womans-clothes/', womans_clothes, name='womans_clothes'),
    path('computersDetailView/<slug:computers>/', computersDetailView, name='computersDetailView'),
    path('manDetailView/', manDetailView, name='manDetailView'),
    path('womansDetailView/', womansDetailView, name='womansDetailView'),
    path('computers/edit/<slug>/', ComputersUpdateView.as_view(), name='computersUpdate'),
    path('computers/delete/<slug>/', ComputersDeleteView.as_view(), name='computersDelete'),
    path('computers/create', ComputersCreateView.as_view(), name='computersCreate'),

]
