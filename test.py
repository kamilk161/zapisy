# coding=utf-8
import config
from polaczenie import Polaczenie, NieUdaloSieZalogowacException

if __name__ == "__main__":
    try:
        z = Polaczenie(config.dane_do_logowania['login'], config.dane_do_logowania['password'])
        print "Logowanie udane"
    except NieUdaloSieZalogowacException as e:
        print e.message