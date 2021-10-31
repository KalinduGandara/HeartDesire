from django.shortcuts import render,redirect
from .forms import UserBioForm,PatnertBioForm
from .models import UserBio,PatnertBio

from .utils import matchPreference

from django.contrib.auth.decorators import login_required 

# Create your views here.

def profile(request,id):
    pass
@login_required
def user_bio(request):
    if request.method == 'POST':
        
        bio = UserBio.objects.get(user = request.user)
        bio_form = UserBioForm(data= request.POST,instance=bio)
        if bio_form.is_valid():
            bio.user = request.user
            bio.save()
            return redirect('/')

        else:
            # One of the forms was invalid if this else gets called.
            print(bio_form.errors)
    else:
        try:
            form = UserBio.objects.get(user = request.user)
        except:
            bio_form = UserBioForm()
            return render(request,'Bio.html',{'bio_form':bio_form,'title':'User Bio'})
        bio_form = UserBioForm(instance = form)
        print(request.user.id)
    
    return render(request,'Bio.html',{'bio_form':bio_form,'title':'User Bio'})

@login_required
def Partner_preference(request):
    if request.method == 'POST':
        if PatnertBio.objects.filter(user = request.user).exists():
            bio = PatnertBio.objects.get(user = request.user)
            bio_form = PatnertBioForm(data= request.POST,instance=bio)
        else:
            bio_form = PatnertBioForm(data= request.POST)
            bio = bio_form.save(commit=False)
        if bio_form.is_valid():
            bio.user = request.user
            bio.save()
            return redirect('/')

        else:
            # One of the forms was invalid if this else gets called.
            print(bio_form.errors)
    else:
        try:
            form:PatnertBio = PatnertBio.objects.get(user = request.user)
        except:
            bio_form = PatnertBioForm()
            # matchPreference(form)
            return render(request,'Bio.html',{'bio_form':bio_form,'title':'Patner Bio'})
        bio_form = PatnertBioForm(instance = form)
        matchPreference(request.user,form)
        return render(request,'Bio.html',{'bio_form':bio_form,'title':'Patner Bio'})