from datetime import datetime
from django.db.models import Q
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News, TechReport, ObserReport
from lab_website_backstage.models import MailRecipient

# 顯示 New! icon 天數
icon_days = 7

# 首頁
def index(request):
    news_list = News.objects.all().order_by('-id')[:3]
    tech_report = TechReport.objects.all().order_by('-id')[:4]
    obser_report = ObserReport.objects.all().order_by('-id')[:4]
    now = datetime.now().astimezone()
    tag=[]
    for news in list(news_list):
        get_tag = str(now - news.date.astimezone()).split(' ')[0]
        if ':' in get_tag:
            tag.append(1)
        else:
            if int(get_tag) <= icon_days :
                tag.append(1)
            else:
                tag.append(0)
    news_tag = zip(news_list, tag)
    context = {
        'news_tag': news_tag,
        'tech_report': tech_report,
        'obser_report': obser_report,
    }
    return render(request, 'lab_website/index.html', context)

#############################################################

# 公告列表
def NewsList(request):
    limit = 6
    current_url = 'news'
    news = News.objects.all().order_by('-id')
    paginator = Paginator(news, limit)
    page = request.GET.get('page', 1)
    now = datetime.now().astimezone()
    tag=[]

    try:
        news_list = paginator.page(page)
    except EmptyPage:
        news_list = paginator.page(1)
    except PageNotAnInteger:
        news_list = paginator.page(1)

    for n in list(news_list):
        get_tag = str(now - n.date.astimezone()).split(' ')[0]
        if ':' in get_tag:
            tag.append(1)
        else:
            if int(get_tag) <= icon_days :
                tag.append(1)
            else:
                tag.append(0)

    news_tag = zip(news_list, tag)

    context = {
            'news_tag': news_tag,
            'news_list': news_list,
            'current_url': current_url,
    }
    return render(request, 'lab_website/news_list.html', context)

# 單篇公告
class NewsDetail(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[2] + '/' + get_url[3]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

#############################################################

# 關於
def about(request):
    current_url = "about"
    context = {
        'current_url': current_url,
    }
    return render(request, 'lab_website/about.html', context)

#############################################################

# 技術報告列表
class TechList(ListView):
    model = TechReport
    ordering = ['-id']
    paginate_by = 3
    template_name = 'lab_website/tech_report.html'

    def get_context_data(self, **kwargs):
        current_url = 'tech-report'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 單篇技術報告
class TechDetail(DetailView):
    model = TechReport
    template_name = 'lab_website/tech_report_detail.html'

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[2] + '/' + get_url[3]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 技術報告-日期查詢
def tech_select_date(request):
    current_url = "tech-report/select-date"

    if request.method == "POST":
        start_date = request.POST['start_date']+'-01'
        end_date = request.POST['end_date']+'-31'
        report = TechReport.objects.filter(date__range=[start_date, end_date]).order_by('-id')
        context = {
                'current_url': current_url,
                'report': report
            }
        return render(request, 'lab_website/tech_select_date.html', context)
    else:
        context = {
                'current_url': current_url,
            }
        return render(request, 'lab_website/tech_select_date.html', context)

# 技術報告-關鍵字查詢
def tech_keyword_research(request):
    current_url = "tech-report/keyword-research"
    
    if request.method == "POST":
        searched = request.POST['searched']
        report = TechReport.objects.filter(Q(subject__icontains=searched) | Q(content__icontains=searched)).order_by('-id')
        context = {
            'current_url': current_url,
            'report': report,
        }
        return render(request, 'lab_website/tech_keyword_research.html', context)
    else:
        context = {
            'current_url': current_url,
        }
        return render(request, 'lab_website/tech_keyword_research.html', context)

#############################################################

# 觀測報告列表
class ObserList(ListView):
    model = ObserReport
    ordering = ['-id']
    paginate_by = 3
    template_name = 'lab_website/obser_report.html'

    def get_context_data(self, **kwargs):
        current_url = 'obser-report'
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 單篇觀測報告
class ObserDetail(DetailView):
    model = ObserReport
    template_name = 'lab_website/obser_report_detail.html'

    def get_context_data(self, **kwargs):
        get_url = self.request.get_full_path().split('/')
        current_url = get_url[2] + '/' + get_url[3]
        context = {
            'current_url': current_url,
        }
        return super().get_context_data(**context)

# 觀測報告-日期查詢
def obser_select_date(request):
    current_url = "obser-report/select-date"
    if request.method == "POST":
        start_date = request.POST['start_date']+'-01'
        end_date = request.POST['end_date']+'-31'
        report = ObserReport.objects.filter(date__range=[start_date, end_date]).order_by('-id')
        context = {
                'current_url': current_url,
                'report': report
            }
        return render(request, 'lab_website/obser_select_date.html', context)
    else:
        context = {
                'current_url': current_url,
            }
        return render(request, 'lab_website/obser_select_date.html', context)

# 觀測報告-關鍵字查詢
def obser_keyword_research(request):
    current_url = "obser-report/keyword-research"

    if request.method == "POST":
        searched = request.POST['searched']
        report = ObserReport.objects.filter(Q(subject__icontains=searched) | Q(content__icontains=searched)).order_by('-id')
        context = {
            'current_url': current_url,
            'report': report,
        }
        return render(request, 'lab_website/obser_keyword_research.html', context)
    else:
        context = {
            'current_url': current_url,
        }
        return render(request, 'lab_website/obser_keyword_research.html', context)

#############################################################

# 聯絡我們
def contact(request):
    current_url = "contact"

    if request.method == "POST":
        msg_name = request.POST['msg-name']
        msg_company = request.POST['msg-company']
        msg_email = request.POST['msg-email']
        msg_phone = request.POST['msg-phone']
        msg_check = request.POST['msg-check']
        msg_other = request.POST['msg-other']
        title = '[ NCSS LAB website ] 收到來自 ' + msg_name + ' 的訊息'
        contents = f'姓名：{msg_name}\n公司：{msg_company}\nEmail：{msg_email}\n電話：{msg_phone}\n需求：{msg_check}\n其他：{msg_other}'
        recipients = list(MailRecipient.objects.values_list('email', flat=True))
        send_mail(
            title,
            contents,
            '',
            recipients,
        ) 
        
        context = {
            'current_url': current_url,
            'msg_name': msg_name,
        }
        return render(request, 'lab_website/contact.html', context)
    else:
        context = {
            'current_url': current_url,
        }
        return render(request, 'lab_website/contact.html', context)
