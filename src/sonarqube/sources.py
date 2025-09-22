class SonarQubeSources:
    def __init__(self, client):
        self.client = client

    def get_sources_index(self, resource, from_line=None, to_line=None):
        """
        Get source code as line number / text pairs.
        :param resource: File key.
        :param from_line: First line. Default value: 1
        :param to_line: Last line (excluded). If not specified, all lines are returned until end of file
        :return:
        """
        params = {"resource": resource}
        if from_line:
            params["from"] = from_line
        if to_line:
            params["to"] = to_line
        return self.client._get("api/sources/index", params=params)

    def get_issue_snippets(self, issueKey):
        """
        Get code snippets involved in an issue or hotspot.
        :param issueKey: Issue or hotspot key.
        :return:
        """
        params = {"issueKey": issueKey}
        return self.client._get("api/sources/issue_snippets", params=params)

    def get_sources_lines(
        self,
        key,
        from_line=None,
        to_line=None,
        pullRequest=None,
        branch=None,
        uuid=None,
    ):
        """
        Show source code with line oriented info.
        :param key: File key. Mandatory if param 'uuid' is not set.
        :param from_line: First line to return. Starts from 1. Default value: 1.
        :param to_line: Optional last line to return (inclusive).
        :param pullRequest: Pull request id.
        :param branch: Branch key.
        :param uuid: File uuid. Mandatory if param 'key' is not set.
        :return:
        """
        params = {}
        if key:
            params["key"] = key
        if from_line:
            params["from"] = from_line
        if to_line:
            params["to"] = to_line
        if pullRequest:
            params["pullRequest"] = pullRequest
        if branch:
            params["branch"] = branch
        if uuid:
            params["uuid"] = uuid
        return self.client._get("api/sources/lines", params=params)

    def get_sources_raw(self, key, branch=None, pullRequest=None):
        """
        Get source code as raw text.
        :param key: File key.
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :return:
        """
        params = {"key": key}
        if branch:
            params["branch"] = branch
        if pullRequest:
            params["pullRequest"] = pullRequest
        return self.client._get("api/sources/raw", params=params)

    def get_sources_scm(self, key, from_line=None, to_line=None, commits_by_line=None):
        """
        Get SCM information of source files.
        :param key: File key.
        :param from_line: First line to return. Starts at 1. Default value: 1.
        :param to_line: Last line to return (inclusive).
        :param commits_by_line: Group lines by SCM commit if value is false, else display commits for each line.
        :return:
        """
        params = {"key": key}
        if from_line:
            params["from"] = from_line
        if to_line:
            params["to"] = to_line
        if commits_by_line:
            params["commits_by_line"] = commits_by_line
        return self.client._get("api/sources/scm", params=params)

    def get_sources_show(self, key, from_line=None, to_line=None):
        """
        Get source code.
        :param key: File key.
        :param from_line: First line to return. Starts at 1. Default value: 1.
        :param to_line: Last line to return (inclusive).
        :return:
        """
        params = {"key": key}
        if from_line:
            params["from"] = from_line
        if to_line:
            params["to"] = to_line
        return self.client._get("api/sources/show", params=params)
