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
}

def custom_js():
    full_js=''
    if params['ext_bar']:
        full_js+=open(ext_bar_js, 'r').read()
        
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
        ext = gr.Checkbox(value=params['ext_bar'], label='Use extension bar')
        
    # Event functions to update the parameters in the backend
    sticky.change(lambda x: params.update({"sticky_tabs": x}), sticky, None)
    ext.change(lambda x: params.update({"ext_bar": x}), ext, None)
    
    #ext button
    btn = gr.Button("Extensions", elem_id = "ext_toggle", visible=params['ext_bar']) 
    btn.click(None, None, None)