from django import forms
from django.contrib.auth.models import User
from django.core import validators

class EditUserForm(forms.Form):
    first_name =forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام خود را وارد نمایید','class':'form-control'}),
        label="نام "
    )
    last_name =forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام خود خانوادگی را وارد نمایید','class':'form-control'}),
        label="نام خانوادگی "
    )
class LoginForm(forms.Form):
    user_name =forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد نمایید'}),
        label="نام کاربری"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا رمز عبور خود را وارد نمایید'}),
        label="رمز عبور"
    )
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام کرده است ')
        return user_name


class RegiserForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label="نام کاربری",
        validators=[
            validators.MaxLengthValidator(limit_value=20,message='تعداد کارکتر های وارد شده نمی تواند بیشتر از 20 تا باشد.')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label="ایمیل"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز عبور خود را وارد نمایید'}),
        label="رمز عبور"
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا تکرار رمز عبور خود را وارد نمایید'}),
        label="تکرار رمز عبور"
    )
    def clean_email(self):
        email =self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('کاربری قبلا با این ایمیل ثبت نام کرده است')
        return email
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        else:
            return user_name
    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password !=re_password:
            raise forms.ValidationError('کلمه های عبور با هم تطابق ندارند')
        return password
