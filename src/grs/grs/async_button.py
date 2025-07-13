import panel as pn
import param
import asyncio

pn.extension()

def async_button():
    button = pn.widgets.Button(name='Click me!')
    text = pn.widgets.StaticText()

    async def run_async(event):
        text.value = f'Running {event.new}'
        await asyncio.sleep(2)
        text.value = f'Finished {event.new}'

    button.on_click(run_async)


    env_param = param.Selector(default="prod", objects=["prod", "dev"])
    env_box = pn.widgets.Select(
        name="Region Name", 
        value=env_param.default, 
        options=env_param.objects,
    )
    placeholder = pn.pane.Placeholder()

    def redirect_func(env):
        if env == "prod":
            url = "https://panel.holoviz.org/"
        else:
            url = "https://holoviz-dev.github.io/panel/"

        button = pn.widgets.Button(name=f"Open {env}")
        # button.js_on_click(args=dict(url=url), code="window.open(url, '_blank');")
        button.js_on_click(code=f"window.location.href='{url}'")
        placeholder.update(button)

    pn.bind(redirect_func, env=env_box.param.value, watch=True)
    env_box.param.trigger("value")

    col = pn.Column(
            pn.Row(button, text),
            pn.Row(env_box, placeholder),
            )
    return col
    # slider = pn.widgets.IntSlider(name='Slider', start=0, end=10, value=3)
    # return slider.rx() * '⭐'
    # return pn.Column([
    #     row,
    #     ]).rx() * "2"
    # return button

# import panel as pn
# import asyncio
#
# from fastapi.templating import Jinja2Templates
# from bokeh.embed import server_document
#
#
# pn.extension()
# templates = Jinja2Templates(directory="templates")
#
# def async_button():
#     button = pn.widgets.Button(name='Click me!')
#     text = pn.widgets.StaticText()
#
#     async def run_async(event):
#         text.value = f'Running {event.new}'
#         await asyncio.sleep(2)
#         text.value = f'Finished {event.new}'
#
#     button.on_click(run_async)
#
#     # row = pn.Row(button, text)
#     # slider = pn.widgets.IntSlider(name='Slider', start=0, end=10, value=3)
#     # return slider.rx() * '⭐'
#     # return pn.Column([
#     #     row,
#     #     ])
#     script = server_document('http://127.0.0.1:5000/app')
#     return templates.TemplateResponse(
#             "button.html", 
#             {
#                 "script": script,
#                 },
#             )
