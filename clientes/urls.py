from django.urls import path
from .views import cliente_list, cliente_new, cliente_update, cliente_delete

urlpatterns = [
    path('list/', cliente_list, name='cliente_list'),
    path('new/', cliente_new, name='cliente_new'),
    path('update/<int:id>', cliente_update, name='cliente_update'),
    path('delete/<int:id>', cliente_delete, name='cliente_delete'),
]