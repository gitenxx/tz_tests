from playwright.sync_api import expect

from page_factory.component import Component


class Input(Component):
    @property
    def type_of(self) -> str:
        return 'input'
    
    def scroll_to(self, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.scroll_into_view_if_needed()
        locator.click()

    def type(self, value: str, validate_value=False, **kwargs):

        locator = self.get_locator(**kwargs)
        locator.type(value, delay=0.8)

        if validate_value:
            self.should_have_value(value, **kwargs)

    def fill(self, value: str, validate_value=False, **kwargs):
            
        locator = self.get_locator(**kwargs)
        locator.fill(value)

        if validate_value:
            self.should_have_value(value, **kwargs)

    def should_have_value(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)