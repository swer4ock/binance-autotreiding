<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
</head>
<body>
<h1>Скрипты Торгового Бота Бинанс</h1>
<p>Этот репозиторий содержит скрипты для автоматической торговли криптовалютами с использованием Binance API.</p>

<h2>Включенные файлы</h2>
<ul>
    <li><strong>stakan.py</strong>: Основной скрипт для мониторинга стакана ордеров и осуществления сделок на основе определённых стратегий.</li>
    <li><strong>start_btcrub.py</strong>: Скрипт для запуска торговли парой BTC/RUB.</li>
    <li><strong>start_btcusdt.py</strong>: Скрипт для запуска торговли парой BTC/USDT.</li>
    <li><strong>readme.md</strong>: Этот файл README.</li>
</ul>

<h2>Требования</h2>
<p>Перед запуском скриптов на macOS необходимо установить следующие компоненты:</p>
<ul>
    <li>Python 3.x</li>
    <li><code>python-binance</code> - Библиотека для взаимодействия с Binance API</li>
    <li><code>logging</code> - Стандартный модуль логирования Python</li>
</ul>

<h2>Установка и Настройка на macOS</h2>
<ol>
    <li>Откройте терминал и клонируйте репозиторий на ваш компьютер:</li>
    <pre><code>git clone https://github.com/swer4ock/binance-autotreiding.git</code></pre>
    
    <li>Перейдите в директорию проекта:</li>
    <pre><code>cd binance-autotreiding</code></pre>

    <li>Убедитесь, что на вашем компьютере установлен Python 3.x. Если он не установлен, вы можете установить его с помощью Homebrew:</li>
    <pre><code>brew install python</code></pre>

    <li>Создайте и активируйте виртуальное окружение (рекомендуется для изоляции зависимостей):</li>
    <pre><code>
    python3 -m venv venv
    source venv/bin/activate
    </code></pre>

    <li>Установите необходимые библиотеки:</li>
    <pre><code>
    pip install python-binance
    </code></pre>

    <li>При необходимости отредактируйте настройки в скриптах, такие как API-ключи и параметры торговли.</li>

    <li>Запустите нужный скрипт с помощью следующей команды:</li>
    <pre><code>python3 stakan.py</code></pre>
    
    <li>BASE_ASSET = 'BTC' и QUOTE_ASSET = 'USDT' выбираете опционально, допустим запуск нескольких программ в паралели</li>
    <pre><code>python3 start_btcrub.py</code></pre>
    
    <p>Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной через <a href="https://t.me/Marselito1">Telegram</a>.</p>
</ol>
</body>
</html>