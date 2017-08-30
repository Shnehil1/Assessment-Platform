from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from assignment.forms import (
    RegistrationForm,
    EditProfileForm
)
import datetime
from .models import Assignment, Assestment, Document
from .forms import DocumentForm
import time
from xlrd import open_workbook
import shutil
import smtplib, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pip
import string
import csv
from django.http import HttpResponse
import xlwt
import xlsxwriter
from xlwt import Workbook
from xlrd import open_workbook
from django.core.files.storage import FileSystemStorage
import time
import shutil
import os
import xlrd
import csv
import sys
from email import encoders
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy


@login_required
def exportcsv(request):
    # Create a workbook and add a worksheet.
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Assessment.xlsx'
    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()
    worksheet.name = "Assestment"

    columns = [
        'Name',
        'Technology',
        'Username'
    ]

    row = 0
    col = 0
    worksheet.write(row, col, columns[0])
    worksheet.write(row, col + 1, columns[1])
    worksheet.write(row, col + 2, columns[2])


    worksheet.freeze_panes(1, 0)

    users = Assestment.objects.all()
    row = 1
    col = 0
    # Iterate over the data and write it out row by row.
    for user in users:
        worksheet.write(row, col, user.name)
        worksheet.write(row, col + 1, user.technology)
        worksheet.write(row, col + 2, user.username)


        row += 1
        col = 0


    workbook.close()
    return response


@login_required
def email(request):

    doc = Document.objects.get()
    book = open_workbook('../Shnehil/media/'+str(doc.document))
    sheet = book.sheet_by_index(0)
    #print(sheet.nrows)
    for rw in range(1, sheet.nrows):
        name,email=[data.value for data in sheet.row(rw)]
        #print(email)

        fromaddr = "support@skillspeed.com"
        # print(name + " " + email + " " + course + " " + lic_no)
        toaddr = email
        msg = MIMEMultipart('alternative')
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Regarding Assessment"

        body = """\
        <html>
    		<head></head>
    		<body>
    		<p>
            Dear Student,
            <br></br>
            <br></br>
            <b>Greetings from Skillspeed!</b>
            <br></br>
            <br></br>
            <p>Your assessment has been created and assigned by the Learning & Development Manager of your Organisation.</p>
            <p>You will shortly receive the Login Credentials for your <b>Skillspeed CloudLabs</b> account.</p>
            <p>Wherein, you will get all the Assignments and Practical Datasets ready for execution.</p>
            <br></br>
            <br></br>
            <b>Happy Coding!</b>
            <br></br>
            <br></br>
            <p>Please do spread the word about our products and like us on Facebook & leave a comment with your thoughts.</p>
            <br></br>
            <div><a href="http://www.facebook.com/SkillspeedOnline"><img src="http://www.mail-signatures.com/articles/wp-content/themes/emailsignatures/images/facebook-35x35.gif"></a><a href="http://www.linkedin.com/company/skillspeed"><img src="http://www.mail-signatures.com/articles/wp-content/uploads/2014/08/linkedin.png" width="35" height="35"></a></div>
            <br></br>
            <b>Thanks & Regards,
            <br></br>
            Skillspeed Support Team
            <br></br></b>
            </p>
            </body>
        </html>
        """
        msg.attach(MIMEText(body, 'html'))

        # print(msg)
        toadd = [toaddr]
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "skillspeed")
        text = msg.as_string()
        Document.objects.all().delete()
        server.sendmail(fromaddr, toadd, text)
        server.quit()

        # shutil.rmtree('../Shnehil/media/')

    return redirect('/assignment')

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/assignment/upload/')
    else:
        form = DocumentForm()
    return render(request, 'assignment/model_form_upload.html', {
        'form': form
    })

@login_required
def index(request):
    assignment = Assignment.objects.all()

    return render(request, 'assignment/index.html', {'all_assignment': assignment})

@login_required
def past_assessments(request):
    past_assessments = Assestment.objects.all()
    date = []
    for assestment in past_assessments:
        di=str(assestment.date).split(' ')
        d=di[0]
        if d not in date:
            date.append(d)
    date.sort()
    print(date)
    args = {'past_assessments': past_assessments, 'date':date}
    return render(request, 'assignment/past_assessments.html', args )


@login_required
def save(request):
    var = request.POST.getlist('checks')
    for i in var:
        a = Assignment.objects.get(pk=i)
        b = Assestment()
        b.name = a.name
        b.technology = a.technology
        b.username = request.user
        b.save()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/assignment/upload/')
    else:
        form = DocumentForm()
    return render(request, 'assignment/model_form_upload.html', {
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/assignment')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'assignment/reg_form.html', args)

@login_required
def view_profile(request):
    args = {'user': request.user}
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/assignment/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'assignment/profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/assignment/profile')
        else:
            return  redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'assignment/change_password.html', args)


