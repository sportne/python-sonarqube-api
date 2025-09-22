class SonarQubeViews:
    def __init__(self, client):
        self.client = client

    def add_application_to_portfolio(self, application, portfolio):
        """
        Add an existing application to a portfolio.
        :param application: Key of the application to be added
        :param portfolio: Key of the portfolio where the application will be added
        """
        params = {"application": application, "portfolio": portfolio}
        return self.client._post("api/views/add_application", params=params)

    def add_application_branch(self, application, branch, key):
        """
        Add a branch of an application selected in a portfolio.
        :param application: Key of the application.
        :param branch: Key of the branch.
        :param key: Key of the portfolio
        """
        params = {"application": application, "branch": branch, "key": key}
        return self.client._post("api/views/add_application_branch", params=params)

    def add_portfolio_to_portfolio(self, portfolio, reference):
        """
        Add an existing portfolio to the structure of another portfolio.
        :param portfolio: Key of the portfolio where a reference will be added
        :param reference: Key of the portfolio to be added
        """
        params = {"portfolio": portfolio, "reference": reference}
        return self.client._post("api/views/add_portfolio", params=params)

    def add_project_to_portfolio(self, key, project):
        """
        Add a project to a portfolio.
        :param key: Key of the portfolio
        :param project: Key of the project.
        """
        params = {"key": key, "project": project}
        return self.client._post("api/views/add_project", params=params)

    def add_project_branch(self, branch, key, project):
        """
        Add a branch of a project selected in a portfolio.
        :param branch: Key of the branch.
        :param key: Key of the portfolio
        :param project: Key of the project.
        """
        params = {"branch": branch, "key": key, "project": project}
        return self.client._post("api/views/add_project_branch", params=params)

    def list_applications_for_portfolio(self, portfolio):
        """
        List applications which the user has access to that can be added to a portfolio.
        :param portfolio: Key of the would-be parent portfolio
        """
        params = {"portfolio": portfolio}
        return self.client._get("api/views/applications", params=params)

    def create_portfolio(
        self, name, description=None, key=None, parent=None, visibility=None
    ):
        """
        Create a new portfolio.
        :param name: Name for the new portfolio.
        :param description: Description for the new portfolio.
        :param key: Key for the new portfolio.
        :param parent: Key of the parent portfolio.
        :param visibility: Whether the created portfolio should be visible to everyone, or only specific user/groups.
        """
        params = {"name": name}
        if description:
            params["description"] = description
        if key:
            params["key"] = key
        if parent:
            params["parent"] = parent
        if visibility:
            params["visibility"] = visibility
        return self.client._post("api/views/create", params=params)

    def delete_portfolio(self, key):
        """
        Delete a portfolio definition.
        :param key: Portfolio key
        """
        params = {"key": key}
        return self.client._post("api/views/delete", params=params)

    def list_portfolios(self):
        """
        List root portfolios.
        """
        return self.client._get("api/views/list")

    def move_portfolio(self, destination, key):
        """
        Move a portfolio.
        :param destination: Key of the destination portfolio
        :param key: Key of the portfolio to move
        """
        params = {"destination": destination, "key": key}
        return self.client._post("api/views/move", params=params)

    def list_move_options(self, key):
        """
        List possible portfolio destinations.
        :param key: Key of the portfolio to move
        """
        params = {"key": key}
        return self.client._get("api/views/move_options", params=params)

    def list_portfolios_for_portfolio(self, portfolio):
        """
        List portfolios that can be referenced.
        :param portfolio: Key of the would-be parent portfolio
        """
        params = {"portfolio": portfolio}
        return self.client._get("api/views/portfolios", params=params)

    def list_projects_in_portfolio(
        self, key, p=None, ps=None, query=None, selected=None
    ):
        """
        List projects manually selected in a portfolio.
        :param key: Portfolio key
        :param p: Index of the page to display.
        :param ps: Size for the paging to apply.
        :param query: If specified, only projects whose key contain the query will be returned
        :param selected: Depending on the value, show only selected items, deselected items, or all items.
        """
        params = {"key": key}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        if query:
            params["query"] = query
        if selected:
            params["selected"] = selected
        return self.client._get("api/views/projects", params=params)

    def list_projects_status_in_portfolio(
        self, portfolio, p=None, ps=None, status=None
    ):
        """
        Return projects with a failed quality gate belonging to the provided portfolio hierarchy.
        :param portfolio: Portfolio key.
        :param p: 1-based page number.
        :param ps: Page size.
        :param status: Quality gate status to filter projects by.
        """
        params = {"portfolio": portfolio}
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        if status:
            params["status"] = status
        return self.client._get("api/views/projects_status", params=params)

    def refresh_portfolio(self, key=None):
        """
        Refresh one or all of the portfolios.
        :param key: Root portfolio key.
        """
        params = {}
        if key:
            params["key"] = key
        return self.client._post("api/views/refresh", params=params)

    def remove_application_from_portfolio(self, application, portfolio):
        """
        Remove an application from a portfolio.
        :param application: Key of the application to be removed
        :param portfolio: Portfolio key
        """
        params = {"application": application, "portfolio": portfolio}
        return self.client._post("api/views/remove_application", params=params)

    def remove_application_branch(self, application, branch, key):
        """
        Remove a branch of an application selected in a portfolio.
        :param application: Key of the project.
        :param branch: Key of the branch.
        :param key: Key of the portfolio
        """
        params = {"application": application, "branch": branch, "key": key}
        return self.client._post("api/views/remove_application_branch", params=params)

    def remove_portfolio_from_portfolio(self, portfolio, reference):
        """
        Remove a reference to a portfolio.
        :param portfolio: Portfolio key
        :param reference: Key of the referenced portfolio to be removed
        """
        params = {"portfolio": portfolio, "reference": reference}
        return self.client._post("api/views/remove_portfolio", params=params)

    def remove_project_from_portfolio(self, key, project):
        """
        Remove a project from a portfolio.
        :param key: Key of the portfolio
        :param project: Key of the project
        """
        params = {"key": key, "project": project}
        return self.client._post("api/views/remove_project", params=params)

    def remove_project_branch(self, branch, key, project):
        """
        Remove a branch of a project selected in a portfolio.
        :param branch: Key of the branch.
        :param key: Key of the portfolio
        :param project: Key of the project.
        """
        params = {"branch": branch, "key": key, "project": project}
        return self.client._post("api/views/remove_project_branch", params=params)

    def search_portfolios(
        self, onlyFavorites=None, p=None, ps=None, q=None, qualifiers=None
    ):
        """
        Search for portfolios.
        :param onlyFavorites: To return only favorite portfolios.
        :param p: 1-based page number.
        :param ps: Page size.
        :param q: Limit search to names or keys that contain the supplied string.
        :param qualifiers: To return only portfolios with specified qualifiers.
        """
        params = {}
        if onlyFavorites:
            params["onlyFavorites"] = onlyFavorites
        if p:
            params["p"] = p
        if ps:
            params["ps"] = ps
        if q:
            params["q"] = q
        if qualifiers:
            params["qualifiers"] = qualifiers
        return self.client._get("api/views/search", params=params)

    def set_manual_mode(self, portfolio):
        """
        Set the projects selection mode of a portfolio on manual selection.
        :param portfolio: Key of the portfolio or sub-portfolio to update
        """
        params = {"portfolio": portfolio}
        return self.client._post("api/views/set_manual_mode", params=params)

    def set_none_mode(self, portfolio):
        """
        Set the projects selection mode of a portfolio to none.
        :param portfolio: Key of the portfolio or sub-portfolio to update
        """
        params = {"portfolio": portfolio}
        return self.client._post("api/views/set_none_mode", params=params)

    def set_regexp_mode(self, portfolio, regexp, branch=None):
        """
        Set the projects selection mode of a portfolio on regular expression.
        :param portfolio: Key of the portfolio or sub-portfolio to update
        :param regexp: A valid regexp.
        :param branch: Selects a branch in all matched projects.
        """
        params = {"portfolio": portfolio, "regexp": regexp}
        if branch:
            params["branch"] = branch
        return self.client._post("api/views/set_regexp_mode", params=params)

    def set_remaining_projects_mode(self, portfolio, branch=None):
        """
        Set the projects selection mode of a portfolio on unassociated projects in hierarchy.
        :param portfolio: Key of the portfolio or sub-portfolio to update
        :param branch: Selects a branch in all matched projects.
        """
        params = {"portfolio": portfolio}
        if branch:
            params["branch"] = branch
        return self.client._post("api/views/set_remaining_projects_mode", params=params)

    def set_tags_mode(self, portfolio, tags, branch=None):
        """
        Set the projects selection mode of a portfolio on project tags.
        :param portfolio: Key of the portfolio or sub-portfolio to update
        :param tags: Comma-separated list of tags.
        :param branch: Selects a branch in all matched projects.
        """
        params = {"portfolio": portfolio, "tags": tags}
        if branch:
            params["branch"] = branch
        return self.client._post("api/views/set_tags_mode", params=params)

    def show_portfolio(self, key):
        """
        Show the details of a portfolio.
        :param key: The key of the portfolio
        """
        params = {"key": key}
        return self.client._get("api/views/show", params=params)

    def update_portfolio(self, key, name, description=None):
        """
        Update a portfolio.
        :param key: Key of the portfolio to update
        :param name: New name for the portfolio.
        :param description: New description for the portfolio.
        """
        params = {"key": key, "name": name}
        if description:
            params["description"] = description
        return self.client._post("api/views/update", params=params)
