import subprocess
from urllib.parse import urlparse, unquote


# проверяет url. если вк - удаляет часть с плейлистом (с ней не скачивается) и возвращает ссылку без плейлиста. если yt - прост возвращает ссылку
def convert_playlist_to_direct(url):
    parsed = urlparse(url)
    if parsed.netloc != 'vkvideo.ru':
        return url
    path = unquote(parsed.path)
    path_parts = path.split('/')
    last_part = path_parts[-1].strip()
    if last_part.startswith('video-'):
        return f"https://vkvideo.ru/{last_part}"
    else:
        raise ValueError("Неверный URL: не заканчивается на 'video-'")

video_url = input("Введите URL видео: ")  # Вводим ссылку вручную
save_path = "C:/Users/Astana/Desktop/MyPrograms/Yotube_VK_video_downloader/result/%(title)s.%(ext)s"

command = f"yt-dlp --cookies-from-browser firefox -o \"{save_path}\" {convert_playlist_to_direct(video_url)}"

try:
    subprocess.run(command, shell=True, check=True)  # Запускаем в терминале
except subprocess.CalledProcessError as e:
    print(f"Ошибка: {e}")
