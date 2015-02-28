#!/usr/bin/python
# -*- coding: utf-8 -*-

import webappmulti
import aleat
import suma


class holaApp(webappmulti.app):

    def process(self, parsed):
        return("200 OK", "<html><body><p>Hola</p></body></html>")


class adiosApp(webappmulti.app):

    def process(self, parsed):
        return("220 OK", "<html><body><p>Adios</p></body></html>")

if __name__ == "__main__":
    hola = holaApp()
    adios = adiosApp()
    aleat = aleat.aleat()
    suma = suma.mySumApp()
    apps = {"/hola": hola, "/adios": adios, "/aleat": aleat, "/suma": suma}
    try:
        testWebApp = webappmulti.webApp("localhost", 9999, apps)
    except KeyboardInterrupt:
        print "Key board interrupt detected."
