from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import twsuser

# Create your views here.
def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST['username']
        company = request.POST['company']
        address = request.POST['address']
        call = request.POST['call']
        email = request.POST['email']
        id = request.POST['id']
        pw = request.POST['pw']
        pwc = request.POST['pwc']
        res_data = {}
        if not (username and pw and pwc and company and address and call and email and id) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if pw != pwc:
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = twsuser(
                username=username,
                company=company,
                address=address,
                call=call,
                email=email,
                id=id,
                pw=pw,
            )
            user.save()
            return redirect('/twsuser/login1/')
        return render(request, 'register.html', res_data)

def login1(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'login1.html')

    elif request.method == "POST":
        login_id = request.POST['id']
        login_password = request.POST['pw']

        if not (login_id and login_password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
        else:
            myuser = twsuser.objects.get(id=login_id)
            if (login_password == myuser.pw):
                request.session['twsuser'] = myuser.id
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/photo/main')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login1.html', response_data)


def main(request):
    user_id = request.session.get('twsuser')

    if request.method == "GET":
        return render(request, 'main.html')


def shopping(request):
    res_data = {}
    user = twsuser.objects.get()
    res_data['company'] = user.company
    res_data['address'] = user.address
    res_data['call'] = user.call
    res_data['email'] = user.email

    return render(request, 'shopping.html', res_data)
