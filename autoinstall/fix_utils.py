import re
import sys
p = sys.path
fin = '0'
for el in p:
    if el.find('site-packages'):
        fin = el
    else:
        pass
if fin == '0':
    print('no module named')
else:
    fin += '\\bootstrap3_datetime\\widgets.py'
data = open(fin).read()
o = open(fin, 'w')
o.write(re.sub("from django.forms.util import flatatt", "from django.forms.utils import flatatt", data))
print("Success")
o.close()
