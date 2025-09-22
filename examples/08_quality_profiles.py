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

# Search for quality profiles
profiles = sonarqube.qualityprofiles.search_quality_profiles()

# Print the profiles
for profile in profiles["profiles"]:
    print(f"- {profile['key']}: {profile['name']} ({profile['language']})")
