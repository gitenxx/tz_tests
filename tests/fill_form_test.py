import allure

from playwright.sync_api import sync_playwright, expect

from pages.main_page import MainPage
from settings import BASE_URL

class TestFillTheForm:
    '''Тесты заполнения формы Request a Quote'''

    @allure.suite('Проверка формы Request a Quote')
    @allure.title('Позитивный кейс')
    def test_fill_form(self,
                        main_page: MainPage
                        ):
        '''Позитивный кейс'''
        with allure.step('Открыть главную страницу'):
            main_page.visit(BASE_URL)
        with allure.step('Заполнить форму'):
            submit = main_page.request_a_quote.fill_request_a_quote_fields(account_purpose_val='Business',
                                                                withdrawal_option_val='withdrawCash',
                                                                name_val='name Name',
                                                                email_val='test@test.test',
                                                                serv_selection_val='C Service')
            with submit[1].expect_request('https://example.com/api/subscribe') as req_info:
                submit[0].click()
            assert req_info.value.method == 'POST'

                    # Тут должно было быть чо-то типа:
                    # with submit[1].expect_response('https://example.com/api/subscribe') as respose_data:
                    #     submit[0].click()
                    # assert respose_data.value.status == '200'
                    # но из-за отсутствия имплементации CORS/пятисотки ответ приходит без урл, поэтому на него не сослаться 
                    # и код не посмотреть.
                    # Статус бы параметризировался в файле тестов, как и остальные значения.
                    
    @allure.suite('Проверка формы Request a Quote')
    @allure.title('Негативный кейс, не заполнено поле Your Name')
    def test_fill_form_negative(self,
                               main_page: MainPage
                               ):
        '''Негативный кейс, не заполнено одно из обязаельных полей (Your Name)'''
        with allure.step('Открыть главную страницу'):
            main_page.visit(BASE_URL)
        with allure.step('Заполнить форму'):
            input_name = main_page.request_a_quote.fill_request_a_quote_fields(account_purpose_val='Business',
                                                                withdrawal_option_val='withdrawCash',
                                                                name_val='',
                                                                email_val='test@test.test',
                                                                serv_selection_val='C Service',
                                                                )
            expect(input_name[2]).not_to_have_class('form-control bg-light border-0 is-valid')