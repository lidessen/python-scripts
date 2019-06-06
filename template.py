import os
from utils import check_path, get_files

TEMPLATE_DIR = '.my_templates'

def get_templates(path):
    templ_path = os.path.join(path, TEMPLATE_DIR)
    if(not check_path(templ_path)):
        return
    