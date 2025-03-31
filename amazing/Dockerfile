FROM node:lts-alpine AS build
WORKDIR /app
COPY package*.json ./

FROM node:lts-alpine 
WORKDIR /app
COPY --from=build /app /app
COPY ./index.js ./
EXPOSE 5000
ENTRYPOINT ["node","index.js"]