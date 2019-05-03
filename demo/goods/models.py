from django.db import models

# Create your models here.

class GoodsModel(models.Model):
    # 名字、价格、评论量、销售量、描述信息这几个字段。
    name = models.CharField(max_length=30, verbose_name='商品名称')
    price = models.FloatField(verbose_name='价格')
    critic = models.IntegerField(default=0, verbose_name='评论量')
    sale = models.IntegerField(default=0, verbose_name='销售量')
    comment = models.CharField(max_length=200, null=True, verbose_name='评论量')

    class Meta:
        db_table = 'tb_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name