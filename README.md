# EditMetadata


### Edit Metadata - Сайт-утилита предназначен для изменения метаданных изображений.


## Описание проекта

Имеется возможность выбрать изображение, задать для него дату, время и координаты в формате "градусы, минуты и секунды". Полученные значения устанавливаются в метаданных изображения. Добавляется водяной знак в левом нижнем углу изображения с этими значениями. И отправляет итоговое изображение на загрузку клиенту.


## Установка

Для запуска проекта испльзуется Docker.

##### 1. Клонировать репозиторий

    git clone https://github.com/andreibaliyevich/EditMetadata.git

##### 2. Перейти в папку репозитория

    cd EditMetadata

##### 3. Создать файл .env с переменными окружения в папке src

Например:

    SECRET_KEY=secret_key
    SQL_NAME=sql_name
    SQL_USER=sql_user
    SQL_PASSWORD=sql_password

##### 4. Создать файл .env с переменными окружения в папке postgres

Например:

    POSTGRES_DB=sql_name
    POSTGRES_USER=sql_user
    POSTGRES_PASSWORD=sql_password

##### 5. Создать образ

    docker-compose build

##### 6. Запустить bash в сервисе django

    docker-compose run django bash

##### 7. Применить миграции

    python manage.py migrate

##### 8. Выйти из bash

    exit

##### 9. Запустить контейнер

    docker-compose up


## Лицензия

[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)

Copyright © 2020 Andrei Baliyevich
