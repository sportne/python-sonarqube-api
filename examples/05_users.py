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

# Search for active users
try:
    users = sonarqube.users.search_users(q="")  # Empty query to get all users

    print(f"Found {len(users['users'])} active users:")
    for user in users["users"]:
        print(
            f"  - Login: {user['login']}, Name: {user['name']}, Email: {user.get('email', 'N/A')}"
        )

except Exception as e:
    print(f"Error searching for users: {e}")
