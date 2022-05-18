FROM python:3.8

MAINTAINER hexin

ARG python_mirror
ARG python_mirror_host

ENV PROJECT_ENV default
ENV PROJECT_PORT 8078

WORKDIR /opt/projects/read_crawler

COPY . .

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone  \
    && pip config --global set global.index-url $python_mirror \
    && pip config --global set install.trusted-host $python_mirror_host \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE $PROJECT_PORT

CMD gunicorn -c $CODE_DIR/main/gunicorn.conf.py -b 0.0.0.0:$PROJECT_PORT "main.wsgi"