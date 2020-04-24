# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark


class BookmarkDetailView(DetailView):  # 상세보기(북마크 확인) 기능
    model = Bookmark


class BookmarkCreateView(CreateView):  # 북마크 등록 기능
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')  # 글쓰기를 완료했을 때 이동할 페이지('list'는 목록보기 페이지 이름)
    template_name_suffix = '_create'    # 템플릿 이름의 접미사 정의, bookmark_create.html


class BookmarkListView(ListView):
    model = Bookmark   # ListView를 상속받아 사용하기 때문에 템플릿 이름도 정해져 있음, (소문자)모델명_list.html
    paginate_by = 5  # 페이징 기능(5건만 보이도록)


class BookmarkUpdateView(UpdateView):  # 수정 기능
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'  # 템플릿명 접미사 정의, 따라서 bookmark_update.html
    success_url = reverse_lazy('list')  # 수정을 완료했을 때 리스트 화면으로 이동


class BookmarkDeleteView(DeleteView):  # 삭제 기능
    model = Bookmark
    success_url = reverse_lazy('list')

