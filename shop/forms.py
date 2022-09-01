from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField

from .models import Book

User = get_user_model()


class RegisterForm(forms.ModelForm):
    """Product Register Form"""

    class Meta:
        # 利用するモデルクラスを指定
        model = Book
        # 利用するモデルのフィールドを指定
        fields = ('title', 'image', 'publisher', 'authors', 'price', 'description', 'publish_date')
    """
    password2 = forms.CharField(
        label='確認用パスワード',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '確認用パスワード'}),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フィールドの属性を書き換え
        self.fields['email'].required = True
        self.fields['email'].widget.attrs = {'placeholder': 'メールアドレス'}
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_username(self):
        value = self.cleaned_data['username']
        if len(value) < 3:
            raise forms.ValidationError(
                '%(min_length)s文字以上で入力してください', params={'min_length': 3})
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        return value

    def clean_password(self):
        value = self.cleaned_data['password']
        return value

    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("パスワードと確認用パスワードが合致しません")
        # ユニーク制約を自動でバリデーションしてほしい場合は super の clean() を明示的に呼び出す
        super().clean()
    
    """