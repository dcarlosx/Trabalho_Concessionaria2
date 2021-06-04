from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import *

class MotoForm(ModelForm):
    class Meta:
        model = Moto
        fields = ['venda', 'cliente', 'marca', 'ano', 'valor', 'data_cadastro']

def cadastrar_moto(request, template_name='moto_form.html'):
    form = MotoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('moto_list')
    return render(request, template_name, {'form': form})

def listar_moto(request, template_name="moto_list.html"):
    query = request.GET.get("busca")
    if query:
        moto = Moto.objects.filter(venda__icontains=query)
    else:
        moto = Moto.objects.all()
    motos = {'lista': moto}
    return render(request, template_name, motos)

def editar_moto(request, pk, template_name='moto_form.html'):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == "POST":
        form = MotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            return redirect('moto_list')
    else:
        form = MotoForm(instance=moto)
    return render(request, template_name, {'form': form})

def remover_moto(request, pk, template_name='moto_delete.html'):
    moto = Moto.objects.get(pk = pk)
    if request.method == "POST":
        moto.delete()
        return redirect('moto_list')
    return render(request, template_name, {'moto': moto})