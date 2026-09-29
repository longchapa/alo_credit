from app.enums import Product
from app.strategies.base import CreditPolicy
from app.strategies.card import CardPolicy
from app.strategies.phone import PhonePolicy
from app.strategies.twist import TwistPolicy


class PolicyResolver:
    def __init__(self) -> None:
        self._policies: dict[Product, CreditPolicy] = {
            Product.PHONE: PhonePolicy(),
            Product.TWIST: TwistPolicy(),
            Product.CARD: CardPolicy(),
        }

    def resolve(self, product: Product) -> CreditPolicy:
        try:
            return self._policies[product]
        except KeyError as exc:
            raise ValueError(f"Unsupported product: {product}") from exc
