import datetime
from app.main import outdated_products
from unittest import mock
from unittest.mock import MagicMock
from unittest import TestCase


class TetOutdatedProduct(TestCase):
    def setUp(self) -> None:
        self.products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]

    @mock.patch("app.main.datetime")
    def test_all_products_ok(
            self,
            mocked_date: MagicMock
    ) -> None:
        mocked_date.date.today.return_value = datetime.date(2022, 1, 2)
        assert outdated_products(self.products) == []

    @mock.patch("app.main.datetime")
    def test_one_product_not_ok(
            self,
            mocked_date: MagicMock
    ) -> None:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(self.products) == ["duck"]

    @mock.patch("app.main.datetime")
    def test_all_products_not_ok(
            self,
            mocked_date: MagicMock
    ) -> None:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 11)
        assert outdated_products(self.products) == ["salmon",
                                                    "chicken",
                                                    "duck"]
