from django.shortcuts import render
from .forms import BmiForm 
# Create your views here.
def bmi(request):
    params = {
        'title' :'BMI計測器',
        'msg' : '身長と体重を入力してください。',
        'form': BmiForm()
    }

    if (request.method=='POST'):
        msg = int(request.POST['weight']) / (int(request.POST['height'])/100 )**2
        params['msg'] = "あなたのBMIは"+'{:.1f}'.format(msg)+"です。"
        params['form'] = BmiForm(request.POST)

    return render(request, 'bmi.html', params)