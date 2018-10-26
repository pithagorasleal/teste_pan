from django.shortcuts import render, redirect
from .forms import StepForm, ProcessForm, ProcessStepConfigForm
from .models import Step, Process

def login(request):
    return render(request, "login.html")

def index(request):
    
    context = {
        'title': 'Sabadin - Index',
        'setor': 'Inicio'
    }

    return render(request, "index.html", context)

def step_new(request):

    if request.method == "POST":
        form = StepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('step_new')
    else:
        form = StepForm()
    return render(request, 'cadastro_step.html', {'form': form, 'objetos': Step.objects.all()})

def process_new(request):

    if request.method == "POST":
        form = ProcessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('process_new')
    else:
        form = ProcessForm()
    return render(request, 'cadastro_process.html', { 'form': form, 'processos': Process.objects.all()})


def process_config(request):

    if request.method == 'POST':
        form = ProcessStepForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
    else:
        form = ProcessStepConfigForm()

    
    return render(request, 'process_config.html', {'form': form})
