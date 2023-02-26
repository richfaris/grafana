import requests
import json

GRAFANA_API_URL = "http://localhost:3000/api"

# Set the API key for authentication
headers = {
    "Authorization": "Bearer <YOUR_API_KEY>",
    "Content-Type": "application/json"
}

# Define the dashboard JSON
dashboard = {
    "dashboard": {
        "title": "My Dashboard",
        "panels": [
            {
                "title": "Panel 1",
                "type": "graph",
                "targets": [
                    {
                        "refId": "A",
                        "expr": "sum(my_metric{job='my_job'})"
                    }
                ]
            },
            {
                "title": "Panel 2",
                "type": "text",
                "content": "Hello World"
            }
        ],
        "time": {
            "from": "now-6h",
            "to": "now"
        },
        "refresh": "5s"
    },
    "overwrite": True
}

# Send the dashboard JSON to the API to create the dashboard
response = requests.post(f"{GRAFANA_API_URL}/dashboards/db", headers=headers, data=json.dumps(dashboard))

# Check the response
if response.status_code == 200:
    print("Dashboard created successfully!")
else:
    print(f"Dashboard creation failed with status code {response.status_code}: {response.text}")
