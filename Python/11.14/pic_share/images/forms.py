from urllib import request
from django.core.files.base import ContentFile
from django import forms
from images.models import Image
from uuslug import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extentions = ['jpg','jpeg','png']
        extention = url.rsplit('.',1)[1].lower()
        if extention not in valid_extentions:
            raise forms.ValidationError('您所给的图片地址格式不支持!')
        return url

    def save(self, commit=True):
        image = super(ImageCreateForm,self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),image_url.rsplit('.',1)[1].lower())
        # 根据url下载图片
        response = request.urlopen(image_url)
        image.image.save(image_name,ContentFile(response.read()),save=False)

        if commit:
            image.save()
        return image