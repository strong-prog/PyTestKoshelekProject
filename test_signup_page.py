import time
import pytest

from pyshadow.main import Shadow
from selenium.common import JavascriptException


class TestAllFieldsEmpty:
    url = 'https://koshelek.ru/authorization/signup'

    @staticmethod
    def button_click(shadow):
        """Метод для нажатия на кнопку"""
        try:
            button_element = shadow.find_element('div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div.k-btn-long-button > button')
            button_element.click()

        except JavascriptException:
            pytest.fail('Элемент "button_element" не найден, тест не может быть выполнен')

    @staticmethod
    def check_alert_text(shadow, element_selector, expected_text):
        """Метод для проверки текста сообщения об ошибке"""
        try:
            alert_text = shadow.find_element(element_selector)

            assert alert_text.text == expected_text, 'Текст сообщения ошибки не соответствует ожидаемому'

        except JavascriptException:
            pytest.fail(f'Элемент "{element_selector}" не найден, тест не может быть выполнен')

    def test_username_alert_field_empty(self, browser):
        """Тест для проверки сообщения об ошибке, если поле имени пользователя пустое"""
        browser.get(TestAllFieldsEmpty.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.button_click(shadow)
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              'Поле не заполнено')

    def test_email_alert_field_empty(self, browser):
        """Тест для проверки сообщения об ошибке, если поле электронной почты пустое"""
        browser.get(TestAllFieldsEmpty.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.button_click(shadow)
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              'Поле не заполнено')

    def test_password_alert_field_empty(self, browser):
        """Тест для проверки сообщения об ошибке, если поле пароля пустое"""
        browser.get(TestAllFieldsEmpty.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.button_click(shadow)
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              'Поле не заполнено')


class TestFieldsInvalidInput:
    url = 'https://koshelek.ru/authorization/signup'

    @staticmethod
    def button_click(shadow):
        """Метод для нажатия на кнопку"""
        try:
            button_element = shadow.find_element(
                'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div.k-btn-long-button > button')
            button_element.click()

        except JavascriptException:
            pytest.fail('Элемент "button_element" не найден, тест не может быть выполнен')

    @staticmethod
    def enter_text(shadow, field_selector, text):
        """Метод для ввода текста в поле ввода"""
        try:
            input_field = shadow.find_element(field_selector)
            input_field.send_keys(text)

        except JavascriptException:
            pytest.fail(f'Элемент "{field_selector}" не найден, тест не может быть выполнен')

    @staticmethod
    def check_alert_text(shadow, field_selector, expected_text):
        """Метод для проверки текста сообщения об ошибке"""
        try:
            alert_text = shadow.find_element(field_selector)

            assert alert_text.text == expected_text, 'Текст сообщения ошибки не соответствует ожидаемому'

        except JavascriptException:
            pytest.fail(f'Элемент "{field_selector}" не найден, тест не может быть выполнен')

    def test_alert_username_field_invalid_input(self, browser):
        """Тест для проверки сообщения об ошибке при вводе некорректного имени пользователя"""
        browser.get(TestFieldsInvalidInput.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.enter_text(shadow,
                        'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-input__slot > div.v-text-field__slot > input',
                        '123')
        time.sleep(1)
        self.button_click(shadow)
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы')

    def test_alert_email_field_invalid_input(self, browser):
        """Тест для проверки сообщения об ошибке при вводе некорректного адреса электронной почты"""
        browser.get(TestFieldsInvalidInput.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.enter_text(shadow,
                        'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(2) > div > div > div.v-input__slot > div.v-text-field__slot > input',
                        '123')
        time.sleep(1)
        self.button_click(shadow)
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              ' Формат e-mail: somebody@somewhere.ru ')

    def test_alert_password_field_short_invalid_input(self, browser):
        """Тест для проверки сообщения об ошибке при вводе слишком короткого пароля"""
        browser.get(TestFieldsInvalidInput.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.enter_text(shadow,
                        'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div.v-input__slot > div.v-text-field__slot > input',
                        '123')
        time.sleep(1)
        self.button_click(shadow)
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              'Пароль должен содержать минимум 8 символов')

    def test_alert_password_field_long_invalid_input(self, browser):
        """Тест для проверки сообщения об ошибке при вводе длинного некорректного пароля"""
        browser.get(TestFieldsInvalidInput.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.enter_text(shadow,
                        'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div.v-input__slot > div.v-text-field__slot > input',
                        '1234567890')
        time.sleep(1)
        self.button_click(shadow)
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры')

    def test_alert_referral_field_invalid_input(self, browser):
        """Тест для проверки сообщения об ошибке при вводе некорректного реферального кода"""
        browser.get(TestFieldsInvalidInput.url)
        shadow = Shadow(browser)
        time.sleep(5)
        self.enter_text(shadow,
                        'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(4) > div > div > div.v-input__slot > div.v-text-field__slot > input',
                        '123')
        time.sleep(1)
        self.check_alert_text(shadow,
                              'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(4) > div > div > div.v-text-field__details > div > div > div > div > div > span',
                              'Неверный формат ссылки')
