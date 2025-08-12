class SonarQubeIssues:
    def __init__(self, client):
        self.client = client

    def search_issues(self, **kwargs):
        """
        Search for issues.
        :param kwargs: The search parameters.
        """
        return self.client._get("api/issues/search", params=kwargs)

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
        return self.client._post("api/issues/assign", params=params)

    def add_comment_to_issue(self, issue_key, text):
        """
        Add a comment to an issue.
        :param issue_key: The key of the issue to add a comment to.
        :param text: The text of the comment.
        """
        params = {"issue": issue_key, "text": text}
        return self.client._post("api/issues/add_comment", params=params)

    def transition_issue(self, issue_key, transition):
        """
        Transition an issue.
        :param issue_key: The key of the issue to transition.
        :param transition: The transition to apply.
        """
        params = {"issue": issue_key, "transition": transition}
        return self.client._post("api/issues/do_transition", params=params)

    def bulk_change_issues(self, **kwargs):
        """
        Bulk change issues.
        :param kwargs: The parameters for the bulk change.
        """
        return self.client._post("api/issues/bulk_change", params=kwargs)

    def get_issue_changelog(self, issue_key):
        """
        Get the changelog of an issue.
        :param issue_key: The key of the issue.
        """
        params = {"issue": issue_key}
        return self.client._get("api/issues/changelog", params=params)

    def delete_comment(self, comment_key):
        """
        Delete a comment on an issue.
        :param comment_key: The key of the comment to delete.
        """
        params = {"comment": comment_key}
        return self.client._post("api/issues/delete_comment", params=params)

    def edit_comment(self, comment_key, text):
        """
        Edit a comment on an issue.
        :param comment_key: The key of the comment to edit.
        :param text: The new text of the comment.
        """
        params = {"comment": comment_key, "text": text}
        return self.client._post("api/issues/edit_comment", params=params)

    def set_issue_severity(self, issue_key, severity):
        """
        Set the severity of an issue.
        :param issue_key: The key of the issue.
        :param severity: The new severity.
        """
        params = {"issue": issue_key, "severity": severity}
        return self.client._post("api/issues/set_severity", params=params)

    def set_issue_tags(self, issue_key, tags):
        """
        Set the tags of an issue.
        :param issue_key: The key of the issue.
        :param tags: The new tags.
        """
        params = {"issue": issue_key, "tags": tags}
        return self.client._post("api/issues/set_tags", params=params)

    def get_tags(self, **kwargs):
        """
        Get a list of tags for issues.
        :param kwargs: The search parameters.
        """
        return self.client._get("api/issues/tags", params=kwargs)

    def get_authors(self, **kwargs):
        """
        Get a list of issue authors.
        :param kwargs: The search parameters.
        """
        return self.client._get("api/issues/authors", params=kwargs)

    def get_anticipated_issue_transitions(self, issue):
        """
        Receive a list of anticipated transitions that can be applied to not yet discovered issues on a specific project.
        :param issue: Issue key
        """
        params = {"issue": issue}
        return self.client._post("api/issues/anticipated_transitions", params=params)

    def get_issue_component_tags(self, component, **kwargs):
        """
        List tags for the issues under a given component.
        :param component: Component key
        :param kwargs: Additional parameters
        """
        params = {"component": component}
        params.update(kwargs)
        return self.client._get("api/issues/component_tags", params=params)

    def export_issues_gitlab_sast(self, project, branch=None, pullRequest=None):
        """
        Return a list of vulnerabilities according to the Gitlab SAST JSON format.
        :param project: Project key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/issues/gitlab_sast_export", params=params)

    def list_issues(self, project, **kwargs):
        """
        List issues.
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"project": project}
        params.update(kwargs)
        return self.client._get("api/issues/list", params=params)

    def pull_issues(self, branch, project, **kwargs):
        """
        Fetch and return all issues for a given branch.
        :param branch: Branch key
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"branch": branch, "project": project}
        params.update(kwargs)
        return self.client._get("api/issues/pull", params=params)

    def pull_taint_issues(self, branch, project, **kwargs):
        """
        Fetch and return all taint vulnerabilities for a given branch.
        :param branch: Branch key
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"branch": branch, "project": project}
        params.update(kwargs)
        return self.client._get("api/issues/pull_taint", params=params)

    def reindex_issues(self, project):
        """
        Reindex issues for a project.
        :param project: Project key
        """
        params = {"project": project}
        return self.client._post("api/issues/reindex", params=params)
