#!/usr/bin/env python

import os, cgi
import urllib.request as ur
import json





pwd  = '11031985'
login = 'BestProTop'
address = 'Москва Кравченко 12'

URL  = 'http://iqdq.ru/services/IQDQ/SearchAddressDetail?addr='+ address +'&login='+login+'&pwd='+pwd

result = ur.urlopen(URL).read()


print (result)

