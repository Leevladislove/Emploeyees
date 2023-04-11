from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_visit, name='visit'),
    path('add', views.add_new_visit, name='add_new_visit'),
    path('edit/<int:id>', views.edit_visit, name='edit_visit'),
    path('update/<int:id>', views.update_visit, name='update_visit'),
    path('detail/<int:id>', views.detail_visit, name='detail_visit'),
    path('delete/<int:id>', views.destroy_visit, name='delete_visit'),
]
