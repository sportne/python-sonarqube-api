import os
from sonarqube import SonarQube

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

# Search for python rules
response = sonarqube.rules.search_rules(languages="py")
rules = response.json()

# Print the rules
for rule in rules["rules"]:
    print(f"- {rule['key']}: {rule['name']}")
