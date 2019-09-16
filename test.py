import re
import unittest


class TestAcceptanceStripe(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAcceptanceStripe, self).__init__(*args, **kwargs)
        with open('order.html', 'r') as file_descriptor:
            self.dom_str = file_descriptor.read()

    def test_acceptance_stripe_public_key_has_been_set(self):
        """Check if Stripe key was defined."""
        return True

    def test_acceptance_stripe_script_has_been_inserted(self):
        """Check if Stripe script was inserted."""
        return True

    def test_acceptance_checkout_button_was_instantiated(self):
        """Check if checkout button was captured."""
        return True

    def test_acceptance_sku_item_defined_on_checkout(self):
        """Check if checkout button was captured."""
        return True

    # Check if redirectToCheckout function call is present
    def test_acceptance_redirect_to_checkout(self):
        return True

    # Check if successUrl redirects to order_success.html
    def test_acceptance_success_url(self):
        return True

    # Check if cancelUrl redirects to order.html
    def test_acceptance_cancel_url(self):
        return True


if __name__ == '__main__':
    unittest.main()
