import requests


class SonarQubeAPI:
    def __init__(self, host=None, token=None, user=None, password=None):
        """
        Create a SonarQube API client.
        :param host: SonarQube host, eg. http://localhost:9000
        :param token: SonarQube user token
        :param user: SonarQube user
        :param password: SonarQube password
        """
        self.host = host
        self.token = token
        self.user = user
        self.password = password

        # Configure authentication
        self.session = requests.Session()
        if self.token:
            self.session.auth = (self.token, "")
        elif self.user and self.password:
            self.session.auth = (self.user, self.password)

    def _get(self, endpoint, **kwargs):
        """
        Send a GET request to the SonarQube API.
        """
        return self.session.get(f"{self.host}/{endpoint}", **kwargs)

    def _post(self, endpoint, **kwargs):
        """
        Send a POST request to the SonarQube API.
        """
        return self.session.post(f"{self.host}/{endpoint}", **kwargs)

    def is_authenticated(self):
        """
        Check if the client is authenticated.
        """
        response = self._get("api/authentication/validate")
        return response.status_code == 200 and response.json().get("valid") is True

    def search_projects(self, q):
        """
        Search for projects.
        :param q: The query to search for.
        """
        params = {"q": q}
        return self._get("api/projects/search", params=params)

    def create_project(self, project_key, name):
        """
        Create a new project.
        :param project_key: The key of the new project.
        :param name: The name of the new project.
        """
        params = {"project": project_key, "name": name}
        return self._post("api/projects/create", params=params)

    def delete_project(self, project_key):
        """
        Delete a project.
        :param project_key: The key of the project to delete.
        """
        params = {"project": project_key}
        return self._post("api/projects/delete", params=params)

    def search_issues(self, **kwargs):
        """
        Search for issues.
        :param kwargs: The search parameters.
        """
        return self._get("api/issues/search", params=kwargs)

    def get_issue_details(self, issue_key):
        """
        Get the details of a specific issue.
        :param issue_key: The key of the issue to get details for.
        """
        return self.search_issues(issues=issue_key)

    def assign_issue(self, issue_key, assignee):
        """
        Assign an issue to a user.
        :param issue_key: The key of the issue to assign.
        :param assignee: The login of the user to assign the issue to.
        """
        params = {"issue": issue_key, "assignee": assignee}
        return self._post("api/issues/assign", params=params)

    def add_comment_to_issue(self, issue_key, text):
        """
        Add a comment to an issue.
        :param issue_key: The key of the issue to add a comment to.
        :param text: The text of the comment.
        """
        params = {"issue": issue_key, "text": text}
        return self._post("api/issues/add_comment", params=params)

    def transition_issue(self, issue_key, transition):
        """
        Transition an issue.
        :param issue_key: The key of the issue to transition.
        :param transition: The transition to apply.
        """
        params = {"issue": issue_key, "transition": transition}
        return self._post("api/issues/do_transition", params=params)

    def bulk_change_issues(self, **kwargs):
        """
        Bulk change issues.
        :param kwargs: The parameters for the bulk change.
        """
        return self._post("api/issues/bulk_change", params=kwargs)

    def get_issue_changelog(self, issue_key):
        """
        Get the changelog of an issue.
        :param issue_key: The key of the issue.
        """
        params = {"issue": issue_key}
        return self._get("api/issues/changelog", params=params)

    def delete_comment(self, comment_key):
        """
        Delete a comment on an issue.
        :param comment_key: The key of the comment to delete.
        """
        params = {"comment": comment_key}
        return self._post("api/issues/delete_comment", params=params)

    def edit_comment(self, comment_key, text):
        """
        Edit a comment on an issue.
        :param comment_key: The key of the comment to edit.
        :param text: The new text of the comment.
        """
        params = {"comment": comment_key, "text": text}
        return self._post("api/issues/edit_comment", params=params)

    def set_issue_severity(self, issue_key, severity):
        """
        Set the severity of an issue.
        :param issue_key: The key of the issue.
        :param severity: The new severity.
        """
        params = {"issue": issue_key, "severity": severity}
        return self._post("api/issues/set_severity", params=params)

    def set_issue_tags(self, issue_key, tags):
        """
        Set the tags of an issue.
        :param issue_key: The key of the issue.
        :param tags: The new tags.
        """
        params = {"issue": issue_key, "tags": tags}
        return self._post("api/issues/set_tags", params=params)

    def get_tags(self, **kwargs):
        """
        Get a list of tags for issues.
        :param kwargs: The search parameters.
        """
        return self._get("api/issues/tags", params=kwargs)

    def get_authors(self, **kwargs):
        """
        Get a list of issue authors.
        :param kwargs: The search parameters.
        """
        return self._get("api/issues/authors", params=kwargs)
