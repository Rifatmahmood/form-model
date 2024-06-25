from django.shortcuts import render
from .forms import GroomForm
def form(request):
    if request.method == 'POST':
        groom_form = GroomForm(request.POST)
        if groom_form.is_valid():
            groom_form.save()
            return redirect('add_author')
    else:
        groom_form = GroomForm()
    return render(request, 'form.html', {'form': groom_form} )