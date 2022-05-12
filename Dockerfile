FROM python:3.8

MAINTAINER hexin

ARG PROJECT_ENV
ARG PROJECT_PORT
ENV PROJECT_ENV ${PROJECT_ENV:-default}
ENV PROJECT_PORT ${PROJECT_PORT:-8078}

ENV CODE_DIR /opt/projects/read_crawler

WORKDIR $CODE_DIR

COPY . $CODE_DIR

ENV MIRROR_PARAM -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone  \
    && pip3 install -r $CODE_DIR/requirements.txt --no-cache-dir $MIRROR_PARAM \

EXPOSE $PROJECT_PORT

CMD gunicorn -c $CODE_DIR/main/gunicorn.conf.py -b 0.0.0.0:$PROJECT_PORT "main.wsgi"