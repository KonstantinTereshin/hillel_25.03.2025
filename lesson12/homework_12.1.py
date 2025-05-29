#ДЗ 12.1. Очистити текст від html-тегів
import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt', remove_empty_lines=False):
    """
    Читає HTML-файл, видаляє всі HTML-теги і записує очищений текст у інший файл.
    
    Параметри:
    html_file (str): шлях до вхідного HTML-файлу.
    result_file (str): шлях до вихідного файлу для запису очищеного тексту (за замовчуванням 'cleaned.txt').
    remove_empty_lines (bool): якщо True, видаляє рядки без тексту (за замовчуванням False).
    """
    # 1. Зчитуємо вміст HTML-файлу
    with codecs.open(html_file, 'r', 'utf-8') as f:
        html = f.read()
    # 2. Видаляємо теги <...>
    text = re.sub(r'<[^>]*>', '', html)
    # 3. Розбиваємо на рядки
    lines = text.splitlines()
    # 4. Якщо потрібно — прибираємо порожні рядки
    if remove_empty_lines:
        cleaned_lines = [line for line in lines if line.strip()]
    else:
        cleaned_lines = lines
    # 5. Записуємо результат
    with codecs.open(result_file, 'w', 'utf-8') as f:
        for line in cleaned_lines:
            f.write(line + '\n')

if __name__ == '__main__':
    # Приклад використання:
    # 1) Просто видалити теги:
    delete_html_tags('draft.html')
    # Результат запишеться у cleaned.txt
    
    # 2) Видалити теги та порожні рядки:
    #delete_html_tags('draft.html', 'cleaned_no_empty.txt', remove_empty_lines=True)
    # Результат запишеться у cleaned_no_empty.txt