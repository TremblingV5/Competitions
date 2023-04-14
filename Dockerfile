FROM python:3.10.6-alpine3.16
LABEL authors="xinzf"

WORKDIR /home

COPY . .

RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/

ENTRYPOINT ["./run.sh"]