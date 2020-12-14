import requests
import time
import re
import os


numberR = requests.get(
    'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=00095716adad9726e55519ef1c4d4ad544e029902901&itemid=16135&excludeno=146')
print(numberR.text)

if len(numberR.text) < 10:
    print(numberR.text)
else:
    number = numberR.text.split('|', 1)
    print(number[1])
requests.get(
    'http://fatpigchain.com/index.php?r=app/send-register-sms&phone=%s' % (number))
