import os
from sonarqube import SonarQube

# --- Configuration ---
# Make sure to configure these to an existing project and a file within it
PROJECT_KEY = "my-project-key"
FILE_KEY = "my-project-key:src/my_file.py"  # Example for a Python file

# A list of metrics to retrieve.
# See https://next.sonarqube.com/sonarqube/web_api/api/metrics/search for a full list.
METRICS_TO_REQUEST = [
    "coverage",
    "bugs",
    "vulnerabilities",
    "code_smells",
    "duplicated_lines_density",
    "ncloc",  # Number of lines of code
]

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


def get_and_print_measures(component_key, title):
    """
    Generic function to get and print measures for a given component.
    """
    print(f"--- {title} ---")
    try:
        measures = sonarqube.measures.component(
            component=component_key, metricKeys=",".join(METRICS_TO_REQUEST)
        )

        print(f"Measures for component '{measures['component']['name']}':")
        for measure in measures["component"]["measures"]:
            metric_name = measure["metric"]
            metric_value = measure["value"]
            print(f"  - {metric_name}: {metric_value}")

    except Exception as e:
        print(f"Error getting measures for component '{component_key}': {e}")
    print("-" * (len(title) + 6) + "\n")


# --- Main Execution ---
if __name__ == "__main__":
    # 1. Get measures for the entire project
    get_and_print_measures(PROJECT_KEY, "Project-Level Measures")

    # 2. Get measures for a specific file (must-have)
    get_and_print_measures(FILE_KEY, "File-Level Measures")
