<h1>Скрипты Торгового Бота</h1>
<p>Этот репозиторий содержит скрипты для автоматической торговли криптовалютами с использованием Binance API.</p>
<h2>Включенные файлы</h2>
<ul>
    <li><strong>stakan.py</strong>: Основной скрипт для мониторинга стакана ордеров и осуществления сделок на основе определённых стратегий.</li>
    <li><strong>start_btcrub.py</strong>: Скрипт для запуска торговли парой BTC/RUB.</li>
    <li><strong>start_btcusdt.py</strong>: Скрипт для запуска торговли парой BTC/USDT.</li>
</ul>
<h2>Требования</h2>
<p>Перед запуском скриптов на macOS необходимо установить следующие компоненты:</p>
<ul>
    <li>Python 3.x</li>
    <li><code>python-binance</code> - Библиотека для взаимодействия с Binance API</li>
    <li><code>logging</code> - Стандартный модуль логирования Python</li>
</ul>
<h2>Установка и Настройка на macOS</h2>
    Откройте терминал и клонируйте репозиторий на ваш компьютер:
    git clone https://github.com/swer4ock/binance-autotreiding.git
    
    Перейдите в директорию проекта:<br>
    cd binance-autotreiding

   Убедитесь, что на вашем компьютере установлен Python 3.x. Если он не установлен, вы можете установить его с помощью Homebrew:
  <code>brew install python</code>

    Создайте и активируйте виртуальное окружение (рекомендуется для изоляции зависимостей):
    
    python3 -m venv venv source venv/bin/activate

    Установите необходимые библиотеки:
    pip install python-binance

    При необходимости отредактируйте настройки в скриптах, такие как API-ключи и параметры торговли.

    Запустите нужный скрипт с помощью следующей команды:
    python3 stakan.py
    python3 start_btcusdt.py
    python3 start_dtrub.py
вы так же можете создать свой файл и поставить свой торговые пары подробнее в самих файлах


    
Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной через <a href="https://t.me/Marselito1">Telegram</a>
