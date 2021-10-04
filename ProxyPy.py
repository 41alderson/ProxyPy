import requests
from bs4 import BeautifulSoup
from time import sleep
import os

user_agent = ["Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"]
url_list_https = "https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
url_list_socks4 = "https://api.proxyscrape.com?request=getproxies&proxytype=socks4&timeout=10000&country=all"
url_list_socks5 = "https://api.proxyscrape.com?request=getproxies&proxytype=socks5&timeout=10000&country=all"


class scrape_proxy:

    @staticmethod
    def http():
        sleep(2)
        print('\n\nStarting Scraping Http/Https Proxies....')

        os.system('type NUL > ProxyPy_http.txt') #linux users use os.system('touch ProxyPy_http.txt')
        r = requests.get(url_list_https)

        with open('ProxyPy_http.txt', 'wb+') as f:
            f.write(r.content)
            f.close()
        sleep(2)

        url2 = 'https://www.proxy-list.download/api/v1/get?type=https'
        url1 = 'https://www.proxy-list.download/api/v1/get?type=http'
        l = requests.get(url2)
        ll = requests.get(url1)
        with open('ProxyPy_http.txt', 'ab+') as w:
            w.write(l.content)
            w.write(ll.content)
            w.close()

        urll = 'https://www.proxy-daily.com/'
        r = requests.get(urll).text
        soup = BeautifulSoup(r, features='html.parser')
        k = soup.find('div', {'class': 'centeredProxyList freeProxyStyle'})
        rep = k.get_text()
        with open('ProxyPy_http.txt', 'a') as ww:
            ww.writelines(rep)
            ww.close()

        print('Leeching Done Successfully')
        sleep(2)

        print('Removing Duplicates...')

        sleep(1)

        with open('ProxyPy_http.txt', 'r') as f:
            print('Total Http/Https Proxies Available: ', len(f.readlines()))

    @staticmethod
    def socks4():
        sleep(2)
        print('\n\nStarting Scraping Socks4 Proxies...')

        os.system('type NUL > ProxyPy_socks4.txt') #linux users use os.system('touch ProxyPy_socks4.txt')

        r = requests.get(url_list_socks4)

        with open('ProxyPy_socks4.txt', 'wb+') as f:
            f.write(r.content)
            f.close()

        url = 'https://www.proxy-list.download/api/v1/get?type=socks4'
        rr = requests.get(url)

        with open('ProxyPy_socks4.txt', 'ab+') as ff:
            ff.write(rr.content)
            ff.close()

        sleep(2)
        
        print('Removing Duplicates Please Wait')
        sleep(2)

        with open('ProxyPy_socks4.txt', 'r') as f:
            print('Total Socks4 Proxies Available: ', len(f.readlines()))

    @staticmethod
    def socks5():
        sleep(2)
        print('\n\nStarting Scraping Socks5 Proxies')

        os.system('type NUL > ProxyPy_socks5.txt') #linux users use os.system('touch ProxyPy_socks5.txt')
        r = requests.get(url_list_socks5)

        with open('ProxyPy_socks5.txt', 'wb+') as f:
            f.write(r.content)
            f.close()

        url = 'https://www.proxy-list.download/api/v1/get?type=socks5'
        rr = requests.get(url)

        with open('ProxyPy_socks5.txt', 'ab+') as ff:
            ff.write(rr.content)
            ff.close()

        sleep(2)

        print('Removing Duplicates Please Wait')
        sleep(2)

        with open('ProxyPy_socks5.txt', 'r') as f:
            print('Total Socks5 Proxies Available: ', len(f.readlines()))

    @staticmethod
    def get_all():
        scrape_proxy.http()
        scrape_proxy.socks4()
        scrape_proxy.socks5()


def main():
    print('''
    \n\t\tMENU
    1.Get Http/Https Proxies.
    2.Get Socks4 Proxies.
    3.Get Socks5 Proxies.
    4.Get All Proxies At Once.
    [All Are Saved In Different Files]
    5.Exit.
    ''')

    opt = input('Enter Your Choice: ')

    if opt == '1':
        scrape_proxy.http()
        sleep(1)
        input('\nPress Enter To Continue...')
        sleep(1)
        print('\nReturning To Main Menu..')
        sleep(1)
        return main()

    elif opt == '2':
        scrape_proxy.socks4()
        sleep(1)
        input('\nPress Enter To Continue...')
        sleep(1)
        print('\nReturning To Main Menu..')
        sleep(1)
        return main()

    elif opt == '3':
        scrape_proxy.socks5()
        sleep(1)
        input('\nPress Enter To Continue...')
        sleep(1)
        print('\nReturning To Main Menu..')
        sleep(1)
        return main()

    elif opt == '4':
        scrape_proxy.get_all()
        sleep(1)
        input('\nPress Enter To Continue...')
        sleep(1)
        print('\nReturning To Main Menu..')
        sleep(1)
        return main()

    elif opt == '5':
        print('\nSorry To See You Go...\n')
        print('Hope You Will Return To Me Again.')
        sleep(2)
        exit(0)

    else:
        print('Unknown Option...\nPlease Retry....')
        sleep(1.5)
        return main()


if __name__ == '__main__':
    print('''
        
        ______                        ______       
        | ___ \                       | ___ \      
        | |_/ /_ __  ___ __  __ _   _ | |_/ /_   _ 
        |  __/| '__|/ _ \\ \/ /| | | ||  __/| | | |
        | |   | |  | (_) |>  < | |_| || |   | |_| |
        \_|   |_|   \___//_/\_\ \__, |\_|    \__, |
                                 __/ |        __/ |
                                |___/        |___/ 

                          A ProxyScraper By 41alderson
    ''')
    sleep(1.5)

    print('''
        \t\tAuthor:   41_alderson
        \t\tGithub:   https://github.com/41alderson/TorrentyPy
        \t\tTelegram: @destroyer41 ''')
    sleep(1.5)
    main()
