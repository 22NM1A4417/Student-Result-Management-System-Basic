from django.shortcuts import render
from .models import Student, Result
from django.contrib.auth.models import User

def search_result(request):
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            results = Result.objects.filter(student=student)
            return render(request, 'result.html', {
                'student': student,
                'results': results
            })
        except:
            return render(request, 'result.html', {'error': "Student not found"})
    return render(request, 'result.html')


# Create your views here.
