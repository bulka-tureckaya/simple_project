# Микросервис на FastAPI с PostgreSQL

Этот проект представляет собой микросервис, реализованный на языке Python с использованием FastAPI и PostgreSQL. Микросервис развертывается в контейнере Docker и конфигурируется с помощью Docker Compose с использованием multi-stage builds.

## Требования

1. **Микросервис должен реализовывать минимум 4 запроса. Метод запроса (GET/POST/UPDATE/PATCH/DELETE) не важен.**
   - GET: Получение информации о ресурсе.
   - POST: Создание нового ресурса.
   - PUT: Обновление существующего ресурса.
   - DELETE: Удаление ресурса.

2. **Реализовывать микросервис можно на любом удобном языке (C++, Rust, Golang, Java, Python и т.д.).**
   - В данном проекте используется Python и FastAPI.

3. **Необходимо использовать реляционную СУБД (любую на вкус разработчика).**
   - В данном проекте используется PostgreSQL.

4. **Микросервис и СУБД должны развертываться совместно. Работать должны в контейнере. Для контейнеризации использовать Docker.**
   - Микросервис и база данных развертываются вместе с использованием Docker Compose.

5. **Для конфигурирования использоваться docker-compose. Необходимо использовать multi-stage.**
   - Проект использует Docker Compose для конфигурирования и multi-stage builds для уменьшения размера финального образа.

6. **Проект должен быть размещено в GitLab/GitHub с доступом для выполнения операции clone или fork.**
   - Проект доступен по ссылке: https://github.com/bulka-tureckaya/simple_project

7. **Для проверки работы необходимо использовать Postman.**
   - Постман используется для тестирования и проверки работы микросервиса.

8. **Требования к обработке ошибок:**
   - При некорректных данных в запросе, микросервис не должен "падать", а возвращать HTTP-код соответствующей ошибки и сопроводительное сообщение.
   - ОПЦИОНАЛЬНО. Логирование ошибок и действий в микросервисе.

## Установка и запуск

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/bulka-tureckaya/simple_project.git
cd simple_project
```

2. **Установите виртуальное окружение:**

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
3. **Запустите микросервис с помощью Docker Compose:**

```bash
docker-compose up --build
```

## Логирование

Проект использует библиотеку loguru для логирования. Логи выводятся только в консоль, без записи в файл. Это позволяет отслеживать действия и ошибки, которые происходят в приложении, непосредственно в терминале.

Логирование настроено следующим образом:

```bash
import sys
from loguru import logger

# Настройка логирования с использованием loguru для вывода в консоль
logger.add(sys.stderr, level="INFO")
```
## Postman

- Для проверки работы приложения я использую Postman

![postman](https://github.com/user-attachments/assets/9f18ac05-6636-45f3-9e14-9691fa1c9212)

- Отправка POST-запроса для создания элемента:

![post](https://github.com/user-attachments/assets/8ee92e7d-2a70-414c-a4a7-dc91d930f1e9)

![send1](https://github.com/user-attachments/assets/d3193c9f-fcca-4ff3-bd3b-304b9171eff4)

- Отправка GET-запроса для чтения элемента:

![get](https://github.com/user-attachments/assets/bdf36373-5049-4802-a7cb-d3392779c2c7)

![send2](https://github.com/user-attachments/assets/f0b40eb3-41ee-4d86-86f9-e3f715f2b992)

- Отправка PUT-запроса для обновления элемента:

![put](https://github.com/user-attachments/assets/3d111975-87f6-47f7-b43d-9437c5a30bb8)

![send3](https://github.com/user-attachments/assets/69f5c538-1c99-43a6-81f4-816029ed1db4)

- Отправка DELETE-запроса для удаления элемента:

![delete](https://github.com/user-attachments/assets/10eb8f0f-16a8-4393-851b-3a8227e7e30d)

![send4](https://github.com/user-attachments/assets/22adad22-c8bb-41be-bc34-d1d593faa273)

- Отправка GET-запроса после удаления элемента:

![get2](https://github.com/user-attachments/assets/d7cd107a-90fe-4cc4-9f77-7fe4b73f4da0)

![send5](https://github.com/user-attachments/assets/d309492a-31e1-4db3-b269-efcb2ec21029)
