FROM python:3.6
ARG USER=user
ARG GROUP=developer
ARG PASS=password

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS yes

# Common
RUN apt-get update && apt-get install -y \
  apt-transport-https \
  libasound2-dev \
  bash-completion \
  build-essential \
  bzip2 \
  cmake \
  curl \
  gcc \
  g++ \
  git \
  less \
  libatlas-base-dev \
  libgl1-mesa-dev \
  locales \
  make \
  man \
  manpages-dev \
  mosquitto-clients \
  net-tools \
  openssh-server \
  openssh-client \
  p7zip \
  postgresql-client \
  software-properties-common \
  sudo \
  unzip \
  vim \
  vim-gnome \
  wget \
  xorg-dev \
  zlib1g-dev \
  zsh

# Node-js
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y nodejs

# Heroku CLI
RUN npm install -g heroku

RUN groupadd -g 1000 $GROUP
RUN useradd -g $GROUP -G sudo -m -s /bin/bash $USER

RUN mkdir /var/run/sshd
RUN echo "${USER}:${PASS}" | chpasswd
RUN echo "root:${PASS}" | chpasswd

# SSH settings. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN sed -e 's@#Port 22@Port 22@' -e 's@#AddressFamily any@AddressFamily inet@' -i /etc/ssh/sshd_config

# OpenCV and Tensorflow
RUN ln -s /usr/include/libv4l1-videodev.h /usr/include/linux/videodev.h

RUN mkdir /tmp_cv
RUN cd /tmp_cv && wget https://github.com/Itseez/opencv/archive/3.1.0.zip && unzip 3.1.0.zip
RUN cd /tmp_cv/opencv-3.1.0 && cmake CMakeLists.txt -DWITH_TBB=ON \
                                                    -DINSTALL_CREATE_DISTRIB=ON \
                                                    -DWITH_FFMPEG=OFF \
                                                    -DWITH_IPP=OFF \
                                                    -DCMAKE_INSTALL_PREFIX=/usr/local
RUN cd /tmp_cv/opencv-3.1.0 && make -j2 && make install
# Note: The latest tornado(6.0.1) caused a problem not to connect to jupyter kernel; tornado==5.1.1 is a W/A.
RUN pip3 install numpy tensorflow opencv-python Pillow scipy matplotlib pandas keras jupyter tornado==5.1.1

# Go 1.11
RUN mkdir /tmp_go
RUN apt-get update && apt-get -y upgrade && \
  cd /tmp_go && \
  wget https://dl.google.com/go/go1.11.4.linux-amd64.tar.gz && \
  tar xvf go1.11.4.linux-amd64.tar.gz && \
  mv go /usr/local


#### User ####
USER $USER
WORKDIR /home/$USER

# Settings
RUN echo 'alias ls="ls -a --color=auto --show-control-chars --time-style=long-iso -FH"' >> /home/$USER/.profile
RUN echo 'alias ll="ls -a -lA"' >> /home/$USER/.profile
RUN echo 'alias h=history' >> /home/$USER/.profile
RUN echo 'alias vi=vim' >> /home/$USER/.profile
RUN echo 'alias jupyter_notebook="jupyter notebook --ip=0.0.0.0 --port=8080"' >> /home/$USER/.profile
RUN echo 'export GOROOT="/usr/local/go"' >> /home/$USER/.profile
RUN echo 'export GOPATH="/work/go"' >> /home/$USER/.profile
RUN echo 'export PATH="/work/bin:$GOPATH/bin:$GOROOT/bin:$PATH"' >> /home/$USER/.profile
RUN echo 'PS1="\$ "' >> /home/$USER/.bashrc
RUN echo 'set background=dark' > /home/$USER/.vimrc
RUN echo 'syntax on' >> /home/$USER/.vimrc
RUN touch /home/$USER/.Xauthority && chmod 600 /home/$USER/.Xauthority

USER root

#ADD .netrc /home/$USER
#ADD .gitconfig /home/$USER
#RUN chown $USER:$GROUP /home/$USER/.netrc /home/$USER/.gitconfig
#RUN chmod 644 /home/$USER/.netrc /home/$USER/.gitconfig

EXPOSE 22
EXPOSE 8080
