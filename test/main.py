from fastapi import FastAPI
import asyncio
from fastapi.responses import PlainTextResponse
from uvicorn import Config, Server

app = FastAPI()


@app.get("/")
def say_hello(name: str, message: str):
        return PlainTextResponse(f"Hello {name}!\n{message}!")


if __name__ == "__main__":
    loop_main = asyncio.new_event_loop()
    config_server = Config(app=app, loop=loop_main)
    server = Server(config_server)
    loop_main.run_until_complete(server.serve())