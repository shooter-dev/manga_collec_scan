import json
import sys

from PyQt5 import QtNetwork
from PyQt5.QtCore import QSize, Qt, QUrlQuery, QUrl, QByteArray, QObject, pyqtSignal
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtWidgets import QApplication

from app.IHM.pages.window.main_windows import MainWindow
from app.lib.container import Container
from app.lib.container_interface import ContainerInterface
from app.lib.router import Router
from app.services.mangacollec.mangacollec import MangaCollec

class PublisherLoader(QObject):
    # Signal pour envoyer les données chargées
    publishers_loaded = pyqtSignal(list)

    def __init__(self, api):
        super().__init__()
        self.api = api

    def load_publishers(self):
        """Fonction qui récupère les éditeurs et émet un signal quand c'est prêt."""
        publishers = self.api.get_publisher_all_v2().get('publishers', [])
        self.publishers_loaded.emit(publishers)  # Émet le signal avec les données récupérées


def main():

    app = QApplication(sys.argv)
    add_app_options(app)
    container: ContainerInterface = Container()
    size = recupere_dimension()


    router = Router()
    api_mangacollec = MangaCollec()

    container.set(Router,router)
    container.set(MangaCollec,api_mangacollec)

    container.set_parameter('publishers', api_mangacollec.get_publisher_all_v2()['publishers'])


    window = MainWindow(size, container, router)


    window.show()
    sys.exit(app.exec_())

def add_app_options(app):
    app.setAttribute(Qt.AA_DisableHighDpiScaling, True)  # Désactiver la mise à l'échelle DPI
    app.setAttribute(Qt.AA_Use96Dpi, True)  # Forcer un DPI standard
    app.setDesktopFileName("MangaCollecScan")
    pass


def recupere_dimension() -> QSize:
    tab_dimention = sys.argv[1].split('x')
    win_width = int(tab_dimention[0])
    win_height = int(tab_dimention[1])
    return QSize(win_width, win_height)


if __name__ == '__main__':
    main()

urls = [
            "https://m.media-amazon.com/images/I/41w8Lk08tnL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt4T1Rsa05HUTRNeTFqWVROaExUUXlZelF0WWpJNFl5MHlOalZqT0RZeE0yWTNaRE1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--cd47f12184334c99194007966e01bb9fde69fe43/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/1104ae77-86bc-43f9-80d3-b14b314f8aad.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt4Tnpjd09XVTVNUzB3TXpReExUUmtNekl0T0RFNU9DMHpaakkzTlROa05XTXpPRGtHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--277b095472ee7b8f767e90b4a9577b518b387751/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/766601aa-17e5-4824-be1d-b17d9b15d92a.jpg",
            "https://m.media-amazon.com/images/I/51c+Bk7ewpL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt4TW1KaU16ZzRZUzA1TnpkbExUUTJNVFV0T1dWaFpDMWhZbVU0TXpZeFlXWXdZalVHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--ecb495cb0ff0c889bdab551f8f4d686e5273f087/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/60480fd3-1074-4376-9920-568db8bb4853.jpg",
            "https://m.media-amazon.com/images/I/51Ei3S-JsTL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxoTVRrNU1UUXpNQzFtTkRZNUxUUTFOV1l0WWpaaU55MWpNR0l5TURSa1ltTTVPRFFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--852cfed68d5b5de760b88dbb892f9aaca9e8d8cb/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/172469e4-47a3-4dca-99fc-b74f75033ea1.jpg",
            "https://m.media-amazon.com/images/I/41XWOJvg1fL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxqWlRObVpERmpPUzB4WmpZMExUUmhaVE10T0dNMk9DMWhPR0l4T1dRM01EUmxZemdHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--53c469d2391db41db7470d8e3b39042bd33fb49a/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/73f5aca3-9922-4060-bf32-3ada34090140.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt6TTJJM1pqSXhNaTB4TVRnNExUUXdNV1V0WW1Vek5TMDRPRGd4WlRjM1lUYzRaRFVHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--bbb4db206adb0248dbe36e3ff9f0cb9811b50c33/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/63f0d4df-ffcd-4e74-9a6f-06bbbd094f64.jpg",
            "https://m.media-amazon.com/images/I/51R18HtnW2L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51fGx-l8UYL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51z0iDBghML._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs0TnpGaVpEVmpNeTA0TldKa0xUUTVOV010WW1ZeU9TMDNObU0wTXpWbVltSTVOalFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--413c8b7b0152523594e835781c223ac87111dda1/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/5c01b6a9-62a0-4d48-9983-1bcfbcd4623c.jpg",
            "https://m.media-amazon.com/images/I/51anGlA9FTL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41NPt7p9DzL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/511FHgcC0YL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51KOsZtYVlL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41yYcPr+2xL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/510gIxV8qEL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxqWWpKa1lqZzBaUzAyTnpObUxUUTRaRE10WWpsa01DMWpZbUl6WW1JNVpXTTFaalVHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--d18005b155b77d764996942ed79a8c8016501b28/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/81cUcnsqeRL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/51HEcO7AyyL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41Vz8q4Z6xL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51C+GtK4C4L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41UH6tVzUjL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51AH6m74DaL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51BS9VEuMzL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51b4ykZlctL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51U9K0L9ErL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51+1r1X7kIL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/5110hUPGRpL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51A9Mg7RcOL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/513RxD9b8VL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51xVvsHeYSL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41wtJhyk7SL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41woFj3UENL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51ERCIz30wL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51XpUKJdBbL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/518DtvxvnzL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51E8LsFM7JL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51yL69CIT9L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51YMXPhE4UL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51TiFY9+sXL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41ETsNbHSLL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41GPo1I3YnL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51nkDxKc-uL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41iDgbCc6iL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt5WkdWaFpUVTJZUzFrTnpJNExUUmtZVEl0T0RCaU9DMHdPV1E0WmpreFlqWm1NeklHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--77fafb2ad7fa8f74629001275215ce4daee3080a/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/71e14729-f14a-45db-85d3-53e2eb7f068b.jpg",
            "https://m.media-amazon.com/images/I/51w0FBi4noL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/519B2vBdtUL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51Uye6nud+L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51SVjMgCpEL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51EskVcF9SL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt3TURZM01UWTJOeTA0T1RFMkxUUTJZelF0T0dFMlpTMWlObU01TURreU9UaG1OemtHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--17631329701edadb523a309b1346766dfdd15adb/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBPZ2h3Ym1jNkZISmxjMmw2WlY5MGIxOXNhVzFwZEZzSGFRTDBBV2tDOUFFPSIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--4f248cb7a1f96865b50df1fd5e45e7f4a6a9f63e/fourreau-naruto-sasuke-retsuden-tome-2-visuel-produit.png.webp",
            "https://m.media-amazon.com/images/I/51VP7GbuY9L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51mKTO5ACuL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51sYqHDoxrL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41Jd+gWS1DL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/61UmMyf-iuL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51Db+fmlb-L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51n9LPduz1L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51sRaeafpeL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/61xoaDP8ZEL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51-X00OfLUL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/61RwtnUmLvL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/512Xyt2o5NL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51pZHwengbL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt4TVdSa1l6YzJPQzFoTjJRMkxUUmhOamd0WVRFd09DMDFPREJpWVdZMU9UZ3pNRE1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--85feb8c04f1584c149bf4c869471503d0a822c32/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQzlBRnBBdlFCIiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--1c1d8c4785852ddf11da8e8f89d08629d358dfe4/GMatnpwXwAA0PFv-2.jpeg",
            "https://m.media-amazon.com/images/I/510doKDTXvL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51K0iW6EHNL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/517+Zip+LrL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51sE8DsjR1L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51zRQoEkEAL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51OOWQTEwSL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51gPqdS0zHL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/516MC433COL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsxT1RCbE1qbGhNeTFtWW1ObUxUUmpNVFV0T1Rsak9DMHlPVEUzWVRNek56UTBaR0lHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--70dd18c6f99e38db3a9336f6b4e6c628aaadddc9/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/1981dc8c-247a-405e-af8a-09cfb7445908.jpg",
            "https://m.media-amazon.com/images/I/51bWls3pVoL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt6TmpBMk1XTTFOQzFpWmpjNUxUUmxNV0l0WWpBeE9DMWlaamhtTURjMU5XVmhabVFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--4d489937cfb142453855a7ec332a294ad99ebf3c/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQzlBRnBBdlFCIiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--1c1d8c4785852ddf11da8e8f89d08629d358dfe4/e28fd74c-00a9-49ba-afff-cc6f13b65fc1.",
            "https://m.media-amazon.com/images/I/51iD7q5ILoL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs1TUdZMVlXUm1NaTB4WmpsbExUUTBZVGt0WW1WbE1pMWhNakJtTUdSbE1qY3laREFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--dddd7ec928d78f80f6bef7b634515a4a2c933caa/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQzlBRnBBdlFCIiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--1c1d8c4785852ddf11da8e8f89d08629d358dfe4/b468f03c-11bc-4a6e-9039-dd89f288c444.",
            "https://m.media-amazon.com/images/I/513Sqze5ASL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51HVTG7TBtL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/61oKSO09igL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41GugLNdyhL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt6TXpoaE4yRm1NaTFsTTJRMkxUUmxZVGt0WVRrMk9TMWxaR1l5TjJReU16RTVOR0VHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--0b187a503decbf34788c4bc18d34695c954aa9f1/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQzlBRnBBdlFCIiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--1c1d8c4785852ddf11da8e8f89d08629d358dfe4/b3680e21-656e-48f7-9485-60c17debdf91.",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt6TlRneE1HSXhaQzB3TXpFd0xUUmlPVFV0T0RJMk9DMDJObUZqT1dFelpHUmxaVE1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--7f33024d782856ae8f8996f203c800ac902098c8/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQzlBRnBBdlFCIiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--1c1d8c4785852ddf11da8e8f89d08629d358dfe4/ebdc6518-e3ad-42ce-b941-21a32b394528.",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxpT0RGak16VXdOQzFtWW1aakxUUTJNMkl0WWpsak5TMWlNRFkzTWpabE1XSm1PV1VHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--693d3eb5bf26bc8c65236b9b8a92e220c1df673b/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/c0eab1cb-8895-4903-97fa-a95213c871f8.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWswWkRVMVlqRmxOeTB3TVdNekxUUXlNMlF0T0RBMk1pMHhNMk0yWWpnMFpXWmtOMkVHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--3782f7c34d24e22fa19b9067a3a99c25fa40782a/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/58ce6f2b-cc83-4c73-bdb8-caba1ab8e62e.jpg",
            "https://m.media-amazon.com/images/I/51-Fj5FBPcL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxrTURnMVlqSXlZeTB5TTJKbExUUXdOREV0T0dVeE55MWxOMlF6TTJVMk56VTFaRE1HT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--5bc24ccab1a779222c99aa26fdb1801497770da4/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/5a8d4c8d-328a-4e4b-a778-75471d080d16.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9791041108268_1_75.jpg",
            "https://m.media-amazon.com/images/I/41W3URABq2L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51Gnyng+swL._SY642_.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9782353483273_1_75.jpg",
            "https://m.media-amazon.com/images/I/51B2ARZayPL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51vXgjf17hL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51u13jq6EEL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51K7ZZTCPjL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51r3WpHYm+L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51lAwmsVFqL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51cJFPPYFnL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51tqna7QmEL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/510DzcngZSL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51Q04ZLl7KL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/416jONAkPyL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41YcKZADVIL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51o9oWZ3i3L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51s7H5afsfL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51DZAyh2mlL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51CI7a-61ZL._SY642_.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9782384140107_1_75.jpg",
            "https://m.media-amazon.com/images/I/41ORMH0W1RL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51h8qCV13cL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51cdrFHr1pL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51S7zxH03QL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/410pWUQUAfL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51R7J01jNRL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41RigRdvS2L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51mTDhxP-pL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/61fClADgKYL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51D5o5tDJRL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41bxYMBpg5L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41jve6-u9rL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41UZR7mCBcL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51-hdH7+KTL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41WBlCtRlvL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41xMHsx8EpL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51BYDeCB8fL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51Zee9z6mkL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51qlJvHJKRL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51JhZs6hgXL._SY642_.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9782889322190_1_75.jpeg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9791041107094_1_75.jpg",
            "https://m.media-amazon.com/images/I/514zrfNrbSL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51kG47a9G5L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51IIu8Y0jpL._SY642_.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9782889324330_1_75.jpeg",
            "https://m.media-amazon.com/images/I/51YbUWGXQVL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxpTURCa05ESTBOaTAxWkdOaUxUUmpPVE10WWpKaU9TMDFOREV6WkRnMU1UUTJOV1VHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--75883f8abd28780dea075287eb0c3563411e0054/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/57f66cac-bfb8-47d4-9011-e47db2191f29.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9791041107117_1_75.jpg",
            "https://m.media-amazon.com/images/I/510gKUqTmGL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/517lRgo5-qL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41mLqphWBPL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51tXIcy2mJL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51BEeY2NKCL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxtTkRjd09EazROUzB3WWpNNExUUmhPV0l0T0RJMVl5MHpZalZoT1RNeU5UZGxNakFHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--037ca1d36d3a2623532748fda72c2c5a9435ddb8/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--7c73e8a32db9248865f33012a40f867d228b3b7c/pack-decouverte-ripper-tome-1-3.jpg.png",
            "https://m.media-amazon.com/images/I/41jR-UpVAQL._SY642_.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt5TmpKa05HSTBaUzAxT0RoakxUUmhaamN0T0dRMVppMWhZakExTnpVeVpUaGpaRGdHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--06c1fe077acf8c0745879492fb1996111c3c0828/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQzlBRnBBdlFCIiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--1c1d8c4785852ddf11da8e8f89d08629d358dfe4/ae082a85-0c73-4fc6-825b-b73fc2dfb965.jpeg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWs1WVdaaU5HTmpNUzAyTlRSakxUUTRObUV0WW1Vek1pMDVPV05tTTJRMU5UWXpPV1VHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--03145968aef15e846c0cbf159037864811e6027d/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/36386aa2-0c1b-4682-bcf3-afdc55eeaf58.jpg",
            "https://api.mangacollec.com/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWt4T1dZNE5EVXdNeTFpT1dZd0xUUm1PVGt0T1RFNE15MW1NbVJpTnpjNU5EQm1OVGtHT2daRlZBPT0iLCJleHAiOm51bGwsInB1ciI6ImJsb2JfaWQifX0=--cb975f34d7fdb42d31b4a0a160fdfc2099dfc9ed/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFMMEFXa0M5QUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--f4740ce9863997714730d7d28982d4fbc8d883df/583fffaa-3a17-4433-914d-867ad5cb6242.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9782385040352_1_75.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9791039126687_1_75.jpg",
            "https://m.media-amazon.com/images/I/51M5YetlM+L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41P47ve+fVL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51T9fsBRUZL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51znBpT54JL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51+rBe-EUoL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51gvloyclEL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51dIqqPz9aL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/412LHZTZZfL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/518q4xKPxqL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51SIMMHD9+L._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41v++sjk0oL._SY642_.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9791039128674_1_75_1.jpg",
            "https://m.media-amazon.com/images/I/511Uc9crLDL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51uVHUVzAhL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/518DdgsXiaL._SY642_.jpg",
            "https://www.bdfugue.com/media/catalog/product/9/7/9782379503719_1_75.jpg",
            "https://m.media-amazon.com/images/I/51cg9xbZvWL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/41kpY4LdrSL._SY642_.jpg",
            "https://m.media-amazon.com/images/I/51iP5R8HtHL._SY642_.jpg"
        ]