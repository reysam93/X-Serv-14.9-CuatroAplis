#!/usr/bin/python
# -*- coding: utf-8 -*-

import webappmulti


class mySumApp(webappmulti.app):

    def __init__(self):
        self.first = None

    def parse(self, request, rest):
        try:
            print "rest: " + rest
            num = float(rest[1:])
        except ValueError:
            return None
        return num

    def process(self, request):
        if not request:
            return("404 Bad Request", "Only numbers")
        if self.first is None:
            self.first = request
            respond = "Primer numero = " + str(request)
        else:
            respond = str(self.first) + " + " + str(request) +\
                     " = " + str(self.first + request)
            self.first = None
        return ("200 OK", "<html><body><p>" + respond + "</p></body></html>")


if __name__ == "__main__":
    sumador = mySumApp("localhost", 9999)
