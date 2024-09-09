from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/home.html')

def academics(request):
    return render(request, 'main/academics.html')

def admission(request):
    return render(request, 'main/admission.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def course_detail(request, course_name):
    return render(request, f'main/{course_name}.html')

def arts_english(request):
    return render(request, 'main/arts_english.html')

def arts_sociology(request):
    return render(request, 'main/arts_sociology.html')

def cs(request):
    return render(request, 'main/cs.html')

def science_mathematics(request):
    return render(request, 'main/science_mathematics.html')

def commerce_accounting(request):
    return render(request, 'main/commerce_accounting.html')

def commerce_economics(request):
    return render(request, 'main/commerce_economics.html')
def form_view(request):
    finalans=0
    
    try:
        if request.method=="POST":
            n1 =int(request.POST.get('num1'))
            n2 =int(request.POST.get('num2'))
            finalans =n1 +n2
            
    except:
        pass
    return render(request,'main/form.html',{'output':finalans})

# def submitform(request):
#     return HttpResponse(request)
def calculator(request):
    c =''
    try:
        if request.method =="POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c= n1 + n2
            elif opr== "-":
                c= n1 - n2
            elif opr== "*":
                c= n1*n2
            elif opr== "/":
                c= n1 / n2


    except:
        c="Invalid operation...."
    print(c)
    return render(request,"calculator.html",{'c':c})


def markCalculator(request):
    c =''
    try:
        if request.method =="POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c= n1 + n2
            elif opr== "-":
                c= n1 - n2
            elif opr== "*":
                c= n1*n2
            elif opr== "/":
                c= n1 / n2


    except:
        c="Invalid operation...."
    print(c)
    return render(request,"main/markCalculator.html",{'c':c})