from django.contrib import admin

from .models import Bookmark

admin.site.register(Bookmark)  # 모델을 관리자 페이지에 등록
