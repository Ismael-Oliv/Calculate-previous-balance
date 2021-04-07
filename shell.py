import os


def InicializateDatabase():
    os.system('echo 5328Isma | sudo -S docker start 526a6a07ddb6')
    os.system('sudo docker ps -a')