# forms.py是django里面用来生成form表单的一个文件
# 在这个文件里面可以实现form表单的自定义
# 我们可以让这个文件作用与html文件里面
# 以达到丰富html文件的效果
# 比如  设置表单内容类型或者合法性检查
# 使用forms会自动为我们生成label标签以及input标签
# 但是form标签以及button需要自己来写

from django import forms

class SumForm(forms.Form):
    a1 = forms.IntegerField(label='num1')
    b1 = forms.IntegerField(label='num2')


