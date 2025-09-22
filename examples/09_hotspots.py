import os
from sonarqube import SonarQube

# Get SonarQube credentials from environment variables
SONAR_HOST = os.getenv("SONAR_HOST", "http://localhost:9000")
SONAR_TOKEN = os.getenv("SONAR_TOKEN")
SONAR_PROJECT_KEY = os.getenv("SONAR_PROJECT_KEY")

# Instantiate the SonarQube client
if SONAR_TOKEN:
    sonarqube = SonarQube(host=SONAR_HOST, token=SONAR_TOKEN)
else:
    print(
        "SONAR_TOKEN environment variable not set. Please set it to your SonarQube API token."
    )
    exit(1)

# Check if a project key is provided
if not SONAR_PROJECT_KEY:
    print(
        "SONAR_PROJECT_KEY environment variable not set. Please set it to your project key."
    )
    exit(1)

# Search for hotspots in the specified project
hotspots = sonarqube.hotspots.search_hotspots(projectKey=SONAR_PROJECT_KEY)

# Print the hotspots
for hotspot in hotspots["hotspots"]:
    print(f"- {hotspot['key']}: {hotspot['message']} (status: {hotspot['status']})")
