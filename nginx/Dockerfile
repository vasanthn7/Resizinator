FROM nginx:1.25.5-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./options-ssl-nginx.conf /etc/nginx/conf.d/options-ssl-nginx.conf

RUN mkdir -p /var/www/static
