# Руководство по запуску тестов с использованием Selenium и PyTest

## Требования

Система:

    Ubuntu/Linux

Установлены следующие компоненты:

    Python (рекомендуется версия 3.x)
    Браузер Chrome или Firefox

## Установка виртуального окружения и зависимостей

    mkdir ~/Test
    cd ~/Test
    git clone https://github.com/strong-prog/PyTestKoshelekProject
    cd PyTestKoshelekProject
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Запуск тестов

Можно запустить тесты с помощью pytest и опционально указать браузер и язык пользователя через командную строку.

    pytest --browser chrome --language en

### Доступные опции командной строки

    --browser: Выберите браузер для запуска тестов. Доступные значения: "chrome" или "firefox". По умолчанию: "firefox".
    --language: Выберите язык пользователя для отображения веб-страниц. Например, "ru", "en", "fr" и т.д. По умолчанию: "ru".



