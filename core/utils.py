import os
import shutil


def init_dir(dir_, mode='append'):
    if mode == 'append':
        if not os.path.exists(dir_):
            os.makedirs(dir_)
    elif mode == 'remove':
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.makedirs(dir_)
    else:
        raise NotImplementedError
    
def parse_html(html_path, fills):
    with open(html_path, encoding='utf-8') as f:
        html = f.read()
    for i, fill in enumerate(fills):
        html = html.replace('{' + str(i + 1) + '}', str(fill))
    return html