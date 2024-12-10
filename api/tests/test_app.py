import pytest
from api.app import app, meals_collection, cart_collection, orders_collection

@pytest.fixture(autouse=True)
def setup_and_teardown():
    try:
        meals_collection.delete_many({})
        cart_collection.delete_many({})
        orders_collection.delete_many({})
    except Exception as e:
        print(f"Error during setup: {e}")

def test_menu_page():
    client = app.test_client()
    response = client.get("/menu")
    assert response.status_code == 200

def test_cart_page():
    client = app.test_client()
    response = client.get("/cart")
    assert response.status_code == 200

def test_place_order_page():
    client = app.test_client()
    response = client.get("/place-order")
    assert response.status_code == 200
