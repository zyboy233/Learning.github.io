from django import  forms
from  django.core.mail import  send_mail
from blog.models import Comment
#django 使用两个类来创建表单
#forms.Form 用于生成标准表单
#forms.ModelForm 用于从模型中生成表单

class CommentFrom(forms.ModelForm):
        class Meta:
            model=Comment
            fields=("name","email","body")
            # exclude 属性指定需要排除的字段
            # exclude=("creater")



class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea)