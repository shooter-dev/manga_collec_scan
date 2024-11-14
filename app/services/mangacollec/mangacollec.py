#    _____ __                __                 
#   / ___// /_  ____  ____  / /____  _____      
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ ___/
#  ___/ / / / / /_/ / /_/ / /_/  __/ /  __          __
# /____/_/ /_/\____/\____/\__/\___/_/  / /   ____ _/ /_ 
#                                     / /   / __ `/ __ \
#                                    / /___/ /_/ / /_/ /
# -*- By Shooter Dev -*-            /_____/\__,_/_.___/
# -*- mangacollec.py -*-
# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple, Any

from .mangacollec_interface import MangaCollecInterface


class MangaCollec (MangaCollecInterface):
    def __init__(self, username: str = None, password: str = None):
        super().__init__(username=username, password=password)

    def get_v2_collection_by_username(self, user: str = None) -> Dict:
        """ """
        url = f'{self._url_api}v2/user/{user}/collection/'

        return self._req_get(url)

    def get_publisher_all_v2(self):
        """ """

        data_json = self._req_get(f'{self._url_api}v2/publishers/')
        return data_json

    def get_publisher_v2(self, id: str) -> Dict:
        """

        :param id:
        :return:
        """
        data_json = self._req_get(f'{self._url_api}v2/publishers/{id}')

        return data_json

    def get_authors_v2(self) -> Dict:
        """
        get all author V2
        :return: list[Dict] [
            {
                "id": str,
                "name": str,
                "first_name": str,
                "tasks_count": int
            }
        ]
        """

        return self._req_get(f'{self._url_api}v2/authors/')

    def get_author_v2(self, id: str) -> Dict:
        """

        :param id:
        :return:
        """
        data_json = self._req_get(f'{self._url_api}v2/authors/{id}')

        return data_json

    def get_series_all_v2(self):
        """

        :return:
        """

        data_json = self._req_get(f'{self._url_api}v2/series/')

        return data_json

    def get_serie_v2(self, id: str) -> Dict:
        """

        :param id:
        :return:
        """
        data_json = self._req_get(f'{self._url_api}v2/series/{id}')

        return data_json

    def get_edition_v2(self, id: str) -> Dict:
        """

        :param id:
        :return:
        """
        data_json = self._req_get(f'{self._url_api}v2/editions/{id}')

        return data_json

    def get_v2_planning(self, annee: str = None, month: str = None) -> Dict:
        """

        :param annee:
        :param month:
        :return:
        """

        url: str = f'{self._url_api}v2/planning'

        if annee is not None and month is not None:
            url += f'?month={annee}-{month}'

        data_json = self._req_get(url)

        return data_json

    def get_v2_volume(self, id: str) -> Dict:
        """

        :param id:
        :return:
        """
        data_json = self._req_get(f'{self._url_api}v2/volumes/{id}')

        return data_json

    def get_v2_news(self) -> Dict:
        """

        :return:
        """

        data_json = self._req_get(f'{self._url_api}v2/volumes/news')

        return data_json

    ####################################################################################################################
    ##                                                                                                                ##
    ##    V1                                                                                                          ##
    ##                                                                                                                ##
    ####################################################################################################################

    def get_v1_volume_by_id(self, id: str):
        """ """
        return self._req_get(f'{self._url_api}v1/volumes/{id}')

    def me(self):
        return self._req_get(f'{self._url_api}v1/users/me')

    def cart(self):
        return self._req_get(f'{self._url_api}v1/users/me/cart')

    def get_v1_recommendation(self):
        return self._req_get(f'{self._url_api}v1/users/me/recommendation')

    def get_jobs_all_v1(self) -> Dict:
        """ """

        return self._req_get(f'{self._url_api}v1/jobs/')

    def get_genres_all_v1(self) -> Dict:

        return self._req_get(f'{self._url_api}v1/types/')

    def get_kinds_all_v1(self) -> Dict:

        return self._req_get(f'{self._url_api}v1/kinds/')

    def get_add_possessions_multiple(self, items: List[str]):
        list_volume: List[Dict] = []
        for item in items:
            list_volume.append({
                "volume_id": item,
            })

        return self._req_post(f'{self._url_api}v1/possessions_multiple', list_volume)
