from django.shortcuts import render
from . models import *

def school(request):
    school = School.objects.all()
    return render(request,"awards/school.html",{"school": school})

def home(request):
    return render(request,"awards/home.html")

def subject(request):
    subject = Subject.objects.all()
    return render(request,"awards/subject.html",{"subject": subject})

def student(request):
    student = Student.objects.all()
    return render(request,"awards/student.html",{"student": student})

def classes(request):
    classes = Classes.objects.all()
    return render(request,"awards/classes.html",{"classes":classes})

def award(request):
    award = Award.objects.all()
    return render(request,"awards/award.html",{"award":award})

def answer(request):
    answer = Answer.objects.all()
    return render(request,"awards/answer.html",{"answer":answer})

def assessment(request):
    assessment = Assessment.objects.all()
    return render(request,"awards/assessment.html",{"assessment":assessment})

def summary(request):
    summary = Summary.objects.all()
    return render(request,"awards/summary.html",{"summary":summary})

