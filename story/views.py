from django.shortcuts import render
from .models import Storie
from .forms import StoryForm

def index(request):

    queryset=Storie.objects.all()

    return render(request, 'index.html', {'stories':queryset,})


def dynamic_story(request,id):
    queryset = Storie.objects.get(id=id)
    context={
        'data':queryset,
    }
    return render(request, 'stories.html',context)




def Stories_form(request, *args, **kwargs):

    form = StoryForm()
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            Storie.objects.create(**form.cleaned_data)
        form = StoryForm()

    context = {
        'form': form,
    }
    return render(request, 'upload_story.html', context)