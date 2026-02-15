from django.urls import path, include
from . import views

# TODO: Dodaj routing do swoich appow w miare ich tworzenia, np:
#   path('menu/', include('menu_app.urls')),
#   path('klienci/', include('customers_app.urls')),
#   path('zamowienia/', include('orders_app.urls')),

urlpatterns = [
    path('hello/', views.hello),
    path('books/', views.booklist),
    path('menu/', include('menu_app.urls')),
    path('klienci/', include('customers_app.urls')),
    path('zamowienia/', include('orders_app.urls'))
]
