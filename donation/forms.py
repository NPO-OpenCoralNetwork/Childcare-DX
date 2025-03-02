from django import forms
from .models import Donation
from django import forms
from .models import Donation

class GeneralDonationForm(forms.ModelForm):
    postal_code = forms.CharField(
        label='郵便番号',
        max_length=8,
        widget=forms.TextInput(attrs={
            'class': 'postal-code',
            'placeholder': '123-4567',
        })
    )
    prefecture = forms.ChoiceField(
        label='都道府県',
             choices=[
                 ('', '選択してください'),
                 ('北海道', '北海道'),
                 ('青森県', '青森県'),
                 ('岩手県', '岩手県'),
                 ('宮城県', '宮城県'),
                 ('秋田県', '秋田県'),
                 ('山形県', '山形県'),
                 ('福島県', '福島県'),
                 ('茨城県', '茨城県'),
                 ('栃木県', '栃木県'),
                 ('群馬県', '群馬県'),
                 ('埼玉県', '埼玉県'),
                 ('千葉県', '千葉県'),
                 ('東京都', '東京都'),
                 ('神奈川県', '神奈川県'),
                 ('新潟県', '新潟県'),
                 ('富山県', '富山県'),
                 ('石川県', '石川県'),
                 ('福井県', '福井県'),
                 ('山梨県', '山梨県'),
                 ('長野県', '長野県'),
                 ('岐阜県', '岐阜県'),
                 ('静岡県', '静岡県'),
                 ('愛知県', '愛知県'),
                 ('三重県', '三重県'),
                 ('滋賀県', '滋賀県'),
                 ('京都府', '京都府'),
                 ('大阪府', '大阪府'),
                 ('兵庫県', '兵庫県'),
                 ('奈良県', '奈良県'),
                 ('和歌山県', '和歌山県'),
                 ('鳥取県', '鳥取県'),
                 ('島根県', '島根県'),
                 ('岡山県', '岡山県'),
                 ('広島県', '広島県'),
                 ('山口県', '山口県'),
                 ('徳島県', '徳島県'),
                 ('香川県', '香川県'),
                 ('愛媛県', '愛媛県'),
                 ('高知県', '高知県'),
                 ('福岡県', '福岡県'),
                 ('佐賀県', '佐賀県'),
                 ('長崎県', '長崎県'),
                 ('熊本県', '熊本県'),
                 ('大分県', '大分県'),
                 ('宮崎県', '宮崎県'),
                 ('鹿児島県', '鹿児島県'),
                 ('沖縄県', '沖縄県'),
             ]
    )
    city = forms.CharField(
        label='市区町村',
        widget=forms.TextInput(attrs={
            'class': 'city',
            'placeholder': '○○市○○区',
        })
    )
    street = forms.CharField(
        label='番地・建物名',
        widget=forms.TextInput(attrs={
            'class': 'street',
            'placeholder': '○○町1-2-3 ○○マンション101',
        })
    )

    class Meta:
        model = Donation
        fields = ['amount', 'is_anonymous', 'name', 'postal_code', 'prefecture', 'city', 'street', 'phone_number']
        labels = {
            'amount': '金額',
            'is_anonymous': '匿名希望',
            'name': '名前',
            'phone_number': '電話番号',
        }
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 100:
            raise forms.ValidationError("金額は100円以上でなければなりません。")
        return amount

class MembershipDonationForm(forms.ModelForm):

    postal_code = forms.CharField(
        label='郵便番号',
        max_length=8,
        widget=forms.TextInput(attrs={
            'class': 'postal-code',
            'placeholder': '123-4567',
        })
    )
    prefecture = forms.ChoiceField(
        label='都道府県',
             choices=[
                 ('', '選択してください'),
                 ('北海道', '北海道'),
                 ('青森県', '青森県'),
                 ('岩手県', '岩手県'),
                 ('宮城県', '宮城県'),
                 ('秋田県', '秋田県'),
                 ('山形県', '山形県'),
                 ('福島県', '福島県'),
                 ('茨城県', '茨城県'),
                 ('栃木県', '栃木県'),
                 ('群馬県', '群馬県'),
                 ('埼玉県', '埼玉県'),
                 ('千葉県', '千葉県'),
                 ('東京都', '東京都'),
                 ('神奈川県', '神奈川県'),
                 ('新潟県', '新潟県'),
                 ('富山県', '富山県'),
                 ('石川県', '石川県'),
                 ('福井県', '福井県'),
                 ('山梨県', '山梨県'),
                 ('長野県', '長野県'),
                 ('岐阜県', '岐阜県'),
                 ('静岡県', '静岡県'),
                 ('愛知県', '愛知県'),
                 ('三重県', '三重県'),
                 ('滋賀県', '滋賀県'),
                 ('京都府', '京都府'),
                 ('大阪府', '大阪府'),
                 ('兵庫県', '兵庫県'),
                 ('奈良県', '奈良県'),
                 ('和歌山県', '和歌山県'),
                 ('鳥取県', '鳥取県'),
                 ('島根県', '島根県'),
                 ('岡山県', '岡山県'),
                 ('広島県', '広島県'),
                 ('山口県', '山口県'),
                 ('徳島県', '徳島県'),
                 ('香川県', '香川県'),
                 ('愛媛県', '愛媛県'),
                 ('高知県', '高知県'),
                 ('福岡県', '福岡県'),
                 ('佐賀県', '佐賀県'),
                 ('長崎県', '長崎県'),
                 ('熊本県', '熊本県'),
                 ('大分県', '大分県'),
                 ('宮崎県', '宮崎県'),
                 ('鹿児島県', '鹿児島県'),
                 ('沖縄県', '沖縄県'),
             ]
    )
    city = forms.CharField(
        label='市区町村',
        widget=forms.TextInput(attrs={
            'class': 'city',
            'placeholder': '○○市○○区',
        })
    )
    street = forms.CharField(
        label='番地・建物名',
        widget=forms.TextInput(attrs={
            'class': 'street',
            'placeholder': '○○町1-2-3 ○○マンション101',
        })
    )


    class Meta:
        model = Donation
        fields = ['amount', 'payment_frequency', 'is_anonymous', 'name', 'address', 'phone_number']
        labels = {
            'amount': '金額',
            'payment_frequency': '',
            'is_anonymous': '匿名希望',
            'name': '名前',
            'phone_number': '電話番号',
            'reason': ''
        }
