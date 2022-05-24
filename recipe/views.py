from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.


class HomeView(View):
    def get(self, request):
        return HttpResponse('Hi')

    def post(self, requeset):
        pass


class CookBook(View):
    def get(self, request):
        return HttpResponse('Hi')

    def post(self, requeset):
        pass