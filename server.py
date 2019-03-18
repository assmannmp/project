import sys,os
import string,cgi,time
import requests
import json
import responder
from http.server import BaseHTTPRequestHandler,HTTPServer,SimpleHTTPRequestHandler


class http(BaseHTTPRequestHandler):

    def do_GET(self):
        total=""
        try:
            if(self.path=='/'):
                return
            else:
                consult = self.path.split('/')
                number = int(consult[1])
                if(type(number) == int):
                    if(number<0):
                        total += "menos "
                        number = number*-1
                    if(number):
                        number1 = int(number/10000)
                        number2 = int((number%10000)/1000)
                        number3 = int(((number%10000)%1000)/100)
                        number4 = int((((number%10000)%1000)%100)/10)
                        number5 = int(((((number%10000)%1000)%100)%10))
                        if(number1!=0):
                            if (number1 == 1 ):
                                total +="dez "
                            elif (number1 == 2):
                                total += "vinte "
                            elif (number1 == 3):
                                total += "trinta "
                            elif (number1 == 4):
                                total += "quarenta "
                            elif (number1 == 5):
                                total += "cinquenta "
                            elif (number1 == 6):
                                total += "sessenta "
                            elif (number1 == 7):
                                total += "setenta "
                            elif (number1 == 8):
                                total += "oitenta "
                            elif (number1 == 9):
                                total += "noventa "
                            total += "e "

                        if(number2!=0):
                            if (number2 == 1 ):
                                total +="um "
                            elif (number2 == 2):
                                total += "dois "
                            elif (number2 == 3):
                                total += "três "
                            elif (number2 == 4):
                                total += "quatro "
                            elif (number2 == 5):
                                total += "cinco "
                            elif (number2 == 6):
                                total += "seis "
                            elif (number2 == 7):
                                total += "sete "
                            elif (number2 == 8):
                                total += "oito "
                            elif (number2 == 9):
                                total += "nove "
                            total += "e "

                        if (number1 != 0 or number2!=0):
                            total+="mil "

                        if (number3 != 0):
                            if (number3 == 1):
                                total += "cem "
                            elif (number3 == 2):
                                total += "duzentos "
                            elif (number3 == 3):
                                total += "trezentos "
                            elif (number3 == 4):
                                total += "quatrocentos "
                            elif (number3 == 5):
                                total += "quinhentos "
                            elif (number3 == 6):
                                total += "seiscentos "
                            elif (number3 == 7):
                                total += "setecentos "
                            elif (number3 == 8):
                                total += "oitocentos "
                            elif (number3 == 9):
                                total += "novecentos "
                            total += "e "

                        if (number4 != 0):
                            if (number4 == 1):
                                if (number5 == 0):
                                    total += "dez"
                                elif(number5 == 1):
                                    total += "onze"
                                elif (number5 == 2):
                                    total += "doze"
                                elif (number5 == 3):
                                    total += "treze"
                                elif (number5 == 4):
                                    total += "quatorze"
                                elif (number5 == 5):
                                    total += "quinze"
                                elif (number5 == 6):
                                    total += "dezesseis"
                                elif (number5 == 7):
                                    total += "dezessete"
                                elif (number5 == 8):
                                    total += "dezoito"
                                elif (number5 == 9):
                                    total += "dezenove"
                            elif (number4 == 2):
                                total += "vinte "
                            elif (number4 == 3):
                                total += "trinta "
                            elif (number4 == 4):
                                total += "quarenta "
                            elif (number4 == 5):
                                total += "cinquenta "
                            elif (number4 == 6):
                                total += "sesenta "
                            elif (number4 == 7):
                                total += "setenta "
                            elif (number4 == 8):
                                total += "oitenta "
                            elif (number4 == 9):
                                total += "noventa "
                            total += "e "

                            if (number5 != 0 and number4 != 1):
                                if (number5== 1):
                                    total += "um"
                                elif (number5 == 2):
                                    total += "dois"
                                elif (number5 == 3):
                                    total += "tres "
                                elif (number5 == 4):
                                    total += "quatro"
                                elif (number5 == 5):
                                    total += "cinco "
                                elif (number5 == 6):
                                    total += "seis "
                                elif (number5 == 7):
                                    total += "sete"
                                elif (number5 == 8):
                                    total += "oito"
                                elif (number5 == 9):
                                    total += "nove"
                        r = {"extenso": total}
                        print(r)
                        return r
                    else:
                        r = {"extenso": total}
                        print(r)
                        return r

                else:
                    return 0

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


def main(NameVirtualHost):
    try:
        virtualhost = NameVirtualHost.split(':')
        if virtualhost[0] == "*":
            virtualhost[0] = ""

        server = HTTPServer((virtualhost[0], int(virtualhost[1])), http)
        print ('Start server HTTP IN %s' % NameVirtualHost)
        server.serve_forever()
    except KeyboardInterrupt:
        print ('Shutting down server HTTP')
        server.socket.close()


if __name__ == '__main__':
    DocumentRoot = "%s/htdocs/" % os.path.realpath(os.path.dirname(__file__))
    PORT = "8000"
    HOST = "localhost"

    try :
        main(sys.argv[1])
    except :
        main("%s:%s" % (HOST,PORT))