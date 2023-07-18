import requests
from PIL import Image
from io import BytesIO

def download_and_save_images(urls, output_folder):
    for url in urls:
        try:
            response = requests.get(url)
            image = Image.open(BytesIO(response.content))
            max_size = 1000
            width, height = image.size
            if width > max_size or height > max_size:
                if width > height:
                    new_width = max_size
                    new_height = int(height * (max_size / width))
                else:
                    new_height = max_size
                    new_width = int(width * (max_size / height))
                image = image.resize((new_width, new_height))
            image = image.convert("RGB")
            image.save(f"{output_folder}/{url.split('/')[-1]}.jpg")
            print(f"Изображение {url} успешно сохранено.")
        except Exception as e:
            print(f"Ошибка при сохранении изображения {url}: {str(e)}")


urls = [
    "https://avatars.mds.yandex.net/i?id=ce15322261396d28b6a52ecd7040ab860fc6212b-8209398-images-thumbs&n=13",]
output_folder = "images"
download_and_save_images(urls, output_folder)