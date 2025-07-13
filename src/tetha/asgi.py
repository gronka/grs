import panel as pn
from bokeh.embed import server_document
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from panel.io.fastapi import add_applications

from grs.async_button import async_button


app = FastAPI()
pn.extension()
templates = Jinja2Templates(directory="templates")


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/")
async def bkapp_page(request: Request):
    script = server_document('http://127.0.0.1:5000/app')
    return templates.TemplateResponse("base.html", {"request": request, "script": script})

def create_panel_app():
    slider = pn.widgets.IntSlider(name='Slider', start=0, end=10, value=3)
    return slider.rx() * '⭐'

def create_panel_app4():
    slider = pn.widgets.IntSlider(name='Slider', start=0, end=10, value=3)
    return slider.rx() * '⭐'

add_applications({
    "/panel_app1": create_panel_app,
    "/panel_app2": pn.Column('I am a Panel object!'),
    "/panel_app3": "async_button.py",
    "/panel_app4": create_panel_app4,
    "/button": async_button,
}, app=app)

# from fast.sinewave import SineWave
#
# def createApp():
#     sw = SineWave()
#     return pn.Row(sw.param, sw.plot).servable()
#
# pn.serve({'/app': createApp},
#         port=5000, allow_websocket_origin=["127.0.0.1:8000"],
#         address="127.0.0.1", show=False)
