#!/usr/bin/python
# -*- coding: utf-8 -*-

import webappmulti
import random


class aleat(webappmulti.app):
    def process(self, parsedRequest):
        newURL = str(random.randint(0, 10000))
        htmlAnswer = "<html><body><p>Hola. <a href=http://localhost:9999/aleat/" +\
                    newURL + ">Dame otra</a></p></body></html>"
        return ("200 OK", htmlAnswer)

if __name__ == '__main__':
    aleat = Aleat("localhost", 9999)
