from django import forms
from .models import Inquiry, Response

from django import forms
from .models import Inquiry, Tag

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['title', 'content', 'tags']
        widgets = {
             'title': forms.TextInput(attrs={}), 
            'tags': forms.CheckboxSelectMultiple,
        }
        labels = {
            'title': '相談タイトル',
            'content': '相談内容',
            'tags': '関連するタグを選択してください',
        }
    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags is None or tags == "":
            return []  # 空リストを返してエラーを防ぐ
        return tags

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['content']
        labels = {
            'content': '',  # ラベルを空にすることで表示されなくなります
        }