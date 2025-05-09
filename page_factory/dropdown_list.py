from page_factory.component import Component


class DropdownList(Component):
    @property
    def type_of(self) -> str:
        return 'dropdown list'
    
    # def hover(self, text: str) -> None:
    #     locator = self.page.get_by_text(text)
    #     locator.hover()

    def select_option(self, option: str,  **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        # locator.scroll_into_view_if_needed()
        locator.click()
        locator.select_option(option)
