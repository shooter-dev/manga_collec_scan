from typing import Any, List

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

from app.IHM.pages.news.news_ui_page import UiNewsPage
from app.lib.interface_page import InterfacePage
from app.models.publisher import Publisher


class NewsPage(InterfacePage):
    ui: UiNewsPage

    def page_update(self) -> Any:
        publishers = self.feature_publishers()

        self.ui.header.add_publisher_to_combo_box(publishers)

    @staticmethod
    def feature_publishers() -> List[Publisher]:
        publishers: List[Publisher] = [
            Publisher(id="bdef8c9e-7395-465d-8175-a1b985d4aa92", title="Pika", closed=False, editions_count=653,
                      no_amazon=False),
            Publisher(id="4c9547ff-2ef6-439a-80b8-ea705a385b76", title="Kana", closed=False, editions_count=569,
                      no_amazon=False),
            Publisher(id="5e961f4c-9954-452a-961f-4d3d922c370d", title="Glénat", closed=False, editions_count=504,
                      no_amazon=False),
            Publisher(id="74de7d1e-f2e9-44bb-8a5a-1fe84258c7bf", title="Ki-oon", closed=False, editions_count=340,
                      no_amazon=False),
            Publisher(id="122e0ec3-f072-4c5d-b40d-3eba4a82fe1e", title="Crunchyroll / Kazé", closed=False,
                      editions_count=312, no_amazon=False),
            Publisher(id="2f064f84-a653-48c1-b1f6-27a694bb7ec6", title="Kurokawa", closed=False, editions_count=281,
                      no_amazon=False),
            Publisher(id="764f8c5b-370b-48eb-9abc-0ca13d5459dd", title="Delcourt/Tonkam", closed=False,
                      editions_count=262, no_amazon=False)]
        return publishers