#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from trade import controller
from dtiaozao import function as fun


#商品浏览模块
def goodsList(req):
    goods_info = controller.get_goods_info()
    return render(req,'goods_list.html', locals())


#商品详情页模块
def goodsDetail(req):
    if not req.session.get('islogin'):
        msg = '你还未登陆，请先登陆！'
        return render(req,'error_msg.html', locals())
    if req.method == 'GET':
        data = req.GET
        goods_detail = controller.get_goods_detail(data)
        return render(req,'goods_detail.html', locals())
    if req.method == 'POST':
        data = req.POST
        buyer_id = req.session['user_info']['uid']
        rt = controller.purchase(data, buyer_id)
        if rt == 1:
            msg = '购买成功，请返回主页！'
        else:
            msg = '购买失败，请联系管理员！！'
        return render(req,'error_msg.html', locals())


#购买记录模块
def buyHis(req):
    if not req.session.get('islogin'):
        msg = '你还没登录，先登录吧....'
        return render(req,'error_msg.html', locals())
    buyer_id = req.session['user_info']['uid']
    id_group = []
    #将购买者id装入列表后传入controller，是为了迎合controller的处理
    id_group.append((buyer_id, None))
    result = controller.trade_his(id_group)
    return render(req,'buy_history.html', locals())
