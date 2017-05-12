# -*- coding: utf-8 -*-

import urllib2 as request

page = request.urlopen('http://beans.itcarlow.ie/prices.html')

text = page.read().encode('utf8')

begin = text.find('ong>$') + 4 # O valor encontrado se refere ao primeiro caractere da string consultada
end = text.find('</str')

price = text[begin:end]
print('O preço encontrado foi %s' % price)