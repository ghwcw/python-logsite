from captcha.fields import CaptchaField
from django import forms
from login import models


# Form登录表单
class UserForm(forms.Form):
    name = forms.CharField(label='用户', max_length=16, error_messages={'required': '用户名不能为空!'},
                           widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages={'required': '密码不能为空!'})
    captcha=CaptchaField(label='验证',error_messages={'required': '验证不能为空!'})


# ModelForm登录表单
class UserModelForm(forms.ModelForm):
    class Meta:
        model=models.User
        fields=('name','password',)
        labels={
            'name':'用户',
            'password':'密码',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'name': {'required': '用户名不为空'},
            'password': {'required': '密码不为空'},
        }


# Form注册表单
class RegisterForm(forms.Form):
    # 二元元组
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = forms.CharField(label="用户", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱",max_length=128, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证')


