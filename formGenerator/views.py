from operator import mod
from statistics import mode
from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def index(request):
    forms = models.Forms.objects.all()
    for i in forms:
        print(i.label)
    return render(request,'./index.html',context={'forms':forms})

def form(request, formkey):
    print(formkey)
    main = models.MainForm.objects.get(InviteKey=formkey)
    forms = models.Forms.objects.filter(formParent=main).all()
    states = models.States.objects.all()
    return render(request,'./index.html',context={'forms':forms,
                                                        'main':main,
                                                        'states':states})

fd = []
def submit(request,formkey):
    main = models.MainForm.objects.get(InviteKey=formkey)
    form = models.Forms.objects.filter(formParent=main).all()
    if request.method == 'POST':
        data = request.POST
        print(data)
        for i in data:
            print(i)
            fieldValues = data[i]
            print(fieldValues)
            fieldName = i
            # if data['newfield']:
            #     print('here')
            #     fieldName = 'userdefine_field'
            
            # fd.append(fieldName)
            # print(fieldValues)
            # print(fieldName)
            if not fieldName == 'csrfmiddlewaretoken':
                    newstore =  models.FormStore(form=main,fieldName=fieldName,
                                        fieldData=fieldValues)
                    newstore.save()
            # for j in fieldValues:
            #     print(j)
        # print(data)

        return HttpResponse('form submission completed')


def AddNewForm(request):
    from random import randint
    fid = randint(12345,765467676)
    
    return render(request,'./newform.html',context={'fid':fid})