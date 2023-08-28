from django.shortcuts import render
from .models import Record
from django.http import HttpResponseRedirect

def main(request):
    a = Record.objects.all()
    context = {'queryset': a}
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        record = Record.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )
        return HttpResponseRedirect('/')


def delete(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect ('/')


def edit(request, pk):
    record = Record.objects.get(pk=pk)
    if request.method == 'POST':
        record.title = request.POST.get('title')
        record.description = request.POST.get('description')
        record.save()
        return HttpResponseRedirect ('/')
    context = {
        'record':record,
    }
    return render(request, 'todo/edit.html', context )