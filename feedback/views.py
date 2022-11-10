from django.shortcuts import render,redirect
from .forms import CommentForm

def index(request):
    success = False
    form = CommentForm(data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            success = True

    context = {
        'form':form,
        'success':success
    } 
    return render(request, 'index.html', context)
        
