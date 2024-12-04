# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        path = self.path

        # Определяем путь к запрашиваемым документам
        if path == "/catalog":
            file_path = "html/catalog.html"
            content_type = "text/html"
        elif path == "/categories":
            file_path = "html/category.html"
            content_type = "text/html"
        elif path == "/contact":
            file_path = "html/contacts.html"
            content_type = "text/html"
        elif path == "/main":
            file_path = "html/main.html"
            content_type = "text/html"
        elif path == "/css/bootstrap.min.css":
            file_path = "css/bootstrap.min.css"
            content_type = "text/css"
        elif path == "/js/bootstrap.bundle.min.js":
            file_path = "js/bootstrap.bundle.min.js"
            content_type = "text/javascript"
        else:
            self.send_error(404, "File Not Found: %s" % self.path)
            return

        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", content_type)  # Отправка типа данных
        self.end_headers()  # Завершение формирования заголовков ответа

        try:
            with open(file_path, "rb") as file:
                content = file.read()
                self.wfile.write(content)  # Тело ответа
        except FileNotFoundError:
            self.send_error(404, "File Not Found: %s" % file_path)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер
        pass

    webServer.server_close()
    print("Server stopped.")