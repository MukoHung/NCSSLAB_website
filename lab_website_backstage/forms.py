from django import forms
from django.contrib.auth.models import Group, User, Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from lab_website.models import News, TechReport, ObserReport
from lab_website_backstage.models import MailRecipient
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm, TextInput, Textarea, FileInput

class NewsForm(ModelForm):        # 自訂表單定義
  class Meta:                     # 表單元類別
    model = News                  # 指定參考的資料模型
    fields = '__all__'            # 顯示*所有*欄位
    widgets = {
      'subject': TextInput(attrs={'class': 'form-control'}),
      'content': Textarea(attrs={'class': 'form-control'}),
      'file': FileInput(attrs={'class': 'form-control', 'multiple': True}),
    }

class TechForm(ModelForm):
  class Meta:
    model = TechReport
    fields = '__all__'
    widgets = {
      'subject': TextInput(attrs={'class': 'form-control'}),
      'content': Textarea(attrs={'class': 'form-control'}),
      'img': FileInput(attrs={'class': 'form-control'}),
      'file': FileInput(attrs={'class': 'form-control', 'multiple': True}),
    }

class ObserForm(ModelForm):
  class Meta:
    model = ObserReport
    fields = '__all__'
    widgets = {
      'subject': TextInput(attrs={'class': 'form-control'}),
      'content': Textarea(attrs={'class': 'form-control'}),
      'img': FileInput(attrs={'class': 'form-control'}),
      'file': FileInput(attrs={'class': 'form-control', 'multiple': True}),
    }

class MailForm(ModelForm):
  class Meta:
    model = MailRecipient
    fields = '__all__'
    widgets = {
      'email': TextInput(attrs={'class': 'form-control'}),
    }
    
class UserUpdateForm(forms.ModelForm):
  groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),
                         widget=FilteredSelectMultiple(Group._meta.verbose_name_plural, False))
  class Meta:
        model = User
        fields = ['username', 'groups']
    
class UserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']

class GroupRegisterForm(forms.ModelForm): 
  permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(),
                         widget=FilteredSelectMultiple(Permission._meta.verbose_name_plural, False))
  class Meta:
    model = Group
    fields = ['name','permissions']

class GroupUpdateForm(forms.ModelForm):
  permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(),
                         widget=FilteredSelectMultiple(Permission._meta.verbose_name_plural, False))
  class Meta:
    model = Group
    fields = ['name', 'permissions']
