#FROM node:latest
#ENV HOST 0.0.0.0
#ADD . /app
#WORKDIR /app
#EXPOSE 3000

#RUN npm i
#RUN npm run build
#RUN npm i -g npm && npm i -g yarn
#RUN rm yarn.lock
#RUN yarn
#RUN yarn build
#CMD [ "npm", "run", "start" ]
FROM node:lts-alpine

ENV HOST 0.0.0.0
# устанавливаем простой HTTP-сервер для статики
RUN npm install -g http-server

# делаем каталог 'app' текущим рабочим каталогом
WORKDIR /app

# копируем оба 'package.json' и 'package-lock.json' (если есть)
COPY package*.json ./

# устанавливаем зависимости проекта за исключением зависимостей для разработки
RUN npm install

# копируем файлы и каталоги проекта в текущий рабочий каталог (т.е. в каталог 'app')
COPY . .

# собираем приложение для production с минификацией
RUN npm run build

EXPOSE 3000
CMD [ "http-server", "dist" ]
