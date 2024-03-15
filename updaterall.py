import os
import csv
from datetime import datetime

# Папка с PDF файлами
pdf_folder = "Cabinet/lk/ALL"

# Путь к CSV файлу
csv_file = "/Users/vitaliyisitov/Documents/Frontend/Code/Cabinet/lk/updated_data.csv"
temp_csv_file = "/Users/vitaliyisitov/Documents/Frontend/Code/Cabinet/lk/temp_updated_data.csv"

# Функция для проверки существования файла в папке
def check_file_existence(pdf_filename):
    pdf_path = os.path.join(pdf_folder, pdf_filename)
    return os.path.exists(pdf_path)

# Получаем список файлов в папке PDF
pdf_files = os.listdir(pdf_folder)
with open(csv_file, mode='r', newline='', encoding='utf-8') as input_file, \
        open(temp_csv_file, mode='w', newline='', encoding='utf-8') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')

    header = next(reader)
    header[1] = "Дата"
    writer.writerow(header)

    for row in reader:
        pdf_filename = row[-1].split('/')[-1]
        pdf_path = os.path.join(pdf_folder, pdf_filename)
        if check_file_existence(pdf_filename):
            pdf_path_relative = os.path.relpath(pdf_path, os.path.dirname(csv_file))
            row[-1] = f"../{pdf_path_relative}"
            student_name, date = row[0], row[1].split()[0]  # Разбиваем строку по пробелу и берем первую часть как дату
            row[1] = datetime.strptime(date, "%d.%m.%Y").strftime("%d.%m.%Y")  # Преобразуем дату в нужный формат
        else:
            row[-1] = ""
        writer.writerow(row)

os.rename(temp_csv_file, csv_file)

print("CSV файл успешно обновлен.")
