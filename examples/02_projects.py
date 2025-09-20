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

# Search for projects
projects = sonarqube.projects.search_projects(q="my-project")
print(f"Found {projects['paging']['total']} projects matching 'my-project':")
for project in projects["components"]:
    print(f"  - {project['name']} (key: {project['key']})")

# --- Destructive Operations (commented out by default) ---

# To create a project, you would uncomment the following lines:
# try:
#     sonarqube.projects.create_project(project_key="my-new-project", name="My New Project")
#     print("Project 'my-new-project' created successfully.")
# except Exception as e:
#     print(f"Error creating project: {e}")


# To delete a project, you would uncomment the following lines:
# try:
#     sonarqube.projects.delete_project(project_key="my-new-project")
#     print("Project 'my-new-project' deleted successfully.")
# except Exception as e:
#     print(f"Error deleting project: {e}")
