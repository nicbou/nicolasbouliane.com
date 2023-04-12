---
title: Running multiple docker-compose projects on the same ports
description: How to serve separate docker-compose projects on the same port without merging them together.
date_created: 2020-11-10
---

Let's say you have two web apps: **ApplesApp** and **OrangesApp**. They are served at apples.com and oranges.com. You want both websites to live on the same server, on the same ports (80 and 443).

Both apps have a similarly simple docker-compose.yml:``

```yaml
# /projects/apples-app/docker-compose.yml
# /projects/oranges-app/docker-compose.yml

version: "3.5"
services:
  db:
    image: postgres:9.6
  backend:
    build: backend
    depends_on:
      - db
  frontend:
    build: frontend
    depends_on:
      - backend
  reverse-proxy: # Routes requests to frontend/backend
    image: nginx
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - backend
      - frontend
```

## The bad solution

You could bring both web apps under the same docker-compose.yml file, and use a reverse proxy to route the requests to the right containers:

```yaml
# /projects/apples-and-oranges/docker-compose.yml

version: "3.5"
services:
  db-apples:
    image: postgres:9.6
  backend-apples:
    build: backend-apples
    depends_on:
      - db-apples
  frontend-apples:
    build: frontend-apples
    depends_on:
      - backend-apples
  db-oranges:
    image: postgres:9.6
  backend-oranges:
    build: backend-oranges
    depends_on:
      - db-oranges
  frontend-oranges:
    build: frontend-oranges
    depends_on:
      - backend-oranges
  # Routes requests to ApplesApp or OrangesApp frontend/backend
  reverse-proxy:
    build: reverse-proxy
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - backend-apples
      - frontend-apples
      - backend-oranges
      - frontend-oranges
```

Okay, that works, but what if you have 5 separate websites, each with half a dozen containers? That docker-compose.yml file will get a little messy. The reverse-proxy's nginx config will get *very* messy.

Besides, those two websites are completely unrelated! If you're working on ApplesApp locally, you don't need to run OrangesApp. If you want to package OrangesApp for other users, you don't want to bundle ApplesApp with it. You also don't want to maintain a separate docker-compose config for each possible combination of apps.

## The good solution

The solution is to create a third docker-compose project that does two things:

1. Create a network that is shared with ApplesApp and OrangesApp
2. Route requests from the outside world to ApplesApp or OrangesApp, depending on the requested domain name

We'll call it **FruitPicker**. It will live in its own separate directory. We'll put all server-specific configurations in that project, so we can change our server configuration without touching ApplesApp or OrangesApp.

### Step 1: Create the parent project

The **FruitPicker** docker-compose.yml file looks like this:

```yaml
# /projects/fruitpicker/docker-compose.yml

version: "3.5"
services:
  reverse-proxy: # The FruitPicker reverse proxy
    image: nginx
    volumes:
      - nginx.conf:/etc/nginx/conf.d/default.conf
    ports:
      - "80:80"
      - "443:443"
networks:
  default:
    name: fruit-network
```

This creates a network called "**fruit-network**". It also creates the reverse-proxy that will route requests to ApplesApp and OrangesApp. We will soon add ApplesApp and OrangesApp to that network.

### Step 2: Add the child projects to the parent's network

We must create a separate docker-compose file that *extends* ApplesApp and OrangesApp's docker-compose files.

We will put those files in the FruitPicker codebase, not in ApplesApp or OrangesApp. Other ApplesApp users don't need our server-specific configurations.

I called that file "**docker-compose.apples.yml**".

```yaml
# /projects/fruitpicker/docker-compose.applesapp.yml
# /projects/fruitpicker/docker-compose.orangesapp.yml

version: "3.5"
services:
  # Extend ApplesApp's reverse-proxy to be on
  # FruitPicker's "fruit-network" network
  reverse-proxy:
    networks:
      default:
        aliases:
          # ApplesApp hostname on "fruit-network"
          - apples
networks:
  default:
    external:
      # Use the existing ("external") network we created
      name: fruit-network
```

(do the same thing for OrangesApp)

This file will *extend* the existing ApplesApp docker-compose.yml file. It adds ApplesApp's reverse proxy to the "fruit-network" network, under the hostname "apples".

Later, we will need to tell docker to use both the original ApplesApp or OrangesApp docker-compose file, and this extended docker-compose file.

### Step 3: configure the FruitPicker reverse proxy

FruitPicker's reverse proxy listens to all incoming requests. We want it to forward apples.com requests to AppleApp's reverse proxy, and oranges.com requests to OrangeApp's reverse proxy.

For example, if I request "https://oranges.com/some-frontend-url", this should happen:

1. FruitPicker's reverse-proxy receives the request, routes it to OrangeApp.
2. OrangeApp's reverse-proxy, receives the request, routes it to its backend.
3. OrangeApp's backend, receives the request

Here's how we will configure FruitPicker's reverse proxy to route requests to OrangeApp:

```
# /projects/fruitpicker/nginx.conf

server {
  # Redirect http:// to https://
  listen 80;
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name apples.com;
  resolver 127.0.0.11 valid=5s; # Local Docker DNS

  location / {
    auth_request off;
    proxy_pass http://apples:80;
    # proxy_set_header, proxy_redirect, etc...
  }
}

server {
  listen 443 ssl;
  server_name oranges.com;
  resolver 127.0.0.11 valid=5s; # Local Docker DNS

  location / {
    auth_request off;
    proxy_pass http://oranges:80;
    # proxy_set_header, proxy_redirect, etc...
  }
}

# Add as many websites as you want here
```

### Step 4: run everything

We must start FruitPicker first. That will create the "fruit-network" network.

```bash
docker-compose -f /projects/fruitpicker/docker-compose.yml up --build -d
```

Next, we start our projects one by one, but tell docker-compose to use the extended docker-compose.yml files.

```bash
docker-compose -f /projects/apples-app/docker-compose.yml -f /projects/fruitpicker/docker-compose.apples.yml up --build -d
```

```bash
docker-compose -f /projects/oranges-app/docker-compose.yml -f /projects/fruitpicker/docker-compose.apples.yml up --build -d
```

You should now be able to access ApplesApp from apples.com, and OrangesApp from oranges.com.

## Caveats

This solution has a few issues.

### Conflicting container names

The ApplesApp and OrangesApp reverse proxies are on two networks: their default network (with all the project's containers), and the fruit-network network (with all the reverse proxies).

If there are containers with the same names on both networks, there's no way to know which one will be used. It shouldn't be an issue in the example above.

You could also assign a higher priority to the default network, but the priority keyword [simply doesn't work](https://github.com/docker/compose/issues/4645#issuecomment-701351876).

### Ports already in use

FruitPicker listens to ports 80 and 443. Your original ApplesApp and OrangesApp also listen to those ports.

You can't un-open ports by extending the docker-compose file. This means you'll need to have a more complicated layout:

- The base docker-compose.yml file shouldn't open any ports.
- The docker-compose.apples.yml file in FruitPicker also shouldn't open any port.
- Create a docker-compose.override.yml file in ApplesApp and OrangesApp, and use that file to open ports 80 and 443.

Here's an example:

```yaml
# /projects/apples-app/docker-compose.yml
# /projects/oranges-app/docker-compose.yml

version: "3.5"
services:
  db:
    ...
  backend:
    ...
  frontend:
    ...
  reverse-proxy: # Routes requests to frontend/backend
    image: nginx
    # NO OPEN PORTS!
    # ports:
    #   - "80:80"
    #   - "443:443"
    depends_on:
      - backend
      - frontend
```

Then create an override file to open the ports. By default, Compose reads two files, a docker-compose.yml and an optional docker-compose.override.yml file. This means the ports will be open by default, but not when you run it as part of FruitPicker.

```yaml
# /projects/apples-app/docker-compose.override.yml
# /projects/oranges-app/docker-compose.override.yml

version: "3.5"
services:
  reverse-proxy:
    ports:
      - "80:80"
      - "443:443"
```

