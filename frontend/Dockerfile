FROM node:latest
ENV HOST 0.0.0.0
ADD . /app
WORKDIR /app
EXPOSE 3000

RUN npm i
RUN npm run build

#RUN npm i -g npm && npm i -g yarn
#RUN rm yarn.lock
#RUN yarn
#RUN yarn build
#CMD [ "yarn", "start" ]
