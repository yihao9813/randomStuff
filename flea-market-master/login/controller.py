#encoding: utf-8
from login.models import LoginUser # GoodsissueGoods, GoodsissueIssuer, GoodsissueSaler
from dtiaozao import function as fun
import os


#用户注册处理
def user_register(date):
    condition = fun.warp_data(date)
    if condition['passwd'] != condition['repasswd']:
        return 0
    del condition['repasswd']
    passwd = fun.mk_md5(condition['passwd'])
    condition['passwd'] = passwd


    #数据库存储
    try:
        r=LoginUser.objects.get(email=condition['email'])
    except LoginUser.DoesNotExist:
        u = LoginUser(**condition)
        u.save()
        if u.name:
            return 1
        else:
            return -1
    return -2
    

#用户登录处理
def user_login(date):
    condition = fun.warp_data(date)
    email = condition['email']
    passwd = fun.mk_md5(condition['passwd'])
    try:
        r = LoginUser.objects.get(email=email)
    except LoginUser.DoesNotExist:
        return 0
    #判断数据库的账号匹配结果是否存在以及密码是否匹配
    if not r or passwd != r.passwd:
        return 0
    return r
