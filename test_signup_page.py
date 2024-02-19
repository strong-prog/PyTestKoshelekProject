from pyshadow.main import Shadow
import time
import pytest

from selenium.common import JavascriptException


class TestAllFieldsEmpty:
    url = "https://koshelek.ru/authorization/signup"

    def test_username_alert_field_empty(self, browser):

        browser.get(TestAllFieldsEmpty.url)
        shadow = Shadow(browser)
        shadow.set_implicit_wait(10)
        try:
            button_element = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div.k-btn-long-button > button')
            button_element.click()

        except JavascriptException:
            pytest.fail('Элемент "button_element" не найден, тест не может быть выполнен')

        time.sleep(2)
        try:
            username_alert_text = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > div > div > span')

            assert username_alert_text.text == "Поле не заполнено", "Текст сообщения ошибки не соответствует ожидаемому"

        except JavascriptException:
            pytest.fail('Элемент "username_alert_text" не найден, тест не может быть выполнен')

    def test_email_alert_field_empty(self, browser):
        browser.get(TestAllFieldsEmpty.url)
        shadow = Shadow(browser)
        shadow.set_implicit_wait(10)
        try:
            button_element = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div.k-btn-long-button > button')
            button_element.click()

        except JavascriptException:
            pytest.fail('Элемент "button_element" не найден, тест не может быть выполнен')

        time.sleep(2)
        try:
            email_alert_text = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div > div > div > div > span')

            assert email_alert_text.text == "Поле не заполнено", "Текст сообщения ошибки не соответствует ожидаемому"

        except JavascriptException:
            pytest.fail('Элемент "email_alert_text" не найден, тест не может быть выполнен')

    def test_password_alert_field_empty(self, browser):
        browser.get(TestAllFieldsEmpty.url)
        shadow = Shadow(browser)
        shadow.set_implicit_wait(10)
        try:
            button_element = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div.k-btn-long-button > button')
            button_element.click()

        except JavascriptException:
            pytest.fail('Элемент "button_element" не найден, тест не может быть выполнен')

        time.sleep(2)
        try:
            password_alert_text = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > div > div > div > div > span')

            assert password_alert_text.text == "Поле не заполнено", "Текст сообщения ошибки не соответствует ожидаемому"

        except JavascriptException:
            pytest.fail('Элемент "password_alert_text" не найден, тест не может быть выполнен')
