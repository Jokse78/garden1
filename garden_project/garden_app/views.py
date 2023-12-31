from django.shortcuts import render
from .models import Veisle, Darzo_darbai
from .forms import VeisleForm, Darzo_darbaiForm
def index(request):
    return render(request, 'garden_app/index.html')

def mano_veisles(request):
    user = request.user
    veisles = Veisle.objects.filter(darzas__vartotojas=user)
    return render(request, 'garden_app/mano_veisles.html', {'veisles': veisles})

def vaisiu_poreikis(request, veisle_id):
    veisle = Veisle.objects.get(pk=veisle_id)
    return render(request, 'garden_app/vaisiu_poreikis.html', {'veisle': veisle})
def vaisiu_poreikis(request, veisle_id):
    veisle = Veisle.objects.get(pk=veisle_id)
    if request.method == 'POST':
        form = Darzo_darbaiForm(request.POST)
        if form.is_valid():
            darzas = form.save(commit=False)
            darzas.vartotojas = request.user
            darzas.veisle = veisle
            darzas.save()
    else:
        form = Darzo_darbaiForm()
    return render(request, 'garden_app/vaisiu_poreikis.html', {'veisle': veisle, 'form': form})



