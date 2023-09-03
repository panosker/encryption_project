from django.urls import path
from . import views
#urlpatterns = [
#    path('', views.home, name='home'),
#    path('file-action/', views.file_action, name='file-action'),
#    path('file-encryption/', views.encr_file_view, name='file-encryption'),
#    path('file-decryption/', views.decr_file_view, name='file-decryption'),
#]

urlpatterns = [
    path('file-encrypt/',views.file_encrypt_view,name='file-encrypt'),
    path('file-decrypt/',views.file_decrypt_view,name='file-decrypt'),
    path('download-file/', views.download_file, name='download-file'),
]
