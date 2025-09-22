[Back to Index](index.md)

# Quality Profiles

### `POST api/qualityprofiles/activate_rule`
*since 4.4*

Activate a rule on a Quality Profile. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `rule` (required): Rule key.

---

### `POST api/qualityprofiles/activate_rules`
*since 4.4*

Bulk-activate rules on one quality profile. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `rules` (required): Comma-separated list of rule keys.

---

### `POST api/qualityprofiles/add_group`
*internal since 6.6*

Allow a group to edit a Quality Profile. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `groupName` (required): Group name.

---

### `POST api/qualityprofiles/add_project`
*since 5.2*

Associate a project with a quality profile. Requires 'Administer Quality Profiles' or 'Administer' right on the project.

**Parameters**
- `qualityProfile` (required): Quality profile name.
- `language` (required): Language key.
- `project` (required): Project key.

---

### `POST api/qualityprofiles/add_user`
*internal since 6.6*

Allow a user to edit a Quality Profile. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `login` (required): User login.

---

### `GET api/qualityprofiles/backup`
*since 5.2*

Backup a quality profile in XML form.

**Parameters**
- `qualityProfile` (required): Quality profile name.
- `language` (required): Language key.

---

### `POST api/qualityprofiles/change_parent`
*since 5.2*

Change a quality profile's parent. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `parentKey` (required): Parent quality profile key.

---

### `GET api/qualityprofiles/changelog`
*since 5.2*

Get the history of changes on a quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `p`, `ps` (optional): Pagination.

---

### `GET api/qualityprofiles/compare`
*internal since 5.2*

Compare two quality profiles.

**Parameters**
- `fromKey` (required): From quality profile key.
- `toKey` (required): To quality profile key.

---

### `POST api/qualityprofiles/copy`
*since 5.2*

Copy a quality profile. Requires 'Administer Quality Profiles' permission.

**Parameters**
- `fromKey` (required): Source quality profile key.
- `toName` (required): New quality profile name.

---

### `POST api/qualityprofiles/create`
*since 5.2*

Create a quality profile. Requires 'Administer Quality Profiles' permission.

**Parameters**
- `name` (required): Quality profile name.
- `language` (required): Language key.

---

### `POST api/qualityprofiles/deactivate_rule`
*since 4.4*

Deactivate a rule on a quality profile. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `rule` (required): Rule key.

---

### `POST api/qualityprofiles/deactivate_rules`
*since 4.4*

Bulk deactivate rules on Quality profiles. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `rules` (required): Comma-separated list of rule keys.

---

### `POST api/qualityprofiles/delete`
*since 5.2*

Delete a quality profile and all its descendants. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.

---

### `GET api/qualityprofiles/inheritance`
*since 5.2*

Show a quality profile's ancestors and children.

**Parameters**
- `key` (required): Quality profile key.

---

### `GET api/qualityprofiles/projects`
*since 5.2*

List projects with their association status regarding a quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `p`, `ps` (optional): Pagination.

---

### `POST api/qualityprofiles/remove_group`
*internal since 6.6*

Remove the ability from a group to edit a Quality Profile.

**Parameters**
- `key` (required): Quality profile key.
- `groupName` (required): Group name.

---

### `POST api/qualityprofiles/remove_project`
*since 5.2*

Remove a project's association with a quality profile.

**Parameters**
- `qualityProfile` (required): Quality profile name.
- `language` (required): Language key.
- `project` (required): Project key.

---

### `POST api/qualityprofiles/remove_user`
*internal since 6.6*

Remove the ability from a user to edit a Quality Profile.

**Parameters**
- `key` (required): Quality profile key.
- `login` (required): User login.

---

### `POST api/qualityprofiles/rename`
*since 5.2*

Rename a quality profile. Requires 'Administer Quality Profiles' or edit right on the specified quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `name` (required): New name.

---

### `POST api/qualityprofiles/restore`
*since 5.2*

Restore a quality profile using an XML file. Requires 'Administer Quality Profiles' permission.

**Parameters**
- `backup` (required): The XML file.

---

### `GET api/qualityprofiles/search`
*since 5.2*

Search quality profiles.

**Parameters**
- `qualityProfile` (optional): Quality profile name.
- `language` (optional): Language key.
- `project` (optional): Project key.

---

### `GET api/qualityprofiles/search_groups`
*internal since 6.6*

List the groups that are allowed to edit a Quality Profile.

**Parameters**
- `key` (required): Quality profile key.
- `q` (optional): Query.
- `p`, `ps` (optional): Pagination.

---

### `GET api/qualityprofiles/search_users`
*internal since 6.6*

List the users that are allowed to edit a Quality Profile.

**Parameters**
- `key` (required): Quality profile key.
- `q` (optional): Query.
- `p`, `ps` (optional): Pagination.

---

### `POST api/qualityprofiles/set_default`
*since 5.2*

Select the default profile for a given language. Requires 'Administer Quality Profiles' permission.

**Parameters**
- `qualityProfile` (required): Quality profile name.
- `language` (required): Language key.

---

### `GET api/qualityprofiles/show`
*internal since 6.5*

Show a quality profile.

**Parameters**
- `key` (required): Quality profile key.
- `compareToSonarWay` (optional): Compare with Sonar way profile.
