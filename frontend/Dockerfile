# Etapa 1: build de la app
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Etapa 2: servidor estático con nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
