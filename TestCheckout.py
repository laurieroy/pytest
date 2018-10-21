from Checkout import Checkout

def test_CanInstantiateCheckout():
    co = Checkout()

def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)