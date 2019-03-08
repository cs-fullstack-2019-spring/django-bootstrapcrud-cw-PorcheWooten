from django.shortcuts import render, redirect, get_object_or_404
from .forms import GarageSaleModel, GarageSaleForm

# Create your views here.


def index(request):
    saleitems = GarageSaleModel.objects.all() #gets all items
    form = GarageSaleForm(request.POST or None) #send info to form
    form = GarageSaleForm() #returns empty form
    if request.method == "POST":
        if form.is_valid(): #validate
            form.save() #save
# display form
    context = {
        'saleitems': saleitems,
        'form': form,

    }

    return render(request, 'BootCRUDApp/index.html', context)


def edititem(request, id):
    items = get_object_or_404(GarageSaleModel, pk=id) #grab specific item
    form = GarageSaleForm(request.POST or None, instance=items) #grab selected item and send to form to make changes
    if form.is_valid(): #validate form
        form.save() #save form
        return redirect(index) #takes you back to index page
    return render(request, 'BootCRUDApp/index.html', {'form':form})

