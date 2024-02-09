[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Check-Eligible)](https://git.io/typing-svg)


# Скрипт, позволяющий посмотреть статистику eligible/not eligible ваших кошельков на дроп проекта.

# Настройка и запуск

1. Установить дополнительные зависимости, выполните: `pip install -r requirements.txt`.
2. Добавили адреса кошельков в файл `data/wallets_evm.txt`.
3. Если будут добавлены прокси в `data/proxy.txt`, и их кол-во < кол-во аккаунтов, то будет работать слующая логика:
`Предположим, что у вас 4 аккаунта и 2 прокси.`

| Аккаунт   | Прокси   |
|-----------|----------|
| Аккаунт 1 | Прокси 1 |
| Аккаунт 2 | Прокси 2 |
| Аккаунт 3 | Прокси 1 |
| Аккаунт 4 | Прокси 2 |
и тд.
4. Перейти в директорию с файлом `main.py`. Запустить файл `main.py`.  
5. Выбрать(указать в консоли) соответствующий номер проекта для просмотра статистики дропа для ваших кошельков.
6. Смотреть результат. Он будет записан в results/{название проекта}.xlsx
7. При обновлении софта(к примеру: добавился нвыой проекта для проверки дропа) нужно прописать в консоли `git clone https://github.com/Irors/Check-Eligible.git` и тогда обновление автоматически установится.
8. В файлах `wallets_evm.txt` и `proxy.txt` указаны примеры ввода данных, перед запуском скрипта - удалите примеры.
---
# Доступные проекты:

 - #### **[ Alt layer ]**

 - #### **[ Orbiter Points ]**

 - #### **[ Meme( ROBOT/HUMAN ) ]**
---
**По любым вопросам писать в тг - @Irorssss**