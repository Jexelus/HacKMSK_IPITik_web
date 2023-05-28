# HacKMSK_IPITik_web
req ver python - 3.10.6

# Installation

1. Create environment
```bash
python3 -m venv env 
source /env/bin/avtivate
pip install -r req.txt
```

2. Install yolov5
```bash
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt
```

3. Move predict.py to yolov5 directory
```bash
mv predict.py yolov5/
```

4. Start server with command
```bash
env/bin/python main.py
```

# API
У нас есть route'ы для апи, но все они только для взаимодействия с мобильным приложением и недоступны обычным пользователям, так как нам важнее было выполнить задачу, на путях не стоят методы авторизации и нету общего или уникальных api ключей для взаимодействия с backend-ом проекта

# BACKEND AND MOBILE CONNECTION
Так как у нас не получилось воспользоваться сервисом Cloud и нету выделенной VDS с доменом, для автомной работы проекта, то всё наше творчество может существовать только в предалах локальной сети, сейчас адреса прописаны хардкодом чтобы поменять, перейдите в директорию мобильного проекта по пути: services/network/service.cs поменяйте ip нa
line - 25
line - 26

# THIS README ONLY FOR WEBSITE AND BACKEND 
mobile project - https://github.com/OneCellDM/HacKMSK_IPITik_mobile