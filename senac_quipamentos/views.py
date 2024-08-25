from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from lista.models import Agendamento, Equipamentos
def Homepage(request):
        return render(request, 'home.html', {})
def proof(request):
        return render(request, 'equipments.html', {})

def criar_agendamento(request):
    if request.method == 'POST':
        # Coleta de dados
        prof_instrutor = request.POST['prof_instrutor']
        turno = request.POST['turno']
        sala = request.POST['sala']
        data = request.POST['data']

        notebook = int(request.POST.get('notebook', 0))
        projetor = int(request.POST.get('projetor', 0))
        camera_fotografica = int(request.POST.get('camera_fotografica', 0))
        tripe_camera = int(request.POST.get('tripe_camera', 0))
        font_caix_som = int(request.POST.get('font_caix_som', 0))
        microfone = int(request.POST.get('microfone', 0))
        caneta_lousa_interativa = int(request.POST.get('caneta_lousa_interativa', 0))
        controle_tv = int(request.POST.get('controle_tv', 0))
        controle_projetor = int(request.POST.get('controle_projetor', 0))

        # Geração dos objetos
        equipamentos = Equipamentos.objects.create(
            notebook=notebook,
            projetor=projetor,
            camera_fotografica=camera_fotografica,
            tripe_camera=tripe_camera,
            font_caix_som=font_caix_som,
            microfone=microfone,
            caneta_lousa_interativa=caneta_lousa_interativa,
            controle_tv=controle_tv,
            controle_projetor=controle_projetor
        )

        agendamento = Agendamento.objects.create(
            equipamentos=equipamentos,
            prof_instrutor=prof_instrutor,
            turno=turno,
            sala=sala,
            data=data
        )

        # Redirecionar para a página de geração do comprovante em PDF
        return redirect('gerar_comprovante', agendamento_id=agendamento.pk)

    return render(request, 'comprovante.html')
