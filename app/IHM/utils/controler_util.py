import importlib


def auto_instance_ui(page):
    page_name = page.__class__.__name__  # Exemple : HomePage -> HomePage
    ui_class_name_str = f"Ui{page.__class__.__name__}"  # Exemple : HomePage -> UiHomePage

    # Exemple : app.IHM.pages.home.home_ui_page
    module_name_str = f"app.IHM.pages.{page_name.lower().replace('page', '')}.{page_name.lower().replace('page', '')}_ui_page"
    return import_class(module_name_str, ui_class_name_str)()

def import_class(module_name: str, class_name: str):
    """Importer dynamiquement une classe en utilisant le nom du module et de la classe"""
    module = importlib.import_module(module_name)
    return getattr(module, class_name)