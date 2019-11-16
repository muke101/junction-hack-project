FROM node:12
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN ls
RUN yarn && yarn build

FROM nginx:alpine
COPY --from=0 /usr/src/app/build /usr/share/nginx/html
EXPOSE 80
