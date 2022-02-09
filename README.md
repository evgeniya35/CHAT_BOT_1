# Отправка в Telegram уведомлений о проверке работ Devman

Программа отслеживает изменения проверок работ преподавателями Devman. Направляет в Telegram сообщения об изменениях.

## Как установить

### Окружение
Python должен быть установлен.

### Установка
Установите программу из репозитория:
```bash
git clone https://github.com/evgeniya35/CHAT_BOT_1.git

```

### Зависимости
Используйте pip для установки зависимостей:
```bash
pip install -r requirements.txt
```

Для работы необходимо поместить в файл `.env` переменные окружения:
```
DEVMAN_TOKEN={ВашДевманТокен}
TG_TOKEN={ВашТелеграмТокен}
TG_CHAT_ID={ТелеграмЧатИД}
```

## Запуск

Для запуска программы используйте командную строку:
```bash
$ python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
