#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random


class aleat(webapp.app):
    def process(self, parsedRequest):
        newURL = str(random.randint(0, 10000))
        htmlAnswer = "<html><body><p><a href=http://localhost:9999/aleat/"\
                     + newURL + ">Dame otra</a></p></body></html>"
        return ("200 OK", htmlAnswer)

if __name__ == '__main__':
    aleat = Aleat("localhost", 9999)
