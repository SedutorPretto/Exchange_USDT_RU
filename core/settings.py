from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    bot_token: str
    admin_id: int
    seller_id: int
    buyer_id: int


@dataclass
class Settings:
    tg_bot: TgBot


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        tg_bot=TgBot(
            bot_token=env.str('TOKEN'),
            admin_id=env.int('ADMIN_ID'),
            seller_id=env.int('SELLER_ID'),
            buyer_id=env.int('BUYER_ID')
        )
    )


settings = get_settings('.env')
