from django.shortcuts import render
from django.contrib.auth import mixins
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import json

from .models import GoodsModel

class ListModelMixin(object):
    def list(self, request):
        print("这是ListModelMixin扩展类")
        return HttpResponse("这是ListModelMixin扩展类")


class CreateModelMixin(object):
    def create(self, request):
        print("这是CreateModelMixin扩展类")
        return HttpResponse("这是CreateModelMixin扩展类")


class BookView(ListModelMixin, CreateModelMixin, View):
    def get(self, request):
        self.list(request)
        return HttpResponse('ok')

    def post(self, request):
        self.create(request)
        return HttpResponse('fine')


class GoodsView(View):
    def get(self, request):
        good = GoodsModel.objects.create(
            name='月亮与六便士',
            price=35.6,
            sale=100
        )
        data_dict = {
            'name':good.name,
            'price': good.price,
            'sale': good.sale
        }
        return JsonResponse({'data': data_dict})



class GetData(View):
    def get(self,request):
        try:
            data = GoodsModel.objects.get(id=1)
        except GoodsModel.DoesNotExist:
            return JsonResponse({'errmsg': '没有此商品'})
        data_dict = {
            'name': data.name,
            'price': data.price,
            'sale': data.sale
        }
        return JsonResponse({'data': data_dict})


class ChangeData(View):
    def get(self, request):
        try:
            goods = GoodsModel.objects.get(id=1)
        except GoodsModel.DoesNotExist:
            return JsonResponse({'errmsg': '没有此商品'})
        goods.price = 40
        goods.save()
        return JsonResponse({'new_price': goods.price})