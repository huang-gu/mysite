import os
from django.core.mail import EmailMultiAlternatives
os.environ['DJANGO_SETTINGS_MODULE'] = 'Caster.settings'
if __name__ == '__main__':
    subject,from_email,to = '来自乱古纪元的一封信','lostangelgang@163.com','201628089@qq.com'
    text_content = '荒天帝在等待，等待能够与他并肩作战的人！'
    html_content = '<p>欢迎访问<a href="http://www.lgzhou.cn" target=_blank>www.lgzhou.cn</a>，这里是周丽刚的个人网站，欢迎各位大神来访！</p>'
    msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
