from aiogram.fsm.state import State, StatesGroup


class FSMDealBuy(StatesGroup):
    choosing_buy = State()
    choosing_buy_terms = State()
    choosing_buy_confirm = State()
    choosing_buy_finish = State()


class FSMDealSell(StatesGroup):
    choosing_sell = State()
    choosing_sell_terms = State()
    choosing_sell_confirm = State()
    choosing_sell_finish = State()
