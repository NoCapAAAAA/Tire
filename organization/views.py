from _cffi_backend import string
from django.shortcuts import render
from django.views.generic import FormView, UpdateView, DetailView, TemplateView
from . import models as m

class DirectorHomeView(TemplateView):
    template_name = 'director/home.html'


class DirectorOrdersView(TemplateView):
    template_name = 'director/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = m.OrderStorage.objects.all()
        return context


class DirectorUsersView(TemplateView):
    template_name = 'director/users.html'


class DirectorStuffView(TemplateView):
    template_name = 'director/stuff.html'


class DirectorClientsView(TemplateView):
    template_name = 'director/clients.html'


class DirectorStatisticsView(TemplateView):
    template_name = 'director/statistics.html'


class ManagerHomeView(TemplateView):
    template_name = 'manager/home.html'


class ManagerOrdersView(TemplateView):
    template_name = 'manager/orders.html'

from django.http import HttpResponse
from docx import *
from docx.shared import Inches
from datetime import date
from io import BytesIO
from datetime import datetime, date, time



def TestDocument(request):
    current_datetime = datetime.now()
    str_current_datetime = str(current_datetime)
    document = Document()
    docx_title= "report"+str_current_datetime+".docx"
    # ---- Cover Letter ----
    document.add_paragraph()
    document.add_paragraph("%s" % date.today().strftime('%B %d, %Y'))

    document.add_paragraph('Welcome to Tuts-Station.com!')
    document.add_paragraph('Tuts-Station Blog provides you latest Code Tutorials on PHP, Laravel, Codeigniter, JQuery, Node js, React js, Vue js, PHP, and Javascript. Mobile technologies like Android, React Native, Ionic etc.')

    document.add_paragraph()
    document.add_paragraph('Thank You!!,')
    document.add_paragraph('Tuts-Station.com')
    qs = m.OrderStorage.objects.all().order_by('pk')
    dictqs = list(qs)
    qstring = str(dictqs)

    document.add_paragraph(qstring)
    qs2 = m.OrderStorage.objects.all().order_by('pk')
    qs2count = qs2.count()
    print(qs2.__dict__)

    # Creating a table object
    table = document.add_table(rows=qs2count, cols=11)

    # Adding heading in the 1st row of the table
    table.style = 'Table Grid'
    table.cell(0, 0).text = 'Номер заказа'
    table.cell(0, 1).text = 'Клиент'
    table.cell(0, 2).text = 'Размер шины'
    table.cell(0, 3).text = 'Период хранения'
    table.cell(0, 4).text = 'Адрес сервиса'
    table.cell(0, 5).text = 'Статус заказа'
    table.cell(0, 6).text = 'Стоимость заказа'
    table.cell(0, 7).text = 'Оплачен'
    table.cell(0, 8).text = 'Дата оплаты'
    table.cell(0, 9).text = 'Создано'
    table.cell(0, 10).text = 'Обновлено'

    document.add_page_break()

    # Prepare document for download
    # -----------------------------
    f = BytesIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=' + docx_title
    response['Content-Length'] = length
    return response