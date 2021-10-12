from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from lab_website.models import News, TechReport, ObserReport
from .models import MailRecipient
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()
# Create your views here.
@csrf_exempt
@login_required
# 後台列表
def DashList(request):
    limit = 4
    news = News.objects.all().order_by('-id')
    paginator_1 = Paginator(news, limit)
    page_1 = request.GET.get('page1', 1)

    tech_report = TechReport.objects.all().order_by('-id')
    paginator_2 = Paginator(tech_report, limit)
    page_2 = request.GET.get('page2', 1)

    obser_report = ObserReport.objects.all().order_by('-id')
    paginator_3 = Paginator(obser_report, limit)
    page_3 = request.GET.get('page3', 1)

    try:
        news_list = paginator_1.page(page_1)
    except EmptyPage:
        news_list = paginator_1.page(1)
    except PageNotAnInteger:
        news_list = paginator_1.page(1)

    try:
        tech_list = paginator_2.page(page_2)
    except EmptyPage:
        tech_list = paginator_2.page(1)
    except PageNotAnInteger:
        tech_list = paginator_2.page(1)

    try:
        obser_list = paginator_3.page(page_3)
    except EmptyPage:
        obser_list = paginator_3.page(1)
    except PageNotAnInteger:
        obser_list = paginator_3.page(1)

    context = {
        'news_list': news_list,
        'tech_list': tech_list,
        'obser_list': obser_list,
    }

    return render(request, 'lab_website_backstage/back_dashboard.html', context)

#############################################################

# 公告功能列表
class BacknewsList(LoginRequiredMixin, ListView):
    model = News
    ordering = ['-id']
    paginate_by = 8
    template_name = 'lab_website_backstage/backnews_list.html'
    
    def get_context_data(self, **kwargs):
        current_url = 'news'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 單篇公告
class BacknewsDetail(DetailView):
    model = News
    template_name = 'lab_website_backstage/backnews_detail.html'

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 新增公告
class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'form/news_form.html'
    success_url = reverse_lazy('back_news')
    permission_required = (
        'lab_website.add_news',
        'lab_website.change_news',
        'lab_website.delete_news',
        'lab_website.view_news'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 修改公告
class NewsUpdate(PermissionRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'form/news_form.html'
    success_url = reverse_lazy('back_news')
    permission_required = (
        'lab_website.add_news',
        'lab_website.change_news',
        'lab_website.delete_news',
        'lab_website.view_news'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + 'update'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 刪除公告
class NewsDelete(PermissionRequiredMixin, DeleteView):
    model = News
    form_class = NewsForm
    template_name = 'form/news_confirm_delete.html'
    success_url = reverse_lazy('back_news')
    permission_required = (
        'lab_website.add_news',
        'lab_website.change_news',
        'lab_website.delete_news',
        'lab_website.view_news'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + 'delete'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

#############################################################

# 技術報告列表
class BackTechList(LoginRequiredMixin, ListView):
    model = TechReport
    ordering = ['-id']
    paginate_by = 8
    template_name = 'lab_website_backstage/back_tech_report.html'

    def get_context_data(self, **kwargs):
        current_url = 'tech-report'
        context = {
            'current_url': current_url,
        }

        return super().get_context_data(**context)

# 單篇技術報告
class BackTechDetail(DetailView):
    model = TechReport
    template_name = 'lab_website_backstage/back_tech_report_detail.html'

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 新增技術報告
class TechCreate(PermissionRequiredMixin, CreateView):
    form_class = TechForm
    template_name = 'form/techreport_form.html'
    success_url = reverse_lazy('back_tech_report')
    permission_required = (
        'lab_website.add_techreport',
        'lab_website.change_techreport',
        'lab_website.delete_techreport',
        'lab_website.view_techreport'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 修改技術報告
class TechUpdate(PermissionRequiredMixin, UpdateView):
    model = TechReport
    form_class = TechForm
    template_name = 'form/techreport_form.html'
    success_url = reverse_lazy('back_tech_report')
    permission_required = (
        'lab_website.add_techreport',
        'lab_website.change_techreport',
        'lab_website.delete_techreport',
        'lab_website.view_techreport'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + 'update'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 刪除技術報告
class TechDelete(PermissionRequiredMixin, DeleteView):
    model = TechReport
    form_class = TechForm
    template_name = 'form/techreport_confirm_delete.html'
    success_url = reverse_lazy('back_tech_report')
    permission_required = (
        'lab_website.add_techreport',
        'lab_website.change_techreport',
        'lab_website.delete_techreport',
        'lab_website.view_techreport'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + 'delete'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

#############################################################

# 觀測報告列表
class BackObserList(LoginRequiredMixin, ListView):
    model = ObserReport
    ordering = ['-id']
    paginate_by = 8
    template_name = 'lab_website_backstage/back_obser_report.html'

    def get_context_data(self, **kwargs):
        current_url = 'obser-report'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 單篇觀測報告
class BackObserDetail(DetailView):
    model = ObserReport
    template_name = 'lab_website_backstage/back_obser_report_detail.html'

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 新增觀測報告
class ObserCreate(PermissionRequiredMixin, CreateView):
    form_class = ObserForm
    template_name = 'form/obserreport_form.html'
    success_url = reverse_lazy('back_obser_report')
    permission_required = (
        'lab_website.add_obserreport',
        'lab_website.change_obserreport',
        'lab_website.delete_obserreport',
        'lab_website.view_obserreport'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 修改觀測報告
class ObserUpdate(PermissionRequiredMixin, UpdateView):
    model = ObserReport
    form_class = ObserForm
    template_name = 'form/obserreport_form.html'
    success_url = reverse_lazy('back_obser_report')
    permission_required = (
        'lab_website.add_obserreport',
        'lab_website.change_obserreport',
        'lab_website.delete_obserreport',
        'lab_website.view_obserreport'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + 'update'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 刪除觀測報告
class ObserDelete(PermissionRequiredMixin, DeleteView):
    model = ObserReport
    form_class = ObserForm
    template_name = 'form/obserreport_confirm_delete.html'
    success_url = reverse_lazy('back_obser_report')
    permission_required = (
        'lab_website.add_obserreport',
        'lab_website.change_obserreport',
        'lab_website.delete_obserreport',
        'lab_website.view_obserreport'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + 'delete'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

#############################################################
# 帳號管理
class Users(PermissionRequiredMixin,TemplateView):
    model = User
    template_name = 'lab_website_backstage/back_account.html'
    permission_required = (
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3]
        users = User.objects.all()
        result = []
        user_dict = {}
        for user in users:
            g = list(user.groups.values('name'))
            user_dict = {'name':user,'id':user.id,'group':g}
            result.append(user_dict)

        context = {
            'result': result,
            'current_url': current_url
        }
        return super().get_context_data(**context)
    

# 新增使用者
class UserCreate(PermissionRequiredMixin,CreateView):
    template_name = 'form/back_add_user.html'
    success_url = reverse_lazy('back_account')
    form_class = UserCreationForm
    permission_required = (
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user'
    )
    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url
        }
        return super().get_context_data(**context)

# 修改使用者權限
class UserUpdate(PermissionRequiredMixin,UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('back_account')
    template_name = 'form/back_update_user.html'
    permission_required = (
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user'
    )
    
    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + get_url[5]
        context = {
            'current_url': current_url
        }
        return super().get_context_data(**context)
    
# 重設使用者密碼
class UserResetPw(PermissionRequiredMixin,PasswordChangeView):
    model = User
    form_class = SetPasswordForm
    template_name = 'form/back_reset_pw.html'
    success_url = reverse_lazy('back_account')
    permission_required = (
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user'
    )
    
    def get_form_kwargs(self):
        get_url = self.request.get_full_path().split('/')
        kwargs = super().get_form_kwargs()
        kwargs['user'] = User.objects.get(username=get_url[4])
        return kwargs
    
    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + get_url[5]
        context = {
            'current_url': current_url
        }
        return super().get_context_data(**context)

# 刪除使用者
class UserDelete(PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'form/user_confirm_delete.html'
    success_url = reverse_lazy('back_account')
    permission_required =(
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user'
    )
    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + get_url[5]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

    
#############################################################
# 個人檔案
def profile(request):
    current_url = "profile"
    current_user = request.user
    user = User.objects.get(username=current_user)
    groups = user.groups.values('name')
    context = {
        'current_url': current_url,
        'groups': groups
    }
    return render(request, 'lab_website_backstage/back_profile.html', context)
    
# 使用者變更密碼
class ProfileChangePw(PasswordChangeView):
    model = User
    template_name = 'form/back_change_pw.html'
    success_url = reverse_lazy('back_account')

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

    
############################################################

# 群組管理
class Groups(PermissionRequiredMixin,TemplateView):
    model = Group
    template_name ='lab_website_backstage/back_group.html'
    permission_required =(
        'auth.add_group',
        'auth.change_group',
        'auth.delete_group',
        'auth.view_group'
    )
    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3]
        groups = Group.objects.all()
        result = []
        group_dict = {}
        for group in groups:
            perm = list(group.permissions.values('name'))
            group_dict = {
                'name':group,
                'id':group.id,
                'perm':perm
            }
            result.append(group_dict)
        context = {
            'current_url': current_url,
            'result': result,
        }
        return super().get_context_data(**context)

    
# 新增群組   
class GroupCreate(PermissionRequiredMixin,CreateView):
    model = Group
    template_name = 'form/back_add_group.html'
    form_class = GroupRegisterForm
    success_url = reverse_lazy('back_group')
    permission_required =(
        'auth.add_group',
        'auth.change_group',
        'auth.delete_group',
        'auth.view_group'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 修改群組權限
class GroupUpadte(PermissionRequiredMixin,UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('back_group')
    template_name = 'form/back_update_group.html'
    permission_required =(
        'auth.add_group',
        'auth.change_group',
        'auth.delete_group',
        'auth.view_group'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + get_url[5]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 刪除群組
class GroupDelete(PermissionRequiredMixin, DeleteView):
    model = Group
    template_name = 'form/group_confirm_delete.html'
    success_url = reverse_lazy('back_group')
    permission_required =(
        'auth.add_group',
        'auth.change_group',
        'auth.delete_group',
        'auth.view_group'
    )
    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + get_url[5]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)
    
#############################################################

# 信件設定
def back_mail(request):
    current_url = "mail-settings"
    recipients = MailRecipient.objects.all()
    context = {
        'current_url': current_url,
        'recipients': recipients,
    }
    return render(request, 'lab_website_backstage/back_mail.html', context)

# 信件設定列表
class BackMailList(PermissionRequiredMixin, ListView):
    model = MailRecipient
    paginate_by = 10
    template_name = 'lab_website_backstage/back_mail.html'
    permission_required = (
        'lab_website_backstage.add_mailrecipient',
        'lab_website_backstage.change_mailrecipient',
        'lab_website_backstage.delete_mailrecipient',
        'lab_website_backstage.view_mailrecipient'
    )

    def get_context_data(self, **kwargs):
        current_url = 'mail-settings'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 新增收件人
class AddRecipient(PermissionRequiredMixin, CreateView):
    form_class = MailForm
    template_name = 'form/back_add_recipient.html'
    success_url = reverse_lazy('back_mail')
    permission_required = (
        'lab_website_backstage.add_mailrecipient',
        'lab_website_backstage.change_mailrecipient',
        'lab_website_backstage.delete_mailrecipient',
        'lab_website_backstage.view_mailrecipient'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 刪除收件人
class DeleteRecipient(PermissionRequiredMixin, DeleteView):
    model = MailRecipient
    form_class = MailForm
    template_name = 'form/bakc_delete_recipient.html'
    success_url = reverse_lazy('back_mail')
    permission_required = (
        'lab_website_backstage.add_mailrecipient',
        'lab_website_backstage.change_mailrecipient',
        'lab_website_backstage.delete_mailrecipient',
        'lab_website_backstage.view_mailrecipient'
    )

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[3] + '/' + get_url[4] + '/' + 'delete'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)
