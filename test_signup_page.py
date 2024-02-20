import time
import pytest

from pyshadow.main import Shadow
from selenium.common import JavascriptException


class TestAllFieldsEmpty:
    url = "https://koshelek.ru/authorization/signup"

    @staticmethod
    def button_click(browser):
        shadow = Shadow(browser)
        shadow.set_implicit_wait(10)
        try:
            button_element = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > '
                'div:nth-child(2) > form > div > div.k-btn-long-button > button')
            button_element.click()

        except JavascriptException:
            pytest.fail('Элемент "button_element" не найден, тест не может быть выполнен')

    @staticmethod
    def check_alert_text(browser, element_selector, expected_text):
        shadow = Shadow(browser)
        try:
            alert_text = shadow.find_element(element_selector)

            assert alert_text.text == expected_text, "Текст сообщения ошибки не соответствует ожидаемому"

        except JavascriptException:
            pytest.fail(f'Элемент "{element_selector}" не найден, тест не может быть выполнен')

    def test_username_alert_field_empty(self, browser):
        browser.get(TestAllFieldsEmpty.url)
        self.button_click(browser)
        time.sleep(2)
        self.check_alert_text(browser,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child('
                              '2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div '
                              '> div > div > div > span',
                              'Поле не заполнено')

    def test_email_alert_field_empty(self, browser):
        browser.get(TestAllFieldsEmpty.url)
        self.button_click(browser)
        time.sleep(2)
        self.check_alert_text(browser,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child('
                              '2) > form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div '
                              '> div > div > div > span',
                              "Поле не заполнено")

    def test_password_alert_field_empty(self, browser):
        browser.get(TestAllFieldsEmpty.url)
        self.button_click(browser)
        time.sleep(2)
        self.check_alert_text(browser,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child('
                              '2) > form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details '
                              '> div > div > div > div > div > span',
                              "Поле не заполнено")
