import requests
import json

# Define the Grafana server URL and credentials
grafana_url = 'http://<grafana-server-url>:<grafana-port>'
grafana_user = '<grafana-username>'
grafana_password = '<grafana-password>'

# Create a new dashboard in Grafana
dashboard_data = {
    "dashboard": {
        "id": None,
        "title": "My Dashboard",
        "panels": [{
            "id": 1,
            "title": "My Graph",
            "type": "graph",
            "datasource": "<datasource-name>",
            "targets": [{
                "expr": "<metric-expression>"
            }],
            "xaxis": {
                "mode": "time",
                "show": True
            },
            "yaxes": [{
                "format": "short",
                "show": True
            }, {
                "format": "short",
                "show": True
            }],
        }],
        "timezone": "browser",
        "schemaVersion": 21
    },
    "overwrite": True
}

response = requests.post(
    f'{grafana_url}/api/dashboards/db',
    auth=(grafana_user, grafana_password),
    headers={'Content-Type': 'application/json'},
    data=json.dumps(dashboard_data)
)

print(response.content)
