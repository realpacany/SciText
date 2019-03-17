from django.shortcuts import render

# Create your views here.


def user_profile(request, id):
    return render(request, 'user_profile.html', {
        'id': id
    })
