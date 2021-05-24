from django.shortcuts import render
# views.py => 화면에 출력할 내용을 데이터베이스로 얻어와서 html에 전송
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Notice
'''
  목록 출력 => SELECT * ~  =====> ListView  : from django.views.generic.list import ListView
  상세출력  => WHERE id=1 =====> DetailView : from django.views.generic.detail import ListView
  추가       => INSERT ~      =====> CreateView : from django.views.generic.edit import ListView
  수정       => UPDATE ~     =====> UpdateView : from django.views.generic.edit import ListView
  삭제       => DELETE ~      =====> DeleteView : from django.views.generic.edit import ListView
'''
# Create your views here.
class NoticeListView(ListView):
    model=Notice

class NoticeDetailView(DetailView):
    model=Notice

class NoticeUpdateView(UpdateView):
    model=Notice
    fields = ['name','subject','content']
    template_name_suffix = '_update'