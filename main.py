import subprocess

video_url = input("Введите URL видео: ")  # Вводим ссылку вручную
save_path = "C:/Users/Astana/Desktop/MyPrograms/Yotube_VK_video_downloader/result/%(title)s.%(ext)s"

command = f'"C:/Users/Astana/Desktop/MyPrograms/Yotube_VK_video_downloader/.venv/Scripts/yt-dlp.exe" -o "{save_path}" "{video_url}"'

try:
    subprocess.run(command, shell=True, check=True)  # Запускаем в терминале
except subprocess.CalledProcessError as e:
    print(f"Ошибка: {e}")
