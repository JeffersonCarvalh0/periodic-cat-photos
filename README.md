# periodic-cat-photos

This bot is intended to solve your problems when it comes to getting random cat pictures in your discord server. It is still a work in progress.

invite url: https://discord.com/api/oauth2/authorize?client_id=926491618075377674&permissions=60480&scope=bot

## Current commands list

 - `!pcats random` -> shows a random cat picture
 
## How to run locally

### Manually

 - `pip install -r requirements.txt`
 - `python3 main.py`

### Using docker compose

 - `docker-compose up`

It requires the following env vars to be configured:

```
DISCORD_TOKEN=<app token>
CAT_API_TOKEN=<api token from https://thecatapi.com>
```

If you are running it through docker-compose, just create an .env file with those variables in the project's root dir and docker-compose will handle the rest.

## License
MIT
