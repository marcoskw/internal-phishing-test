from django.shortcuts import render
from django.http import HttpResponse
from .models import Click
import subprocess


def tracert_and_save(ip_address):

    # Executa o tracert
    process = subprocess.Popen(['tracert', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = process.communicate(timeout=30)  # Timeout de 15 segundos
    result_in_string = ''.join(map(str, result))

    return result_in_string

def click_link(request):

    # Obter o endereço IP do cliente
    ip_address = request.META.get('REMOTE_ADDR')
    # Obter o nome da máquina
    machine_name = tracert_and_save(ip_address)

    # Registrar o clique
    Click.objects.create(
        ip_address=ip_address,
        machine_name=machine_name,
    )

    return render(request, 'collect_email/index.html')