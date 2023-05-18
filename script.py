import os

import gradio as gr

current_dir = os.path.dirname(os.path.abspath(__file__))
sticky_tabs_css = os.path.join(current_dir, "sticky_tabs.css")
ext_bar_css = os.path.join(current_dir, "ext_bar.css")
ext_bar_js = os.path.join(current_dir, "ext_bar.js")

params = {
    "display_name": "UI Tweaks (Restart to apply)",
    "is_tab": False,
    "sticky_tabs": True,
    "ext_bar": True,
    "bar_init_show":False,
    "bar_dyna_height":False,
    "bar_width": 500,
}

def custom_js():
    full_js=''
    if params['ext_bar']:
        full_js+=open(ext_bar_js, 'r').read()
        
    #initially show extensions if set in params
    if params['bar_init_show']:
        full_js+='\ndocument.getElementById("extensions").style.setProperty("right", "5px");'
        
    #lock bar height to max if not dynamic
    if not params['bar_dyna_height']:
        full_js+='\ndocument.getElementById("extensions").style.setProperty("height", "calc(100% - 5em)");'
        
    full_js+=f'\ndocument.getElementById("extensions").style.setProperty("max-width", "{params["bar_width"]}px");'    
    
    return full_js

def custom_css():
    full_css=''
    if params['ext_bar']:
        full_css+=open(ext_bar_css, 'r').read()
        
    if  params['sticky_tabs']:
        full_css+=open(sticky_tabs_css, 'r').read()
    
    return full_css
    
def ui():    
    with gr.Row():
        sticky = gr.Checkbox(value=params['sticky_tabs'], label='Use sticky tabs')
        ext = gr.Checkbox(value=params['ext_bar'], label='Use extension sidebar')
    with gr.Accordion("Extension sidebar settings", open=False):
        show = gr.Checkbox(value=params['bar_init_show'], label='Open sidebar on startup')
        dyna_h = gr.Checkbox(value=params['bar_dyna_height'], label='Dynamic sidebar height')
        #set_w = gr.Number(value=params['bar_width'], label='sidebar width (pixels)', interactive=True, precision=0)
        set_w = gr.Slider(200, 2000,step=50,value=params['bar_width'], label='sidebar width (pixels)')
        
    # Event functions to update the parameters in the backend
    sticky.change(lambda x: params.update({"sticky_tabs": x}), sticky, None)
    ext.change(lambda x: params.update({"ext_bar": x}), ext, None)
    show.change(lambda x: params.update({"bar_init_show": x}), show, None)
    dyna_h.change(lambda x: params.update({"bar_dyna_height": x}), dyna_h, None)
    set_w.change(lambda x: params.update({"bar_width": x}), set_w, None)
    
    #ext button
    btn = gr.Button("Extensions", elem_id = "ext_toggle", visible=params['ext_bar']) 
    btn.click(None, None, None)