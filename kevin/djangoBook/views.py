'''
Created on Nov 19, 2012

@author: Kevin
'''

from django.http import HttpResponse
from django.template.context import Context
from django.template.loader import get_template
from djangoBook.models import Publisher
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('DjangoDoc/current_datetime.html')
    html = t.render(Context({'current_date': now}))
    
    p = Publisher(name='Apress',
         address='2855 Telegraph Ave.',
         city='Berkeley',
         state_province='CA',         
         country='U.S.A.',
         website='http://www.apress.com/')
    
    p.save();
    
    
    return HttpResponse(html)