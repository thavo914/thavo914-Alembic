from flask_appbuilder import BaseView, expose
from airflow.models import DagRun
from airflow.utils.state import State
from airflow.utils.timezone import utcnow
from datetime import timedelta
import os

class MetricsDashboard(BaseView):
    route_base = "/metrics"
    # This path is relative to the view module location
    template_folder = "../templates"  # Changed to point to parent directory's templates folder
    
    @expose("/")
    def list(self):
        # Get metrics for the last 24 hours using timezone-aware datetime
        end_date = utcnow()
        start_date = end_date - timedelta(days=1)
        
        # Get DAG runs
        dag_runs = DagRun.find(
            execution_start_date=start_date,
            execution_end_date=end_date
        )
        
        # Calculate success rate
        success_count = len([run for run in dag_runs if run.state == State.SUCCESS])
        total_runs = len(dag_runs)
        success_rate = (success_count / total_runs * 100) if total_runs > 0 else 0
        
        # Prepare metrics for template
        metrics = {
            'total_runs': total_runs,
            'success_count': success_count,
            'success_rate': round(success_rate, 2),
            'start_date': start_date,
            'end_date': end_date
        }
        
        # Add debugging to verify template path
        template_path = os.path.join(os.path.dirname(__file__), "../templates/dashboard.html")
        print(f"Looking for template at: {template_path}")
        print(f"Template exists: {os.path.exists(template_path)}")
        
        return self.render_template(
            "dashboard.html",
            metrics=metrics
        )