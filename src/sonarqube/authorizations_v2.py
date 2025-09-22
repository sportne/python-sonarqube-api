class SonarQubeAuthorizationsV2:
    def __init__(self, client):
        self.client = client

    def add_group_member(self, userId=None, groupId=None):
        """
        Add a user to a group.
        :param userId: ID of the user to add to group.
        :param groupId: ID of the group where a member needs to be added.
        """
        params = {}
        if userId:
            params["userId"] = userId
        if groupId:
            params["groupId"] = groupId
        return self.client._post(
            "/api/v2/authorizations/group-memberships", json=params
        )

    def search_group_members(self, **kwargs):
        """
        Get the list of groups and members matching the query.
        :param kwargs: Additional parameters
        """
        return self.client._get(
            "/api/v2/authorizations/group-memberships", params=kwargs
        )

    def remove_group_member(self, member_id):
        """
        Remove a user from a group.
        :param member_id: The ID of the group membership to delete.
        """
        return self.client._delete(
            f"/api/v2/authorizations/group-memberships/{member_id}"
        )

    def create_group(self, name, description=None):
        """
        Create a new group.
        :param name: Name for the new group.
        :param description: Description for the new group.
        """
        params = {"name": name}
        if description:
            params["description"] = description
        return self.client._post("/api/v2/authorizations/groups", json=params)

    def search_groups(self, **kwargs):
        """
        Get the list of groups.
        :param kwargs: Additional parameters
        """
        return self.client._get("/api/v2/authorizations/groups", params=kwargs)

    def get_group(self, group_id):
        """
        Fetch a single group.
        :param group_id: The id of the group to fetch.
        """
        return self.client._get(f"/api/v2/authorizations/groups/{group_id}")

    def update_group(self, group_id, **kwargs):
        """
        Update a group name or description.
        :param group_id: The id of the group to update.
        :param kwargs: Additional parameters
        """
        return self.client._patch(
            f"/api/v2/authorizations/groups/{group_id}", json=kwargs
        )

    def delete_group(self, group_id):
        """
        Deletes a group.
        :param group_id: The ID of the group to delete.
        """
        return self.client._delete(f"/api/v2/authorizations/groups/{group_id}")
