import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    """Определение функций добавления опции командной строки для pytest"""
    parser.addoption('--browser', action='store', default='firefox',  # Опция --browser для выбора браузера
                     help="Выберите браузер: chrome or firefox")

    parser.addoption('--language', action='store', default='ru',  # Опция --language для выбора языка пользователя
                     help="Выберите язык пользователя: ru, en, fr и т.д.")


@pytest.fixture(scope="session")
def browser(request):
    """Определение функций которые будет инициализировать браузер перед выполнением тестов"""
    browser_name = request.config.getoption("browser")  # Получение значения опции --browser из командной строки
    user_language = request.config.getoption("language")  # Получение значения опции --language из командной строки

    if browser_name == "chrome":
        print("\nЗапуск chrome browser для теста..")
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # Установка языка
        browser = webdriver.Chrome(options=options)  # Инициализация браузера Chrome с заданными опциями

    elif browser_name == "firefox":
        print("\nЗапуск firefox browser для теста..")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)  # Установка языка
        browser = webdriver.Firefox(options=options)  # Инициализация браузера Firefox с заданными опциями

    else:
        raise pytest.UsageError("--browser должно быть chrome или firefox")  # Исключение, если некорректный браузер

    yield browser
    print("\nБраузер закрыт..")
    browser.quit()
