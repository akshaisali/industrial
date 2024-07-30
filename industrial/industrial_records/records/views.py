from django.shortcuts import render, redirect, get_object_or_404
from .forms import MaterialDetailForm
from .models import MaterialDetail


def home(request):
    return render(request, 'records/home.html')

def material_list(request, sqf_type):
    data = MaterialDetail.objects.filter(sqf_type=sqf_type)
    return render(request, 'records/sqf_list.html', {'data': data, 'sqf_type': sqf_type})

def material_add(request, sqf_type):
    if request.method == 'POST':
        form = MaterialDetailForm(request.POST)
        if form.is_valid():
            MaterialDetail = form.save(commit=False)
            MaterialDetail.sqf_type = sqf_type
            MaterialDetail.save()
            return redirect('material_list', sqf_type=sqf_type)
    else:
        form = MaterialDetailForm()
    return render(request, 'records/material_form.html', {'form': form, 'sqf_type': sqf_type})

def sqf_80(request):
    return material_list(request, '80')

def sqf_100(request):
    return material_list(request, '100')

def sqf_120(request):
    return material_list(request, '120')

def material_edit(request, pk):
    material = get_object_or_404(MaterialDetail, pk=pk)
    if request.method == 'POST':
        form = MaterialDetailForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_list', sqf_type=material.sqf_type)
    else:
        form = MaterialDetailForm(instance=material)
    return render(request, 'records/material_edit.html', {'form': form})
def material_delete(request, pk):
    material = get_object_or_404(MaterialDetail, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('material_list', sqf_type=material.sqf_type)
    return render(request, 'records/material_confirm_delete.html', {'material': material})
def material_list(request, sqf_type):
    data = MaterialDetail.objects.filter(sqf_type=sqf_type)
    return render(request, 'records/sqf_list.html', {'data': data, 'sqf_type': sqf_type})

def material_confirm_delete(request, pk):
    MaterialDetail = get_object_or_404(MaterialDetail, pk=pk)
    if request.method == 'POST':
        MaterialDetail.delete()
        return redirect('material_list', sqf_type=MaterialDetail.sqf_type)
    return render(request, 'records/material_confirm_delete.html', {'material': MaterialDetail})
def tempering(request, sqf_type):
    data = MaterialDetail.objects.filter(sqf_type=sqf_type)  
    return render(request, 'records/tempering.html', {'data': data, 'sqf_type': sqf_type})

def washing(request, sqf_type):
    # Placeholder view for Washing
    data = MaterialDetail.objects.filter(sqf_type=sqf_type)
    return render(request, 'records/washing.html', {'data': data, 'sqf_type': sqf_type})

def travelser(request, sqf_type):
    # Placeholder view for Traverser
    data = MaterialDetail.objects.filter(sqf_type=sqf_type)
    return render(request, 'records/travelser.html', {'data': data, 'sqf_type': sqf_type})

def crossconveyor(request, sqf_type):
    # Placeholder view for Cross Conveyor
    data = MaterialDetail.objects.filter(sqf_type=sqf_type)
    return render(request, 'records/crossconveyor.html', {'data': data, 'sqf_type': sqf_type})