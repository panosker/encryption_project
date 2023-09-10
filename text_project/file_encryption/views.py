from .file_encryption import file_encrypt, file_decrypt
from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.urls import reverse
import os
from encr_decr_app.ratelimit import new_rates

@new_rates(non_registered_rate='10/m', registered_rate='50/m')
def download_file(request):
    file_path = request.GET.get('path', '')

    if not file_path:
        return HttpResponse('File not found.', status=404)

    if not os.path.exists(file_path):
        return HttpResponse('File not found.', status=404)

    file_name = os.path.basename(file_path)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    os.remove(file_path)

    return response

@new_rates(non_registered_rate='10/m', registered_rate='50/m')
def file_encrypt_view(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        encrypted_file = file_encrypt(file)
        download_link_encr = reverse('download-file') + '?path=' + encrypted_file

        context = {
            'download_link_encr': download_link_encr,
        }

        return render(request, 'file_encryption/home.html', context)

    return render(request, 'file_encryption/home.html')

@new_rates(non_registered_rate='10/m', registered_rate='50/m')
def file_decrypt_view(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        decrypted_file = file_decrypt(file)
        download_link_decr = reverse('download-file') + '?path=' + decrypted_file

        context = {
            'download_link_decr': download_link_decr,
        }

        return render(request, 'file_encryption/home.html', context)

    return render(request, 'file_encryption/home.html')
