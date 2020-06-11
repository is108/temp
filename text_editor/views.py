from django.shortcuts import render, get_object_or_404, redirect

from .models import Text, Image, File
from .forms import TextForm, ImageForm, FileForm


def show_text(request):
    text = Text.objects.get(pk = 1)
    images = Image.objects.all()
    return render(request, 'text_editor/show_text.html', {'text': text, 'images': images})

def edit_text(request):
    text = get_object_or_404(Text, pk=1)
    if request.method == "POST":
        form = TextForm(request.POST, instance=text)
        if form.is_valid():
            text = form.save(commit=False)
            text.save()
            return redirect('show_text')
    else:
        form = TextForm(instance=text)

    return render(request, 'text_editor/edit_text.html', {'form': form})

def load_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST)
        print("start")
        print(request.body)
        print("end")
        print ("form", form)
        print("request", request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
            return redirect('show_text')
        print("error", form.errors)
    else:
        form = ImageForm()
    return render(request, 'text_editor/load_image.html', {'form': form})

def load_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['files']
            form.save()
    else:
        form = FileForm(request.POST, request.FILES)
    return render(request, 'text_editor/load_file.html', {'form': form})

def show_files(request):
    files = File.objects.all()
    return render(request, 'text_editor/show_files.html', {'files': files})
