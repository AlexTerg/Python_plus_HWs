# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
from pathlib import Path
import logging
import argparse

logging.basicConfig(filename='task6.log', encoding='utf-8',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, ext, isdir, parent_dir')

def parser():
    '''
    Метод запуска функции read_dir из терминала
    '''
    parser = argparse.ArgumentParser(prog='read_dir', 
                                     description='Собиратель инфы каталога', 
                                     epilog='read_dir("path")')
    parser.add_argument('-d', '--dir', help='Укажите путь до директории', type=Path)
    arg = parser.parse_args()
    return read_dir(arg.dir)

def read_dir(path: Path):
    for file in path.iterdir():
        f = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(f)
        if file.is_dir():
            read_dir(Path(file.parent) / file.name)
            
print(parser())
                    