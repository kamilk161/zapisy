# coding=utf-8
import re
import requests


class NieUdaloSieZalogowacException(Exception):
    pass


class Polaczenie(object):
    _session = requests.Session()

    def __init__(self, login, password):
        l = self._loguj(login, password)
        if not l:
            raise NieUdaloSieZalogowacException(u'Nie udalo sie zalogować.(Blędne dane logowania)?')

    def _loguj(self, login, password):
        data = {
            'login': login,
            'pass': password,
            'licznik': 's',
        }
        r = self._session.post('https://ps.ug.edu.pl/login.web', data=data)
        return r.url.find('studMain.web') != -1

    #niepotrzebne
    def wyklady_do_wyboru(self):
        r = self._session.get('https://ps.ug.edu.pl/wdw.web')
        wyklady = re.findall(r'zajecia[.]web[?]idZajec=(\d*)&idBloku=(\d*)', r.content)
        nazwy = re.findall(r'<td id="tdNazwa(\d*)_(\d)" style="([^"]*)">([^<]+)</td>', r.content, re.M | re.S)
        for id, nazwa in enumerate(nazwy):
            print "('%s', '%s'), #%s" % (wyklady[id][0], wyklady[id][1], nazwa[3].replace('\t', '').replace('\r\n', '').replace('\n', ''))

    def zapisz_na_zajecie(self, idZajec, idBloku):
        data_to_enroll = {
            'idZajec': idZajec,
            'idBloku': idBloku,
            'action': u'Zapisz na zajęcia'
        }

        r = self._session.post('https://ps.ug.edu.pl/zajecia.web', data=data_to_enroll)
        print r.url
        if r.status_code == 200:
            print "OK"
        else:
            print "Wystapil jakis problem"