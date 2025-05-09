from page_factory.component import Component


class Checkbox(Component):
    @property
    def type_of(self) -> str:
        return 'checkbox'

    def check(self, **kwargs) -> None:
        locator = self.get_locator(**kwargs)
        locator.check()
