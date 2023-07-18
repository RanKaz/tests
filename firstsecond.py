import requests

def save_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            page_content = response.text
            with open('page.html', 'w') as file:
                file.write(page_content)
            print('Страница успешно сохранена на диск!')
        else:
            print(f'Ошибка при получении страницы. Код ответа: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при получении страницы: {str(e)}')

def save_pages(urls):
    for url in urls:
        save_page(url)

# Пример использования:
urls = ['https://bloodborne.fandom.com/ru/wiki/%D0%9A%D0%BE%D1%88%D0%BC%D0%B0%D1%80_%D0%BE%D1%85%D0%BE%D1%82%D0%BD%D0%B8%D0%BA%D0%B0']
save_pages(urls)