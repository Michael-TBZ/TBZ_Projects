# Split domain from the rest of a URL

from urllib.parse import urlsplit


def get_domain(url):
    net_location = urlsplit(url)[1]
    return '.'.join(net_location.rsplit('.', 2)[-2:])


def main(url):
    if get_domain(url) == '':
        print(get_domain('https://' + url))
    else:
        print(get_domain(url))


url = 'http://abc.nl/adwawd'
main()
