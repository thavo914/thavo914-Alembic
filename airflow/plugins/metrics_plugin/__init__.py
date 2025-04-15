from airflow.plugins_manager import AirflowPlugin
from metrics_plugin.views.dashboard import MetricsDashboard

class MetricsPlugin(AirflowPlugin):
    name = "metrics_plugin"
    operators = []
    flask_blueprints = []
    hooks = []
    executors = []
    admin_views = []
    appbuilder_views = [
        {
            "name": "Metrics Dashboard",
            "category": "Metrics",
            "view": MetricsDashboard()
        }
    ]
    appbuilder_menu_items = []
