import os
from django.core import mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'logsite.settings'
if __name__ == '__main__':
    # 发送文本邮件
    # mail.send_mail(
    #     subject='来自Django的邮件',
    #     message='欢迎访问汪春旺的网站，本站专注于技术分享。',
    #     from_email='汪春旺<wangchunwang@dhcc.com.cn>',
    #     recipient_list=['wcwnina@foxmail.com',],
    #     fail_silently=True,
    # )

    # 发送HTML邮件
    subject='来自Django的HTML邮件'
    body='欢迎访问汪春旺的博客http://www.cnblogs.com/wcwnina/，本站专注于技术分享。'
    from_email = '汪春旺<wangchunwang@dhcc.com.cn>'
    to=['wcwnina@foxmail.com',]
    html_content='欢迎访问汪春旺的博客<a href="http://www.cnblogs.com/wcwnina/">http://www.cnblogs.com/wcwnina/</a>，本站专注于技术分享。'

    msg=mail.EmailMultiAlternatives(subject=subject,body=body,from_email=from_email,to=to)
    msg.attach_alternative(content=html_content,mimetype='text/html')
    msg.send()

