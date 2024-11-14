import json
from abc import abstractclassmethod, abstractmethod
from http import HTTPStatus
import os
import time
from typing import Dict

import dotenv
import requests

@abstractmethod
class MangaCollecInterface():
    __version__ = '2.0.0'
    _url_api = 'https://api.mangacollec.com/'

    __client_id = "38fee110b53a75af6cc72f6fb66fa504fc6241e566788f4b2f5b21c25ba2fefb"
    __client_secret = "060658630f7d199c19ab1cf34ed4e50935c748267e318a24e048d6ab45871da2"

    headers = {}

    __username = None
    __password = None

    access_token = None
    refresh_token = None

    star_token_time = 0
    expiration_time = 60 * 2 # 2H

    def __init__(self, username: str = None, password: str = None):
        dotenv.load_dotenv()

        self.star_token_time = time.time()

        self.__init_identifiant(password, username)

        self.__init_header()

        self.__get_access_token()

    def __init_identifiant(self, password, username):
        if self.__is_client_env:
            self._username = os.environ['MANGACOLLEC_USERNAME']
            self._password = os.environ['MANGACOLLEC_PASSWORD']
        else:
            self.__username = username
            self.__password = password

    @property
    def __is_client_env(self) -> bool:
        if os.environ['MANGACOLLEC_USERNAME'] and os.environ['MANGACOLLEC_PASSWORD']:
            return True
        return False

    def __init_header(self):
        self.headers['Accept-encoding'] = 'gzip, deflate, br, zstd'
        self.headers['Accept-language'] = 'fr-FR,fr;q=0.9,en;q=0.8'
        self.headers['Connection'] = 'keep-alive'
        self.headers['Host'] = 'api.mangacollec.com'
        self.headers['User-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'

    def __get_access_token(self) -> None:
        payload = {
            'grant_type': 'password',
            'username': self._username,
            'password': self._password,
            'client_id': self.__client_id,
            'client_secret': self.__client_secret
        }

        response = requests.post(
            'https://api.mangacollec.com/oauth/token',
            headers=self.headers,
            data=payload
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            print(f'Error 401: {response.json().get("error") } description: {response.json().get("error_description") }')
            #TODO: raise Error conextion invalide ou usernam password invalid

        if response.status_code == HTTPStatus.OK:
            response_json = response.json()
            self.access_token = response_json['access_token']
            self.refresh_token = response_json['refresh_token']

    def __is_token_valid(self) -> bool:
        start = self.star_token_time

        end = time.time()

        temp_passed = end - start

        if temp_passed > self.expiration_time or self.access_token is None:
            return False

        return True

    def __get_token_is_not_valid(self) -> None:
        if not self.__is_token_valid():
            self.__get_access_token()

    def __req_header(self) -> Dict[str, str]:
        headers: Dict = self.headers.copy()
        headers['Accept'] = 'application/json'
        headers['Authorization'] = f'Bearer {self.access_token}'
        return headers

    def _req_get(self, url) -> Dict | None:
        """
        Get Method
        :param url: path url
        :return: Dic: valeur de retour
        """
        self.__get_token_is_not_valid()

        self.__req_header()

        response = requests.get(url, headers=self.__req_header())

        if response.status_code == HTTPStatus.OK:
            return json.loads(response.content)

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            print("permission denied")

    def _req_post(self, url, data=None) -> Dict | None:
        """
        Post Method
        :param url: path url
        :param data: param
        :return: Dic: valeur de retour
        """
        self.__get_token_is_not_valid()

        self.__req_header()

        response = requests.post(url, headers=self.__req_header(), data=data)

        if response.status_code == HTTPStatus.OK:
            return json.loads(response.content)

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            print("permission denied")
            return None
