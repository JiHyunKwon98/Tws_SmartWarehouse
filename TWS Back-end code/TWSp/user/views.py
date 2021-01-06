from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def signup(request):    #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)  # 딕셔너리형태
        id = request.POST.get('id', None)
        pw = request.POST.get('pw', None)
        pwc = request.POST.get('pwc', None)
        company = request.POST.get('company', None)
        address = request.POST.get('address', None)
        call = request.POST.get('call', None)
        email = request.POST.get('email', None)
        print(username, id, pw, pwc, company, address, call, email)
        user = User()
        user.username=username
        user.id=id
        user.pw=pw
        user.pwc=pwc
        user.company=company
        user.address=address
        user.call=call
        user.email=email
        user.save()
        return render(request, 'signup.html')


def login(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('pw', None)

        if not (login_username and login_password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
        else:
            user = User.objects.get(username=login_username)
            # db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, user.pw):
                request.session['user'] = user.id
                # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login.html', response_data)

def home(request):
    user_id = request.session.get('user')
    if user_id :
        user_info = User.objects.get(pk=user_id)  #pk : primary key
        return HttpResponse(user_info.username)   # 로그인을 했다면, username 출력

    return HttpResponse('로그인을 해주세요.') #session에 user가 없다면, (로그인을 안했다면)