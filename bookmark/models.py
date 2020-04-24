from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')  # 문자열 데이터

    def __str__(self):  # 던더 메소드, 매직 메서드
        return "이름: " + self.site_name + " / 주소: " + self.url

    # def get_absolute_url(self):
    #     return reverse('detail', args=[str(self.id)])
    #     # 'detail'이라는 url로 이동하면서, id값을 문자열로 가지고(?)

