from dataclasses import dataclass


@dataclass
class NewsItemModel:
    serie_name: str | None
    url_volume: str | None
    numero_volume: str | None
    is_sponsor: bool | None