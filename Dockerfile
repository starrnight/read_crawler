FROM python:3.8

MAINTAINER hexin

ENV PROJECT_ENV default
ENV PROJECT_PORT 8078
ENV PYTHON_MIRROR http://127.0.0.1:8081/repository/pypi-group/simple/
ENV PYTHON_MIRROR_HOST 127.0.0.1

WORKDIR /opt/projects/read_crawler

COPY . .

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone  \
    && pip config --global set global.index-url $PYTHON_MIRROR \
    && pip config --global set install.trusted-host $PYTHON_MIRROR_HOST \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE $PROJECT_PORT

CMD gunicorn -c $CODE_DIR/main/gunicorn.conf.py -b 0.0.0.0:$PROJECT_PORT "main.wsgi"