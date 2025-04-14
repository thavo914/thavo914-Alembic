from airflow.plugins_manager import AirflowPlugin
from flask_appbuilder.security.manager import SecurityManager
from flask_appbuilder.menu import Menu

class CustomSecurityManager(SecurityManager):
    def __init__(self, appbuilder):
        super(CustomSecurityManager, self).__init__(appbuilder)

class CustomPlugin(AirflowPlugin):
    name = "custom_plugin"
    operators = []
    flask_blueprints = []
    hooks = []
    executors = []
    admin_views = []
    menu_links = [
        Menu(
            name='Custom Dashboard',
            href='/custom_dashboard',
            category='Custom Menu',
            category_icon='fa-th'
        )
    ]
    appbuilder_views = []
    appbuilder_menu_items = []