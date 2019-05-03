from django.shortcuts import render, reverse, redirect
from django.views.generic import View
from django.http import JsonResponse
import logging

logger = logging.getLogger('django')


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        logger.info(username)
        logger.info(mobile)
        return JsonResponse({'username': username, 'mobile': mobile})


class ReverseView(View):
    def get(self, request):
        return redirect(reverse("ReqResp: index"))