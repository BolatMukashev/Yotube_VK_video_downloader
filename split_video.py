import subprocess

video_path = input("Путь к видео: ").strip('"')
start = input("Начало обрезки (чч:мм:сс или сс): ").strip()
end = input("Конец обрезки (чч:мм:сс или сс): ").strip()

# Формируем путь для выходного файла
dot_index = video_path.rfind('.')
output_path = video_path[:dot_index] + "_cut" + video_path[dot_index:]

command = [
    "ffmpeg",
    "-i", video_path,
    "-ss", start,
    "-to", end,
    "-c", "copy",
    output_path
]

try:
    subprocess.run(command, check=True)
    print(f"Готово! Сохранено: {output_path}")
except subprocess.CalledProcessError as e:
    print(f"Ошибка: {e}")