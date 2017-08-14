import os

path = r'D:\PyProjects'
projectName = ''
folders = \
[   ['input',[
        ['src', []],
        ['doc', []]
        ] ],
    ['output', []],
    ['scenes', []],
    ['assets', [
        ['texture', []],
        ['model', [
            ['characters', []],
            ['locations', []]
        ]],
    ]]
]                                               # создание списка для подпапок

def creatFolder(path):                          # функция для соединения путей
    if not os.path.exists(path):                # для проверки сушествует ли коталог project1
        os.mkdir(path)                          # создание оснавной папки

def build(root, data):                          # Recursive Functions
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            creatFolder(path)
            build(path, d[1])

projectName = input('Enter project name: ')
if projectName:
    fullPath = os.path.join(path, projectName)
    creatFolder(fullPath)
    build(fullPath, folders)