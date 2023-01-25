from django.shortcuts import render,HttpResponse
from Todo.models import Todo
import mysql.connector as sql
import json
# Create your views here.
######## msql connection #########
def dbConnection():
    db = json.loads(open("config.json").read())
    return db['dbconnect'][0]


def home(request):
    context={'sucsess':False,}
    if request.method=='POST':
        #HANDLING FORM
        title = request.POST['title']
        desc = request.POST['decription']
        print("----",title,desc)
        instance = Todo(taskTitle=title,taskDiscription=desc)
        instance.save()
        dataBaseVar = sql.connect(**dbConnection())
        cursor = dataBaseVar.cursor()
        query = f"insert into task (name,description)values('{title}','{desc}')"
        print("query", query)
        cursor.execute(query)
        dataBaseVar.commit()
        context={'success':True,'name':'sai'}
    else:
        print("----------------------")
    return render(request,'index.html',context)

def todoList(request):
    allmytasks = Todo.objects.all()
    print("allmytasks: ",allmytasks)
    print('---------------------------------------------')
    for each in allmytasks:
        print('each.taskTitle: ',each.taskTitle,'each.taskDiscription: ',each.taskDiscription)
    context={'tasks':allmytasks}
    return render(request,'about.html',context)