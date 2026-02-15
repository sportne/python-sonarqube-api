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

# Search for open issues in the project
try:
    response = sonarqube.issues.search_issues(componentKeys=PROJECT_KEY, statuses="OPEN")
    issues = response.json()

    print(f"Found {issues['paging']['total']} open issues in project '{PROJECT_KEY}':")
    for issue in issues["issues"]:
        print(
            f"  - [{issue['severity']}] {issue['message']} "
            f"(in {issue['component']})"
        )

except Exception as e:
    print(f"Error searching for issues in project '{PROJECT_KEY}': {e}")
