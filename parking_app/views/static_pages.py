from django.shortcuts import render

def pseudo_points_history(request):
    return render(request, 'points_history.html')