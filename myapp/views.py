from django.shortcuts import render

def index(req):
  return render(req, 'myapp/index.html')

def cal(req):
    a = 5
    b = 6
    c = a*b
    return render(req, 'myapp/index.html', {'a':a,'b':b,'c':c})