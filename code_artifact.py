import requests
from bs4 import BeautifulSoup
import time
import random

class AdvancedScraper:
    def __init__(self):
        # Создаем сессию, чтобы сохранять куки и сессионные данные
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        })

    def fetch_data(self, url):
        try:
            # Имитируем случайную задержку, чтобы избежать блокировок
            time.sleep(random.uniform(1.0, 3.0))
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()  # Вызовет ошибку, если статус не 200
            
            return self._parse_html(response.text)
        except requests.exceptions.RequestException as e:
            return {"error": f"Ошибка соединения: {str(e)}"}

    def _parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        # Используем .get() для безопасного извлечения данных
        title_tag = soup.find('h1')
        price_tag = soup.find('span', {'class': 'price-value'})
        
        return {
            "title": title_tag.text.strip() if title_tag else "Не найдено",
            "price": price_tag.text.strip() if price_tag else "Не найдено",
            "status": "success"
        }

if __name__ == "__main__":
    scraper = AdvancedScraper()
    target_url = "https://example.com/product/123"
    
    print(f"Запуск парсинга для: {target_url}")
    result = scraper.fetch_data(target_url)
    
    if "error" in result:
        print(f"Произошла беда: {result['error']}")
    else:
        print(f"Данные получены: {result}")