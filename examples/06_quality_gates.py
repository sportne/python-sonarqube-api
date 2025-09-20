import os
from sonarqube import SonarQube

# --- Configuration ---
# Make sure to configure this to an existing project key
PROJECT_KEY = "my-project-key"

# Get SonarQube credentials from environment variables
SONAR_HOST = os.getenv("SONAR_HOST", "http://localhost:9000")
SONAR_TOKEN = os.getenv("SONAR_TOKEN")

# Instantiate the SonarQube client
if SONAR_TOKEN:
    sonarqube = SonarQube(host=SONAR_HOST, token=SONAR_TOKEN)
else:
    print(
        "SONAR_TOKEN environment variable not set. Please set it to your SonarQube API token."
    )
    exit(1)

# Get the quality gate status for the project
try:
    qg_status = sonarqube.quality_gates.project_status(projectKey=PROJECT_KEY)
    project_status = qg_status["projectStatus"]

    print(
        f"Quality Gate status for project '{PROJECT_KEY}': {project_status['status']}"
    )
    print("--- Conditions ---")

    if not project_status["conditions"]:
        print("No conditions found for this quality gate.")
    else:
        for condition in project_status["conditions"]:
            print(
                f"  - Metric: {condition['metricKey']}, "
                f"Status: {condition['status']}, "
                f"Value: {condition.get('actualValue', 'N/A')}"
            )
    print("------------------")

except Exception as e:
    print(f"Error getting quality gate status for project '{PROJECT_KEY}': {e}")
