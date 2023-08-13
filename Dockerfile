FROM nvidia/cuda:11.4.3-base-ubuntu20.04
ENV NOTO_DIR /usr/share/fonts/opentype/notosans

RUN apt update \
    && apt install -y \
    git \
    curl \
    # make \
    unzip \
    # ffmpeg \
    file \
    xz-utils \
    sudo \
    python3 \
    python3-pip

# RUN mkdir -p ${NOTO_DIR} &&\
#   wget -q https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip -O noto.zip &&\
#   unzip ./noto.zip -d ${NOTO_DIR}/ &&\
#   chmod a+r ${NOTO_DIR}/NotoSans* &&\
#   rm ./noto.zip

RUN apt-get autoremove -y && apt-get clean && \
  rm -rf /usr/local/src/*

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -U pip setuptools wheel \
    && pip install --no-cache-dir -r /tmp/requirements.txt
