import os

if os.path.exists("./datas"):
    files = os.listdir("./datas")
    for file in files:
        if os.path.isfile(os.path.abspath("./datas/"+file)):
            os.remove(os.path.abspath("./datas/"+file))
print("删除成功")

