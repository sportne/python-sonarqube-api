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

    def get_anticipated_issue_transitions(self, issue):
        """
        Receive a list of anticipated transitions that can be applied to not yet discovered issues on a specific project.
        :param issue: Issue key
        """
        params = {"issue": issue}
        return self._post("api/issues/anticipated_transitions", params=params)

    def get_issue_component_tags(self, component, **kwargs):
        """
        List tags for the issues under a given component.
        :param component: Component key
        :param kwargs: Additional parameters
        """
        params = {"component": component}
        params.update(kwargs)
        return self._get("api/issues/component_tags", params=params)

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
        return self._get("api/issues/gitlab_sast_export", params=params)

    def list_issues(self, project, **kwargs):
        """
        List issues.
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"project": project}
        params.update(kwargs)
        return self._get("api/issues/list", params=params)

    def pull_issues(self, branch, project, **kwargs):
        """
        Fetch and return all issues for a given branch.
        :param branch: Branch key
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"branch": branch, "project": project}
        params.update(kwargs)
        return self._get("api/issues/pull", params=params)

    def pull_taint_issues(self, branch, project, **kwargs):
        """
        Fetch and return all taint vulnerabilities for a given branch.
        :param branch: Branch key
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"branch": branch, "project": project}
        params.update(kwargs)
        return self._get("api/issues/pull_taint", params=params)

    def reindex_issues(self, project):
        """
        Reindex issues for a project.
        :param project: Project key
        """
        params = {"project": project}
        return self._post("api/issues/reindex", params=params)

    # SonarQube Applications API
    def add_project_to_application(self, application, project):
        """
        Add a project to an application.
        :param application: Application key
        :param project: Project key
        """
        params = {"application": application, "project": project}
        return self._post("api/applications/add_project", params=params)

    def create_application(self, name, key=None, visibility=None, description=None):
        """
        Create a new application.
        :param name: Name of the application
        :param key: Key of the application
        :param visibility: Visibility of the application
        :param description: Description of the application
        """
        params = {"name": name}
        if key:
            params["key"] = key
        if visibility:
            params["visibility"] = visibility
        if description:
            params["description"] = description
        return self._post("api/applications/create", params=params)

    def create_branch_in_application(self, application, branch, project, projectBranch):
        """
        Create a new branch on a given application.
        :param application: Application key
        :param branch: Branch name
        :param project: Project keys
        :param projectBranch: Project branches
        """
        params = {
            "application": application,
            "branch": branch,
            "project": project,
            "projectBranch": projectBranch,
        }
        return self._post("api/applications/create_branch", params=params)

    def delete_application(self, application):
        """
        Delete an application definition.
        :param application: Application key
        """
        params = {"application": application}
        return self._post("api/applications/delete", params=params)

    def delete_branch_in_application(self, application, branch):
        """
        Delete a branch on a given application.
        :param application: Application key
        :param branch: Branch name
        """
        params = {"application": application, "branch": branch}
        return self._post("api/applications/delete_branch", params=params)

    def refresh_applications(self, key=None):
        """
        Refresh one or all applications.
        :param key: Application key. If not specified, all applications are refreshed.
        """
        params = {}
        if key:
            params["key"] = key
        return self._post("api/applications/refresh", params=params)

    def remove_project_from_application(self, application, project):
        """
        Remove a project from an application.
        :param application: Application key
        :param project: Project key
        """
        params = {"application": application, "project": project}
        return self._post("api/applications/remove_project", params=params)

    def search_application_projects(self, application, q=None, p=None, ps=None):
        """
        List projects manually selected in an application.
        :param application: Application key
        :param q: Query to filter projects
        :param p: Page number
        :param ps: Page size
        """
        params = {"application": application}
        if q:
            params["q"] = q
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self._get("api/applications/search_projects", params=params)

    def set_application_tags(self, application, tags):
        """
        Set tags on a application.
        :param application: Application key
        :param tags: Comma-separated list of tags
        """
        params = {"application": application, "tags": tags}
        return self._post("api/applications/set_tags", params=params)

    def show_application(self, application, branch=None, pullRequest=None):
        """
        Returns an application and its associated projects.
        :param application: Application key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"application": application}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self._get("api/applications/show", params=params)

    def show_application_leak(self, application, branch=None, pullRequest=None):
        """
        Show leak of an application.
        :param application: Application key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"application": application}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self._get("api/applications/show_leak", params=params)

    def update_application(self, application, name=None, description=None):
        """
        Update an application.
        :param application: Application key
        :param name: New name of the application
        :param description: New description of the application
        """
        params = {"application": application}
        if name:
            params["name"] = name
        if description:
            params["description"] = description
        return self._post("api/applications/update", params=params)

    def update_branch_in_application(self, application, branch, name):
        """
        Update a branch on a given application.
        :param application: Application key
        :param branch: Branch name
        :param name: New branch name
        """
        params = {"application": application, "branch": branch, "name": name}
        return self._post("api/applications/update_branch", params=params)

    # SonarQube Compute Engine API
    def get_ce_activity(self, **kwargs):
        """
        Search for tasks.
        :param kwargs: The search parameters.
        """
        return self._get("api/ce/activity", params=kwargs)

    def get_ce_activity_status(self, componentId=None):
        """
        Returns CE activity related metrics.
        :param componentId: Component ID
        """
        params = {}
        if componentId:
            params["componentId"] = componentId
        return self._get("api/ce/activity_status", params=params)

    def get_ce_analysis_status(self, analysisId):
        """
        Get the analysis status of a given component.
        :param analysisId: Analysis ID
        """
        params = {"analysisId": analysisId}
        return self._get("api/ce/analysis_status", params=params)

    def cancel_ce_task(self, id):
        """
        Cancels a pending task.
        :param id: Task ID
        """
        params = {"id": id}
        return self._post("api/ce/cancel", params=params)

    def cancel_all_ce_tasks(self):
        """
        Cancels all pending tasks.
        """
        return self._post("api/ce/cancel_all")

    def get_ce_component(self, component):
        """
        Get the pending tasks, in-progress tasks and the last executed task of a given component.
        :param component: Component key
        """
        params = {"component": component}
        return self._get("api/ce/component", params=params)

    def dismiss_ce_analysis_warning(self, project, warning):
        """
        Permanently dismiss a specific analysis warning.
        :param project: Project key
        :param warning: Warning key
        """
        params = {"project": project, "warning": warning}
        return self._post("api/ce/dismiss_analysis_warning", params=params)

    def get_ce_indexation_status(self):
        """
        Returns the count of projects with completed issue indexing.
        """
        return self._get("api/ce/indexation_status")

    def get_ce_info(self):
        """
        Gets information about Compute Engine.
        """
        return self._get("api/ce/info")

    def pause_ce(self):
        """
        Requests pause of Compute Engine workers.
        """
        return self._post("api/ce/pause")

    def resume_ce(self):
        """
        Resumes pause of Compute Engine workers.
        """
        return self._post("api/ce/resume")

    def set_ce_worker_count(self, count):
        """
        Set the number of workers in the Compute Engine.
        :param count: Number of workers
        """
        params = {"count": count}
        return self._post("api/ce/set_worker_count", params=params)

    def submit_scanner_report(self, **kwargs):
        """
        Submits a scanner report to the queue.
        :param kwargs: The submission parameters.
        """
        return self._post("api/ce/submit", params=kwargs)

    def get_ce_task(self, id):
        """
        Give Compute Engine task details.
        :param id: Task ID
        """
        params = {"id": id}
        return self._get("api/ce/task", params=params)

    def get_ce_task_types(self):
        """
        List available task types.
        """
        return self._get("api/ce/task_types")

    def get_ce_worker_count(self):
        """
        Return number of Compute Engine workers.
        """
        return self._get("api/ce/worker_count")

    # SonarQube Components API
    def get_components_app(self, component, branch=None, pullRequest=None):
        """
        Coverage data required for rendering the component viewer.
        :param component: Component key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"component": component}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self._get("api/components/app", params=params)

    def search_components(self, qualifiers, q=None, p=None, ps=None):
        """
        Search for components.
        :param qualifiers: Comma-separated list of component qualifiers.
        :param q: Query to filter components
        :param p: Page number
        :param ps: Page size
        """
        params = {"qualifiers": qualifiers}
        if q:
            params["q"] = q
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self._get("api/components/search", params=params)

    def search_components_projects(self, q=None, p=None, ps=None):
        """
        Search for projects.
        :param q: Query to filter projects
        :param p: Page number
        :param ps: Page size
        """
        params = {}
        if q:
            params["q"] = q
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self._get("api/components/search_projects", params=params)

    def show_component(self, component, branch=None, pullRequest=None):
        """
        Returns a component and its ancestors.
        :param component: Component key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"component": component}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self._get("api/components/show", params=params)

    def get_component_suggestions(self, q=None):
        """
        Internal WS for the top-right search engine.
        :param q: Query to filter components
        """
        params = {}
        if q:
            params["q"] = q
        return self._get("api/components/suggestions", params=params)

    def get_component_tree(self, component, **kwargs):
        """
        Navigate through components based on the chosen strategy.
        :param component: Base component key
        :param kwargs: Additional parameters
        """
        params = {"component": component}
        params.update(kwargs)
        return self._get("api/components/tree", params=params)

    # SonarQube Duplications API
    def get_duplications(self, key, branch=None, pullRequest=None):
        """
        Get duplications.
        :param key: File key
        :param branch: Branch key
        :param pullRequest: Pull request ID
        """
        params = {"key": key}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self._get("api/duplications/show", params=params)

    # SonarQube Editions API
    def activate_grace_period(self):
        """
        Enable a license 7-days grace period if the Server ID is invalid.
        """
        return self._post("api/editions/activate_grace_period")

    def is_valid_license(self):
        """
        Return the validity of the license.
        """
        return self._get("api/editions/is_valid_license")

    def set_license(self, license):
        """
        Set the license for enabling features of commercial editions.
        :param license: License key
        """
        params = {"license": license}
        return self._post("api/editions/set_license", params=params)

    def show_license(self):
        """
        Show information about currently installed license.
        """
        return self._get("api/editions/show_license")

    def unset_license(self):
        """
        Un-sets license.
        """
        return self._post("api/editions/unset_license")

    # SonarQube Favorites API
    def add_favorite(self, component):
        """
        Add a component as favorite.
        :param component: Component key
        """
        params = {"component": component}
        return self._post("api/favorites/add", params=params)

    def remove_favorite(self, component):
        """
        Remove a component as favorite.
        :param component: Component key
        """
        params = {"component": component}
        return self._post("api/favorites/remove", params=params)

    def search_favorites(self, p=None, ps=None):
        """
        Search for favorites.
        :param p: Page number
        :param ps: Page size
        """
        params = {}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self._get("api/favorites/search", params=params)

    # SonarQube Hotspots API
    def add_hotspot_comment(self, hotspot, text):
        """
        Add a comment to a Security Hotspot.
        :param hotspot: Hotspot key
        :param text: Comment text
        """
        params = {"hotspot": hotspot, "text": text}
        return self._post("api/hotspots/add_comment", params=params)

    def assign_hotspot(self, hotspot, assignee):
        """
        Assign a hotspot to an active user.
        :param hotspot: Hotspot key
        :param assignee: User login
        """
        params = {"hotspot": hotspot, "assignee": assignee}
        return self._post("api/hotspots/assign", params=params)

    def change_hotspot_status(self, hotspot, status, resolution=None, comment=None):
        """
        Change the status of a Security Hotspot.
        :param hotspot: Hotspot key
        :param status: The new status
        :param resolution: The resolution if the new status is "REVIEWED"
        :param comment: A comment to add
        """
        params = {"hotspot": hotspot, "status": status}
        if resolution:
            params["resolution"] = resolution
        if comment:
            params["comment"] = comment
        return self._post("api/hotspots/change_status", params=params)

    def delete_hotspot_comment(self, comment):
        """
        Delete comment from Security Hotspot.
        :param comment: Comment key
        """
        params = {"comment": comment}
        return self._post("api/hotspots/delete_comment", params=params)

    def edit_hotspot_comment(self, comment, text):
        """
        Edit a comment.
        :param comment: Comment key
        :param text: New comment text
        """
        params = {"comment": comment, "text": text}
        return self._post("api/hotspots/edit_comment", params=params)

    def list_hotspots(self, projectKey, p=None, ps=None):
        """
        List Security Hotpots.
        :param projectKey: Project key
        :param p: Page number
        :param ps: Page size
        """
        params = {"projectKey": projectKey}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self._get("api/hotspots/list", params=params)

    def pull_hotspots(self, branch, project):
        """
        Fetch and return all hotspots for a given branch.
        :param branch: Branch key
        :param project: Project key
        """
        params = {"branch": branch, "project": project}
        return self._get("api/hotspots/pull", params=params)

    def search_hotspots(self, projectKey, **kwargs):
        """
        Search for Security Hotspots.
        :param projectKey: Project key
        :param kwargs: Additional parameters
        """
        params = {"projectKey": projectKey}
        params.update(kwargs)
        return self._get("api/hotspots/search", params=params)

    def show_hotspot(self, hotspot):
        """
        Provides the details of a Security Hotspot.
        :param hotspot: Hotspot key
        """
        params = {"hotspot": hotspot}
        return self._get("api/hotspots/show", params=params)

    # SonarQube Languages API
    def list_languages(self, q=None, ps=None):
        """
        List supported programming languages.
        :param q: A pattern to match language keys/names against.
        :param ps: The size of the list to return, 0 for all languages.
        """
        params = {}
        if q:
            params["q"] = q
        if ps:
            params["ps"] = ps
        return self._get("api/languages/list", params=params)

    # SonarQube Measures API
    def get_measures_component(
        self,
        component,
        metricKeys,
        branch=None,
        pullRequest=None,
        additionalFields=None,
    ):
        """
        Return component with specified measures.
        :param component: Component key
        :param metricKeys: Comma-separated list of metric keys
        :param branch: Branch key
        :param pullRequest: Pull request ID
        :param additionalFields: Comma-separated list of additional fields
        """
        params = {"component": component, "metricKeys": metricKeys}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        if additionalFields:
            params["additionalFields"] = additionalFields
        return self._get("api/measures/component", params=params)

    def get_measures_component_tree(self, component, metricKeys, **kwargs):
        """
        Navigate through components based on the chosen strategy with specified measures.
        :param component: Base component key
        :param metricKeys: Comma-separated list of metric keys
        :param kwargs: Additional parameters
        """
        params = {"component": component, "metricKeys": metricKeys}
        params.update(kwargs)
        return self._get("api/measures/component_tree", params=params)

    def search_measures(self, projectKeys, metricKeys, **kwargs):
        """
        Search for project measures ordered by project names.
        :param projectKeys: Comma-separated list of project keys
        :param metricKeys: Comma-separated list of metric keys
        :param kwargs: Additional parameters
        """
        params = {"projectKeys": projectKeys, "metricKeys": metricKeys}
        params.update(kwargs)
        return self._get("api/measures/search", params=params)

    def search_measures_history(self, component, metrics, **kwargs):
        """
        Search measures history of a component.
        :param component: Component key
        :param metrics: Comma-separated list of metric keys
        :param kwargs: Additional parameters
        """
        params = {"component": component, "metrics": metrics}
        params.update(kwargs)
        return self._get("api/measures/search_history", params=params)

    # SonarQube Metrics API
    def search_metrics(self, p=None, ps=None):
        """
        Search for metrics.
        :param p: Page number
        :param ps: Page size
        """
        params = {}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        return self._get("api/metrics/search", params=params)

    def get_metric_types(self):
        """
        List all available metric types.
        """
        return self._get("api/metrics/types")

    # SonarQube Monitoring API
    def get_monitoring_metrics(self):
        """
        Return monitoring metrics in Prometheus format.
        """
        return self._get("api/monitoring/metrics")

    # SonarQube New Code Periods API
    def list_new_code_periods(self, project):
        """
        Lists the new code definition for all branches in a project.
        :param project: Project key
        """
        params = {"project": project}
        return self._get("api/new_code_periods/list", params=params)

    def set_new_code_period(self, project=None, branch=None, type=None, value=None):
        """
        Updates the new code definition on different levels.
        :param project: Project key
        :param branch: Branch key
        :param type: Type of new code definition
        :param value: Value of new code definition
        """
        params = {}
        if project:
            params["project"] = project
        if branch:
            params["branch"] = branch
        if type:
            params["type"] = type
        if value:
            params["value"] = value
        return self._post("api/new_code_periods/set", params=params)

    def show_new_code_period(self, project=None, branch=None):
        """
        Shows the new code definition.
        :param project: Project key
        :param branch: Branch key
        """
        params = {}
        if project:
            params["project"] = project
        if branch:
            params["branch"] = branch
        return self._get("api/new_code_periods/show", params=params)

    def unset_new_code_period(self, project=None, branch=None):
        """
        Unsets the new code definition for a branch, project or global.
        :param project: Project key
        :param branch: Branch key
        """
        params = {}
        if project:
            params["project"] = project
        if branch:
            params["branch"] = branch
        return self._post("api/new_code_periods/unset", params=params)

    # SonarQube Notifications API
    def add_notification(self, login, type, channel=None, project=None):
        """
        Add a notification.
        :param login: User login
        :param type: Notification type
        :param channel: Channel
        :param project: Project key
        """
        params = {"login": login, "type": type}
        if channel:
            params["channel"] = channel
        if project:
            params["project"] = project
        return self._post("api/notifications/add", params=params)

    def list_notifications(self, login=None):
        """
        List notifications.
        :param login: User login
        """
        params = {}
        if login:
            params["login"] = login
        return self._get("api/notifications/list", params=params)

    def remove_notification(self, login, type, channel=None, project=None):
        """
        Remove a notification.
        :param login: User login
        :param type: Notification type
        :param channel: Channel
        :param project: Project key
        """
        params = {"login": login, "type": type}
        if channel:
            params["channel"] = channel
        if project:
            params["project"] = project
        return self._post("api/notifications/remove", params=params)
