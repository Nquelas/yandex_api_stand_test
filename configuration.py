# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = "https://a20e6e2b-e6dc-4637-a679-485cf18e5253.serverhub.praktikum-services.ru"

# CREATE_USER_PATH хранит путь к API-методу для создания нового пользователя.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание пользователя.
CREATE_USER_PATH = "/api/v1/users/"
USERS_TABLE_PATH = "/api/db/resources/user_model.csv"
