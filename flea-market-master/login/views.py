#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from login import controller


#登录模块
def login(request):
    if request.method == 'GET':
        msg = '非法访问！！'
        return render(request,'error_msg.html', locals())
    else:
        data = request.POST
        rt = controller.user_login(data)
        if rt:
            #登录成功后，将用户信息添加到session中
            request.session['islogin'] = True
            user_info = {}
            user_info['uid'] = rt.id
            user_info['name'] = rt.name
            user_info['email'] = rt.email
            user_info['phone'] = rt.phone
            request.session['user_info'] = user_info
            return HttpResponseRedirect('/')
        else:
            msg = '账号或密码错误！'
            return render(request,'error_msg.html', locals())


#登出模块
def logout(request):
    if request.method == 'POST':
        msg = '非法访问！！'
        return render(request,'error_msg.html', locals())
    else:
        #删除session信息
        del request.session['user_info']
        del request.session['islogin']
        return HttpResponseRedirect('/')


#注册模块
def register(request):
    if request.method == 'GET':
        status = False
        return render(request,'user_register.html', locals())
    else:
        status = True
        date = request.POST
        rt = controller.user_register(date)
        if rt == 1:
            msg = '注册成功，请返回首页后登录！'
        elif rt == 0:
            msg = '两次密码填写不正确！'
        elif rt == -1:
            msg = '注册失败，请联系站长！！！'
        else:
            msg = '用户以存在，请重新注册！'
        return render(request,'user_register.html', locals())
