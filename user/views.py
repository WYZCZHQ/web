from django.shortcuts import render,HttpResponse
from io import BytesIO
import user.checkcode as check_code
# Create your views here.
def index(request):
    return render(request,'user/index.html')
def register(request):
    return render(request,'user/register.html')
def create_code_img(request):
    #在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img,code = check_code.create_code()
    request.session['check_code'] = code
    img.save(f,'PNG')
    return HttpResponse(f.getvalue())