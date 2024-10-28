from locust import HttpUser, task, between

#locust -f locustfile.py --host=https://pksolena.ru
#запуск проверки

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Время ожидания между запросами от 1 до 5 секунд

    def on_start(self):

        # Устанавливаем общие заголовки для всех запросов
        self.client.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://pksolena.ru/"
        })

    @task
    def index_page(self):
        self.client.get("/")  # Запрос на главную страницу

    @task
    def services_page(self):
        self.client.get("/food-salt/")  # Запрос на страницу "Пищевая соль"

    @task
    def contact_page(self):
        self.client.get("/lizunets/")  # Запрос на страницу "Лизунцы для животных"

    @task
    def news_page(self):
        self.client.get("/galit/")  # Запрос на страницу "Галит"

    @task
    def news_page(self):
        self.client.get("/soda/")  # Запрос на страницу "Сода"

