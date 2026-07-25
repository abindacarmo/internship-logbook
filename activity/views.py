from django.shortcuts import render, redirect, get_object_or_404
from .models import Aktivitas
from .forms import AktivitasForm

def activity_list(request):
    activities = Aktivitas.objects.all()
    return render(request, 'activity/activity_list.html', {'activities': activities})

def activity_create(request):
    if request.method == 'POST':
        form = AktivitasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = AktivitasForm()
    return render(request, 'activity/activity_form.html', {'form': form})

def activity_update(request, pk):
    activity = get_object_or_404(Aktivitas, pk=pk)
    if request.method == 'POST':
        form = AktivitasForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = AktivitasForm(instance=activity)
    return render(request, 'activity/activity_form.html', {'form': form})

def activity_delete(request, pk):
    activity = get_object_or_404(Aktivitas, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    return render(request, 'activity/activity_confirm_delete.html', {'activity': activity})
