#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from login import controller


#登录模块
def login(req):
    if req.method == 'GET':
        msg = '非法访问！！'
        return render(req,'error_msg.html', locals())
    else:
        data = req.POST
        rt = controller.user_login(data) # change start
        if rt == -1:
            msg = '账号或密码错误！'
            return render(req,'error_msg.html', locals())
            #change end
        elif rt:
            #登录成功后，将用户信息添加到session中
            req.session['islogin'] = True
            user_info = {}
            user_info['uid'] = rt.id
            user_info['name'] = rt.name
            user_info['email'] = rt.email
            user_info['phone'] = rt.phone
            req.session['user_info'] = user_info
            return HttpResponseRedirect('/')


#登出模块
def logout(req):
    if req.method == 'POST':
        msg = '非法访问！！'
        return render(req,'error_msg.html', locals())
    else:
        #删除session信息
        del req.session['user_info']
        del req.session['islogin']
        return HttpResponseRedirect('/')


#注册模块
def register(req):
    if req.method == 'GET':
        status = False
        return render(req,'user_register.html', locals())
    else:
        status = True
        date = req.POST
        rt = controller.user_register(date)
        if rt == 1:
            msg = '注册成功，请返回首页后登录！'
            
        #change Start
        elif rt == 0:
            msg = '两次密码填写不正确！'
        elif rt == -2:
            msg = 'Email already exists!'
        elif rt == -3:
            msg = "Username already exists."
        else:
            msg = '注册失败，请联系站长！！！'
        return render(req,'user_register.html', locals())
        #change End
