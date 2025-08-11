import requests


class SonarQube:
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

    # SonarQube Permissions API
    def add_group_to_permission_template(self, template_name, group_name, permission):
        """
        Add a group to a permission template.
        :param template_name: Template name
        :param group_name: Group name
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "groupName": group_name,
            "permission": permission,
        }
        return self._post("api/permissions/add_group_to_template", params=params)

    def add_project_creator_to_permission_template(self, template_name, permission):
        """
        Add a project creator to a permission template.
        :param template_name: Template name
        :param permission: Permission
        """
        params = {"templateName": template_name, "permission": permission}
        return self._post(
            "api/permissions/add_project_creator_to_template", params=params
        )

    def add_user_to_permission_template(self, template_name, login, permission):
        """
        Add a user to a permission template.
        :param template_name: Template name
        :param login: User login
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "login": login,
            "permission": permission,
        }
        return self._post("api/permissions/add_user_to_template", params=params)

    def apply_permission_template_to_project(self, template_name, project_key):
        """
        Apply a permission template to one project.
        :param template_name: Template name
        :param project_key: Project key
        """
        params = {"templateName": template_name, "projectKey": project_key}
        return self._post("api/permissions/apply_template", params=params)

    def bulk_apply_permission_template(self, template_name, **kwargs):
        """
        Apply a permission template to several components.
        :param template_name: Template name
        :param kwargs: Additional parameters
        """
        params = {"templateName": template_name}
        params.update(kwargs)
        return self._post("api/permissions/bulk_apply_template", params=params)

    def create_permission_template(self, name, **kwargs):
        """
        Create a permission template.
        :param name: Template name
        :param kwargs: Additional parameters
        """
        params = {"name": name}
        params.update(kwargs)
        return self._post("api/permissions/create_template", params=params)

    def delete_permission_template(self, template_name):
        """
        Delete a permission template.
        :param template_name: Template name
        """
        params = {"templateName": template_name}
        return self._post("api/permissions/delete_template", params=params)

    def get_permission_groups(self, **kwargs):
        """
        Lists the groups with their permissions.
        :param kwargs: Additional parameters
        """
        return self._get("api/permissions/groups", params=kwargs)

    def remove_group_from_permission_template(
        self, template_name, group_name, permission
    ):
        """
        Remove a group from a permission template.
        :param template_name: Template name
        :param group_name: Group name
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "groupName": group_name,
            "permission": permission,
        }
        return self._post("api/permissions/remove_group_from_template", params=params)

    def remove_project_creator_from_permission_template(
        self, template_name, permission
    ):
        """
        Remove a project creator from a permission template.
        :param template_name: Template name
        :param permission: Permission
        """
        params = {"templateName": template_name, "permission": permission}
        return self._post(
            "api/permissions/remove_project_creator_from_template", params=params
        )

    def remove_user_from_permission_template(self, template_name, login, permission):
        """
        Remove a user from a permission template.
        :param template_name: Template name
        :param login: User login
        :param permission: Permission
        """
        params = {
            "templateName": template_name,
            "login": login,
            "permission": permission,
        }
        return self._post("api/permissions/remove_user_from_template", params=params)

    def search_permission_templates(self, q=None):
        """
        List permission templates.
        :param q: Query to filter templates
        """
        params = {}
        if q:
            params["q"] = q
        return self._get("api/permissions/search_templates", params=params)

    def set_default_permission_template(self, template_name):
        """
        Set a permission template as default.
        :param template_name: Template name
        """
        params = {"templateName": template_name}
        return self._post("api/permissions/set_default_template", params=params)

    def get_permission_template_groups(self, template_name, **kwargs):
        """
        Lists the groups with their permission on the chosen template.
        :param template_name: Template name
        :param kwargs: Additional parameters
        """
        params = {"templateName": template_name}
        params.update(kwargs)
        return self._get("api/permissions/template_groups", params=params)

    def get_permission_template_users(self, template_name, **kwargs):
        """
        Lists the users with their permission on the chosen template.
        :param template_name: Template name
        :param kwargs: Additional parameters
        """
        params = {"templateName": template_name}
        params.update(kwargs)
        return self._get("api/permissions/template_users", params=params)

    def update_permission_template(self, id, **kwargs):
        """
        Update a permission template.
        :param id: Template ID
        :param kwargs: Additional parameters
        """
        params = {"id": id}
        params.update(kwargs)
        return self._post("api/permissions/update_template", params=params)

    def get_permission_users(self, **kwargs):
        """
        Lists the users with their permissions.
        :param kwargs: Additional parameters
        """
        return self._get("api/permissions/users", params=kwargs)

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

    # SonarQube Plugins API
    def get_available_plugins(self):
        """
        Get the list of all the plugins available for installation.
        """
        return self._get("api/plugins/available")

    def cancel_all_pending_plugins(self):
        """
        Cancels any operation pending on any plugin.
        """
        return self._post("api/plugins/cancel_all")

    def download_plugin(self, key):
        """
        Download plugin JAR.
        :param key: Plugin key
        """
        params = {"key": key}
        return self._get("api/plugins/download", params=params)

    def install_plugin(self, key):
        """
        Installs the latest version of a plugin.
        :param key: Plugin key
        """
        params = {"key": key}
        return self._post("api/plugins/install", params=params)

    def get_installed_plugins(self):
        """
        Get the list of all the plugins installed.
        """
        return self._get("api/plugins/installed")

    def get_pending_plugins(self):
        """
        Get the list of plugins with pending operations.
        """
        return self._get("api/plugins/pending")

    def uninstall_plugin(self, key):
        """
        Uninstalls the plugin.
        :param key: Plugin key
        """
        params = {"key": key}
        return self._post("api/plugins/uninstall", params=params)

    def update_plugin(self, key):
        """
        Updates a plugin.
        :param key: Plugin key
        """
        params = {"key": key}
        return self._post("api/plugins/update", params=params)

    def get_plugin_updates(self):
        """
        Lists plugins with available updates.
        """
        return self._get("api/plugins/updates")

    # SonarQube Project Analyses API
    def create_project_analysis_event(self, analysis, name, category=None):
        """
        Create a project analysis event.
        :param analysis: Analysis key
        :param name: Event name
        :param category: Event category
        """
        params = {"analysis": analysis, "name": name}
        if category:
            params["category"] = category
        return self._post("api/project_analyses/create_event", params=params)

    def delete_project_analysis(self, analysis):
        """
        Delete a project analysis.
        :param analysis: Analysis key
        """
        params = {"analysis": analysis}
        return self._post("api/project_analyses/delete", params=params)

    def delete_project_analysis_event(self, event):
        """
        Delete a project analysis event.
        :param event: Event key
        """
        params = {"event": event}
        return self._post("api/project_analyses/delete_event", params=params)

    def search_project_analyses(self, project, **kwargs):
        """
        Search a project analyses and attached events.
        :param project: Project key
        :param kwargs: Additional parameters
        """
        params = {"project": project}
        params.update(kwargs)
        return self._get("api/project_analyses/search", params=params)

    def update_project_analysis_event(self, event, name):
        """
        Update a project analysis event.
        :param event: Event key
        :param name: New name
        """
        params = {"event": event, "name": name}
        return self._post("api/project_analyses/update_event", params=params)

    # SonarQube Project Badges API
    def get_project_badge_ai_code_assurance(self, project, branch=None):
        """
        Generate a badge for project's AI assurance as an SVG.
        :param project: Project key
        :param branch: Branch key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        return self._get("api/project_badges/ai_code_assurance", params=params)

    def get_project_badge_measure(self, project, metric, branch=None):
        """
        Generate badge for project's measure as an SVG.
        :param project: Project key
        :param metric: Metric key
        :param branch: Branch key
        """
        params = {"project": project, "metric": metric}
        if branch:
            params["branch"] = branch
        return self._get("api/project_badges/measure", params=params)

    def get_project_badge_quality_gate(self, project, branch=None):
        """
        Generate badge for project's quality gate as an SVG.
        :param project: Project key
        :param branch: Branch key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        return self._get("api/project_badges/quality_gate", params=params)

    def renew_project_badge_token(self, project):
        """
        Creates new token replacing any existing token for project badge access.
        :param project: Project key
        """
        params = {"project": project}
        return self._post("api/project_badges/renew_token", params=params)

    def get_project_badge_token(self, project):
        """
        Retrieve a token to use for project badge access.
        :param project: Project key
        """
        params = {"project": project}
        return self._get("api/project_badges/token", params=params)

    # SonarQube Project Branches API
    def delete_project_branch(self, project, branch):
        """
        Delete a non-main branch of a project.
        :param project: Project key
        :param branch: Branch name
        """
        params = {"project": project, "branch": branch}
        return self._post("api/project_branches/delete", params=params)

    def get_project_branch_ai_code_assurance(self, project, branch=None):
        """
        Gets whether a project passed as parameter is AI Code Assured or not.
        :param project: Project key
        :param branch: Branch key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        return self._get("api/project_branches/get_ai_code_assurance", params=params)

    def list_project_branches(self, project):
        """
        List the branches of a project.
        :param project: Project key
        """
        params = {"project": project}
        return self._get("api/project_branches/list", params=params)

    def rename_project_branch(self, project, name):
        """
        Rename the main branch of a project.
        :param project: Project key
        :param name: New branch name
        """
        params = {"project": project, "name": name}
        return self._post("api/project_branches/rename", params=params)

    def set_project_branch_automatic_deletion_protection(
        self, project, branch, is_protected
    ):
        """
        Protect a specific branch from automatic deletion.
        :param project: Project key
        :param branch: Branch name
        :param is_protected: Boolean indicating if the branch should be protected
        """
        params = {"project": project, "branch": branch, "isProtected": is_protected}
        return self._post(
            "api/project_branches/set_automatic_deletion_protection", params=params
        )

    def set_project_main_branch(self, project, branch):
        """
        Allow to set a new main branch.
        :param project: Project key
        :param branch: Branch name
        """
        params = {"project": project, "branch": branch}
        return self._post("api/project_branches/set_main", params=params)

    # SonarQube Project Dump API
    def export_project_dump(self, project, projectKey=None):
        """
        Triggers project dump so that the project can be imported to another SonarQube server.
        :param project: Project key
        :param projectKey: Project key (optional)
        """
        params = {"project": project}
        if projectKey:
            params["projectKey"] = projectKey
        return self._post("api/project_dump/export", params=params)

    def import_project_dump(self, file, project=None, projectKey=None):
        """
        Triggers the import of a project dump.
        :param file: Path to the project dump file
        :param project: Project key (optional)
        :param projectKey: Project key (optional)
        """
        params = {}
        if project:
            params["project"] = project
        if projectKey:
            params["projectKey"] = projectKey
        with open(file, "rb") as f:
            files = {"file": f}
            return self._post("api/project_dump/import", params=params, files=files)

    def get_project_dump_status(self, project=None, projectKey=None, id=None):
        """
        Provide the import and export status of a project.
        :param project: Project key (optional)
        :param projectKey: Project key (optional)
        :param id: Project id (optional)
        """
        params = {}
        if project:
            params["project"] = project
        if projectKey:
            params["projectKey"] = projectKey
        if id:
            params["id"] = id
        return self._get("api/project_dump/status", params=params)

    # SonarQube Project Links API
    def create_project_link(self, projectId, name, url):
        """
        Create a new project link.
        :param projectId: Project Id
        :param name: Link name
        :param url: Link url
        """
        params = {"projectId": projectId, "name": name, "url": url}
        return self._post("api/project_links/create", params=params)

    def delete_project_link(self, id):
        """
        Delete existing project link.
        :param id: Link ID
        """
        params = {"id": id}
        return self._post("api/project_links/delete", params=params)

    def search_project_links(self, projectId):
        """
        List links of a project.
        :param projectId: Project Id
        """
        params = {"projectId": projectId}
        return self._get("api/project_links/search", params=params)

    # SonarQube Project Pull Requests API
    def delete_project_pull_request(self, project, pullRequest):
        """
        Delete a pull request.
        :param project: Project key
        :param pullRequest: Pull request key
        """
        params = {"project": project, "pullRequest": pullRequest}
        return self._post("api/project_pull_requests/delete", params=params)

    def list_project_pull_requests(self, project):
        """
        List the pull requests of a project.
        :param project: Project key
        """
        params = {"project": project}
        return self._get("api/project_pull_requests/list", params=params)

    # SonarQube Project Tags API
    def search_project_tags(self, q=None):
        """
        Search tags
        :param q: Limit search to tags that contain the supplied string.
        """
        params = {}
        if q:
            params["q"] = q
        return self._get("api/project_tags/search", params=params)

    def set_project_tags(self, project, tags):
        """
        Set tags on a project.
        :param project: Project key
        :param tags: Comma-separated list of tags
        """
        params = {"project": project, "tags": tags}
        return self._post("api/project_tags/set", params=params)

    # SonarQube Projects API
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

    def bulk_delete_projects(self, analyzedBefore=None, projects=None, q=None):
        """
        Delete one or several projects.
        :param analyzedBefore: Delete projects analyzed before the given date (inclusive).
        :param projects: Comma-separated list of project keys
        :param q: Query string
        """
        params = {}
        if analyzedBefore:
            params["analyzedBefore"] = analyzedBefore
        if projects:
            params["projects"] = projects
        if q:
            params["q"] = q
        return self._post("api/projects/bulk_delete", params=params)

    def export_project_findings(self, project, branch=None, pullRequest=None):
        """
        Export all findings (issues and hotspots) of a specific project branch.
        :param project: Project key
        :param branch: Branch key
        :param pullRequest: Pull request key
        """
        params = {"project": project}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self._get("api/projects/export_findings", params=params)

    def get_project_contains_ai_code(self, project):
        """
        Get whether a project contains AI code or not
        :param project: Project key
        """
        params = {"project": project}
        return self._get("api/projects/get_contains_ai_code", params=params)

    def get_project_detected_ai_code(self, project):
        """
        Get detected AI code
        :param project: Project key
        """
        params = {"project": project}
        return self._get("api/projects/get_detected_ai_code", params=params)

    def get_project_license_usage(self):
        """
        Help admins to understand how much each project affects the total number of lines of code.
        """
        return self._get("api/projects/license_usage")

    def search_my_projects(self, organization=None):
        """
        Return list of projects for which the current user has 'Administer' permission.
        :param organization: Organization key
        """
        params = {}
        if organization:
            params["organization"] = organization
        return self._get("api/projects/search_my_projects", params=params)

    def search_my_scannable_projects(self, organization=None):
        """
        List projects that a user can scan.
        :param organization: Organization key
        """
        params = {}
        if organization:
            params["organization"] = organization
        return self._get("api/projects/search_my_scannable_projects", params=params)

    def set_project_contains_ai_code(self, project, contains_ai_code):
        """
        Sets if the project passed as parameter contains or not AI code according to the value of the contains_ai_code parameter.
        :param project: Project key
        :param contains_ai_code: Boolean indicating if the project contains AI code
        """
        params = {"project": project, "contains_ai_code": contains_ai_code}
        return self._post("api/projects/set_contains_ai_code", params=params)

    def update_project_default_visibility(self, visibility):
        """
        Update the default visibility for new projects.
        :param visibility: New visibility (private or public)
        """
        params = {"visibility": visibility}
        return self._post("api/projects/update_default_visibility", params=params)

    def update_project_key(self, project, new_key):
        """
        Update a project all its sub-components keys.
        :param project: Project key
        :param new_key: New project key
        """
        params = {"from": project, "to": new_key}
        return self._post("api/projects/update_key", params=params)

    def update_project_visibility(self, project, visibility):
        """
        Updates visibility of a project, application or a portfolio.
        :param project: Project, application or portfolio key
        :param visibility: New visibility (private or public)
        """
        params = {"project": project, "visibility": visibility}
        return self._post("api/projects/update_visibility", params=params)
