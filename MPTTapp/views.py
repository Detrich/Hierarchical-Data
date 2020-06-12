from django.shortcuts import render
from MPTTapp.models import FolderorFile
# Create your views here.
def showfilesorfolder(request):
    return render(request,'homepage.html',{'which':FolderorFile.objects.all()})