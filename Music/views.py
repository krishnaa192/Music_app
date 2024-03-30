from django.shortcuts import render
from .models import *
from .forms import *
from .forms import MusicForm, FolderForm
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.
def home(request):
    music=Music.objects.all()
    context={'music':music}
    return render(request,'index.html',context)

def loginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
            return redirect('login')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username is already taken. Please choose a different one.'})
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
       
        login(request,user)
        Folder.objects.create(user=request.user, name="Favorite")
        return redirect('home')
    return render(request,'register.html')

def folder_type(request,type):
    folders = get_object_or_404(Folder, name=type, user=request.user)

    # Get all music associated with the folder
    folder_music = folders.music.all()
    
    context={'folders':folders,'folder_music':folder_music}
    return render(request,'folders.html',context)



def Folder_view(request):
    folders=Folder.objects.filter(user=request.user)
    context={'folders':folders}
    return render(request,'folder.html',context)

def add_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            try:
                # Create the new folder submitted through the form
                folder = form.save(commit=False)
                folder.user = request.user
                folder.save()
                
                # Create the "Favorite" folder for the user
                
                
                return redirect('folder')
            except IntegrityError:
                # Handle the case where folder name already exists for the user
                form.add_error('name', 'A folder with this name already exists.')
    else:
        form = FolderForm()
    return render(request, 'add_folder.html', {'form': form})

def modify_folder(request, id):
    folder = Folder.objects.get(id=id)
    if request.method == 'POST':
        form =  FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('folder')
    else:
        form =  FolderForm(instance=folder)
    return render(request, 'add_folder.html', {'form': form})

@login_required(login_url="login")
def delete_folder(request,id):
 user = request.user
 folder=Folder.objects.get(id=id)
#  if request.user == blog.user:
 if request.method == 'POST':
    folder.delete()
    return redirect('home')
 context={'folder':folder}
 return render(request,"delete_playlist.html",context)
    

def add_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MusicForm()
    return render(request, 'add_music.html', {'form': form})

def modify_music(request, id):
    music = Music.objects.get(id=id)
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            form.save()
    else:
        form = MusicForm(instance=music)
    return render(request, 'add_music.html', {'form': form})

def delete_music(request, id):
    music = Music.objects.get(id=id)
    music.delete()
    return render(request, 'index.html')



@login_required
def add_to_playlist(request,id):
   
        user_folders = Folder.objects.filter(user=request.user)
        selected_music = get_object_or_404(Music, id=id)
        if request.method == 'POST':
            folder_id = request.POST.get('folder')
            folder = get_object_or_404(Folder, id=folder_id)
            folder.music.add(selected_music)
            return redirect('folder')
        return render(request, 'add_to_playlist.html', {'selected_music': selected_music, 'user_folders': user_folders})




@login_required
def remove_from_playlist(request, id):
    # Remove music from playlist
    user = request.user
    music = get_object_or_404(Music, id=id)
    user_folders = Folder.objects.filter(user=user)
    for folder in user_folders:
        folder.music.remove(music)
    return redirect('folder')





# views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Music, Folder

def add_to_favorites(request, id):
    
    music = get_object_or_404(Music, id=id)
    favorites_folder, _ = Folder.objects.get_or_create(name='Favorite', user=request.user)
    if music not in favorites_folder.music.all():
     favorites_folder.music.add(music)
     return redirect('folder')
    else:
        #music already in favorites
        messages.info(request, 'This music is already in your favorites.')
        return redirect('home')



    