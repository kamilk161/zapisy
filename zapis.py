# coding=utf-8
import sched
import time
import config
from polaczenie import Polaczenie


def loguj_i_zapisz():
    z = Polaczenie(config.dane_do_logowania['login'], config.dane_do_logowania['password'])
    z.zapisz_na_zajecie(*config.zajecia[config.wybor[0]])
    z.zapisz_na_zajecie(*config.zajecia[config.wybor[1]])

loguj_i_zapisz()
scheduler = sched.scheduler(time.time, time.sleep)
t = time.strptime(config.task_time, '%Y-%m-%d %H:%M:%S')
print "Task zostanie uruchomiony %s" % config.task_time
t = time.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, loguj_i_zapisz, ())
scheduler.run()