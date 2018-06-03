from django.db import models


# Create your models here.
class User(models.Model):
    # 二元元组
    gender = (
        ('male', '男'),
        ('female', '女'),
        ('unknown', '未知'),
    )
    name = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=128, unique=True)
    sex = models.CharField(max_length=16, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)  # 创建时的时间
    has_confirm=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户表'
        verbose_name_plural = '用户表'


# 邮箱验证码
class ConfirmString(models.Model):
    code=models.CharField(max_length=256)
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)   # 一对一
    c_time = models.DateTimeField(auto_now_add=True)  # 创建时的时间

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"

