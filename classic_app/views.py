from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import File
from .forms import UploadForm

def index(request):
    return HttpResponse('Hello there')

def classic_app(request):
    data = File.objects.all()
    return render(request, 'classic_app/classic_app.html', {'files': data, 'form':UploadForm})

def file(request, file_id):
    #f = next((item for item in data if item['id'] == file_id), None) # where next() is a python generator
    f = File.objects.get(pk=file_id)
    if f is not None:
        return render(request, 'classic_app/file.html', {'file':f})
    else:
        #raise Http404("File does not exist")
        return render(request, '404.html')

def edit(request, file_id):
    name = request.POST.get('name')
    file_type = request.POST.get('type')
    f = File.objects.get(pk=file_id)
    print(name, file_type, f)
    if f:
        if name:
            f.name = name
        if file_type:
            f.file_type = file_type
        f.save()
        return redirect(classic_app)
    else:
        return redirect(classic_app)

def delete(request, file_id):
    f = File.objects.get(pk=file_id)
    if f:
        f.delete()
    return redirect(classic_app)

def upload(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect(classic_app)
