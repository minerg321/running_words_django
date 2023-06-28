
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def make_video(text):
  width, height = 100, 100
  background = (0, 0, 0)
  text_color = (255, 255, 255)
  font_size = 24

  # Загружаем шрифт
  font = ImageFont.truetype("./Roboto-Regular.ttf", font_size)

  # Рассчитываем размер текста и начальное положение
  text_size = font.getbbox(text)
  text_width, text_height = text_size[2] - text_size[0], text_size[3] - text_size[1]
  x, y = width, (height - text_height) // 2

  # Создаем видео-писатель
  fourcc = cv2.VideoWriter_fourcc(*'mp4v') # или используйте 'XVID'
  out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (width, height))

  for _ in range(int(3 * 30)): # Длительность видео 3 секунды при 30 fps
    # Создаем новый пустой кадр
    img = Image.new('RGB', (width, height), color=background)
    d = ImageDraw.Draw(img)

    # Рисуем текст на текущем положении
    d.text((x, y), text, fill=text_color, font=font)

    # Преобразуем изображение PIL в изображение OpenCV
    frame = np.array(img)

    # Сдвигаем текст влево
    x -= 5
    if x + text_width < 0:
      x = width

    # Записываем кадр в выходной файл
    out.write(frame)

  out.release()

if __name__ == '__main__':
  make_video('Загружено на google colab')