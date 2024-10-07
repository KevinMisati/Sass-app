from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

@login_required
def profile_list_view(request):
    context = {
        'object_list' : User.objects.filter(is_active=True)
    }
    return render (request,"profiles/list.html",context)

@login_required
def profile_view(request,username=None,*args,**kwargs):
    user = request.user
    #profile_user_object = User.objects.get(username=username)
    profile_user_object = get_object_or_404(User,username=username)
    return HttpResponse(f"Hello there {username} - {profile_user_object.id} - {user.id}")
