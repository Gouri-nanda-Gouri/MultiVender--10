from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method == "POST":
        a=request.POST.get('txt_num1')
        b=request.POST.get('txt_num2')
        c=int(a)+int(b)
        return render(request,'Basics/Sum.html',{'Result':c})
    else:
        return render(request,'Basics/Sum.html')


def Largest(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_num1'))
        b=int(request.POST.get('txt_num2'))
        if a>b:
            c=a
        else:
            c=b
        return render(request,'Basics/Largest.html',{'Result':c})
    else:
        return render(request,'Basics/Largest.html')




def Calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get('txt_num1'))
        num2=int(request.POST.get('txt_num2'))
        submit=(request.POST.get('btn'))
        if submit== '+':
            sum= num1 + num2
        elif submit=='-':
            sum= num1-num2
        elif submit=='*':
            sum=num1*num2  
        elif submit=='/':
            sum=num1 / num2
        return render(request,'Basics/Calculator.html',{'Result':sum})
    else:
        return render(request,'Basics/Calculator.html')