from django.shortcuts import render, redirect, HttpResponse
from utils.pay import AliPay
import json
import time


def ali():
    # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
    app_id = "2016091100486897"
    # POST请求，用于最后的检测
    notify_url = "http://47.94.172.250:8804/page2/"
    # notify_url = "http://www.wupeiqi.com:8804/page2/"

    # GET请求，用于页面的跳转展示
    return_url = "http://47.94.172.250:8804/page2/"
    # return_url = "http://www.wupeiqi.com:8804/page2/"

    merchant_private_key_path = "keys/app_private_2048.txt"
    alipay_public_key_path = "keys/alipay_public_2048.txt"

    alipay = AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=merchant_private_key_path,
        alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        debug=True,  # 默认False,
    )
    return alipay


def page1(request):
    if request.method == "GET":
        return render(request, 'page1.html')
    else:
        money = float(request.POST.get('money'))
        alipay = ali()
        # 生成支付的url
        query_params = alipay.direct_pay(
            subject="充气式韩红",  # 商品简单描述
            out_trade_no="x2" + str(time.time()),  # 商户订单号
            total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
        )

        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)

        return redirect(pay_url)


def page2(request):
    alipay = ali()
    if request.method == "POST":
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        print(post_dict)

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        print('POST验证', status)
        return HttpResponse('POST返回')

    else:
        params = request.GET.dict()
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        print('GET验证', status)
        return HttpResponse('支付成功')
