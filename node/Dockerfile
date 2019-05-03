FROM node:10.15-alpine

RUN mkdir /src
WORKDIR /src

RUN echo {} > package.json
RUN npm install --save express && \
    npm install --save ejs && \
    npm install --save pg

EXPOSE 3000
