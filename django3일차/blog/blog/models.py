from django.db import models

#제목, 본문, 댓글, 작성자, 일시, 카테고리
class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('free', '자유'),
        ('travle', '여행'),
        ('game', '게임'),
        ('dog', '강아지'),
    )
    category = models.CharField('카테고리', max_length=15, choices=CATEGORY_CHOICES)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')

    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now=True)

    def __str__(self):
        return self.get_category_display()

    class Meta:
        verbose_name='블로그'
        verbose_name_plural = '블로그 목록'