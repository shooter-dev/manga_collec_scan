class Publisher:

    def __init__(self, id: str, title: str, closed: bool,editions_count: int, no_amazon: bool):
        self.id = id
        self.title = title
        self.closed = closed
        self.editions_count = editions_count
        self.no_amazon = no_amazon

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.id
