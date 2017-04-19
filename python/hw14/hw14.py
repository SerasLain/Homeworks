import os

def countdirs(path):
    counter = 0
    for root, dirs, files in os.walk(path):
        ## считаем, что системные файлы без расширения - это файлы с нулевым расширением
        filearr = [file for file in files if file.endswith('.') == True]
        for file in filearr:
            files.pop(file)
        dictionary = {f[-1:-3]:' ' for f in files}
        if len(dictionary)+len(filearr) != len(files):
            counter +=1
    print(counter)

def main():
    countdirs('.')

main()
