from playwright.sync_api import Page, expect

from page_factory.input import Input
from page_factory.button import Button
from page_factory.dropdown_list import DropdownList
from page_factory.checkbox import Checkbox



class RequestAQuoteForm:
    '''Форма request a quote.'''
    def __init__(self, page: Page) -> None:
        self.page = page

    def fill_request_a_quote_fields(self, 
                                    account_purpose_val: str, 
                                    withdrawal_option_val: str,
                                    name_val: str,
                                    email_val: str,
                                    serv_selection_val: str
                                    ):
        '''Позитивный кейс.'''
        
        self.page.wait_for_load_state()
        name = Input(self.page, 'input[placeholder="Your Name"]', 'your name')
        email = Input(self.page, ':nth-match(input[placeholder="Your Email"], 1)', 'your email')
        service_selection = DropdownList(self.page, 'select[class="form-select bg-light border-0"]', 'services list')
        account_purpose = Checkbox(self.page, f'input[value="{account_purpose_val}"]', 'account_purpose')
        withdrawal_options = Checkbox(self.page, f'input[id="{withdrawal_option_val}"]', 'withdrawal options')
        message_field = Input(self.page, 'textarea[placeholder="Message"]', 'message')
        submit = Button(self.page, 'button[class="btn btn-dark w-100 py-3"]', 'submit')
        name_inp_locator = self.page.locator('input[placeholder="Your Name"]')
        name.scroll_to()
        name.type(name_val)
        email.type(email_val)
        service_selection.select_option(serv_selection_val)
        account_purpose.check()
        withdrawal_options.check()
        message_field.type('Sample message')
        return submit, self.page, name_inp_locator
