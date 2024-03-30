
from django.urls import path,include
from . import views


urlpatterns = [
   
    path('',views.home,name='home'),
    path('folder/',views.Folder_view,name='folder'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.register,name='register'),
    path('add_folder/',views.add_folder,name='add_folder'),
    path('folder/<str:type>/', views.folder_type, name='folder_type'),
     path('add/<int:id>/', views.add_to_playlist, name='add'),
     path('modify/<int:id>/', views.modify_folder, name='modify'),
    path('delete/<int:id>/', views.delete_folder, name='delete'),
    path('remove_music/<int:id>/', views.remove_from_playlist, name='remove_music'),
    path('add_to_favorite/<int:id>/', views.add_to_favorites, name='add_to_favorite'),


]
