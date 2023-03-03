from provider.config.config import Config


class IBaseRepository(Config):
    def __init__(self) -> None:
        super().__init__()
        self.cursor=self.conn.cursor()
        