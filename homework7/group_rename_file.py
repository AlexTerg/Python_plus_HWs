# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение

import os

__all__ = ['rename_file']

def rename_file(last_filename: str, sn: int, orig_ext: str, final_ext: str, rng: list[int]) -> None:
    cnt = 1
    for file in os.listdir('./'):
        if file.endswith(orig_ext):
            start, end = rng
            filename = file.split('.')[0][start:end] + last_filename + str(cnt).zfill(sn)
            cnt += 1
            os.rename(file, f'{filename}.{final_ext}')


if __name__ == '__main__':
    rename_file('test', 2, 'txt', 'md', [3, 6])
