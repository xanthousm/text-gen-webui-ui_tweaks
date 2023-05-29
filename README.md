# ui_tweaks
An extension for  [text-generation-webui by oobabooga](https://github.com/oobabooga/text-generation-webui). 

Adds options to keep tabs on page (sticky tabs) and to move extensions into a hidden sidebar.

![image](https://github.com/xanthousm/text-gen-webui-ui_tweaks/assets/70198941/c5998420-9607-43d1-865f-65ec0f449ec2)

### Installation:
1. Make sure you're in the `text-generation-webui` directory and clone this repository directly into the `extensions` directory
```bash
git clone https://github.com/xanthousm/text-gen-webui-ui_tweaks.git extensions/ui_tweaks
```
2. Activate it in the UI's **Interface mode** tab, or by using the ```--extension``` flag on launch (e.g. `--extension ui_tweaks`).

### Sidebar settings:
- Open sidebar on startup
- Hide sidebar by clicking anywhere
- Dynamic height (shrink to fit)
- Custom width

### Save default settings by editing ```params``` in ```script.py``` or by using oobabooga's ```settings.yaml``` file:
- Eg: Add ```ui_tweaks-bar_init_show: true``` to a new line in ```settings.yaml```
