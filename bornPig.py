import requests
import time
import re
import os


def smsSAR(invite):
    token = requests.get(
        'http://120.78.144.40:9180/service.asmx/UserLoginStr?name=121956840&psw=142536')
    print('Token OK')

    numberR = requests.get(
        'http://120.78.144.40:9180/service.asmx/GetHM2Str?token=%s&xmid=77914&sl=1&lx=0&a1=&a2=&pk=&ks=0&rj=121956840' % (token.text))
    if len(numberR.text) < 6:
        print('Get number wrong, pass: %s' % (numberR.text))
        time.sleep(5)
        return
    number = numberR.text.replace('hm=', '')
    if number[0:2] == '14':
        print('14 is come, pass: %s' % (number))
        release = requests.get(
            'http://120.78.144.40:9180/service.asmx/sfHmStr?token=%s&hm=%s' % (token.text, number))
        if release.text == '1':
            print('14 release OK')
        else:
            print(release.text)
        return
    print(number)
    sendN = requests.get(
        'http://fatpigchain.com/index.php?r=app/send-register-sms&phone=%s' % (number))

    for i in range(12):
        t = requests.get(
            'http://120.78.144.40:9180/service.asmx/GetYzm2Str?token=%s&xmid=77914&hm=%s&sf=1' % (token.text, number))
        if len(t.text) > 10:
            release = requests.get(
                'http://120.78.144.40:9180/service.asmx/sfHmStr?token=%s&hm=%s' % (token.text, number))
            if release.text == '1':
                print('Get msg release OK')
            else:
                print(release.text)
            code = re.findall(r"为(.+?),", t.text)
            print(code)
            url = 'http://fatpigchain.com/index.php?r=app/register'
            d = {'phone': number, 'code': code,
                 'password': '123456', 'invaitecode': invite}
            r = requests.post(url, data=d)
            print(r.text)
            break
        else:
            if t.text == '1':
                print('...')
            else:
                if t.text == '-3':
                    print('Waitting for release. ')
                else:
                    print('Get msg wrong, code: %s' % (t.text))
                    break
        time.sleep(5)

    release = requests.get(
        'http://120.78.144.40:9180/service.asmx/sfHmStr?token=%s&hm=%s' % (token.text, number))
    if release.text == '1':
        print('Get msg release OK')
    else:
        print(release.text)


if __name__ == '__main__':
    invite = input('输入邀请码：')
    smsSAR(invite)
