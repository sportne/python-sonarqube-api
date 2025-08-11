# python-sonarqube-api

A Python wrapper for the Sonarqube Web API that allows you to easily interact with your SonarQube instance. This library will provide access to the full functionality of the SonarQube API, allowing you to automate tasks, extract data, and integrate SonarQube into your existing workflows.

## Features Checklist

This is a list of features that need to be implemented to consider this a complete SonarQube Python API client.

### Applications
- [x] Add a project to an application (`api/applications/add_project`)
- [x] Create a new application (`api/applications/create`)
- [x] Create a new branch on a given application (`api/applications/create_branch`)
- [x] Delete an application definition (`api/applications/delete`)
- [x] Delete a branch on a given application (`api/applications/delete_branch`)
- [x] Refresh one or all applications (`api/applications/refresh`)
- [x] Remove a project from an application (`api/applications/remove_project`)
- [x] List projects manually selected in an application (`api/applications/search_projects`)
- [x] Set tags on a application (`api/applications/set_tags`)
- [x] Returns an application and its associated projects (`api/applications/show`)
- [x] Show leak of an application (`api/applications/show_leak`)
- [x] Update an application (`api/applications/update`)
- [x] Update a branch on a given application (`api/applications/update_branch`)

### Authentication
- [x] Authenticate a user (`api/authentication/login`)
- [x] Logout a user (`api/authentication/logout`)
- [x] Check credentials (`api/authentication/validate`)

### Compute Engine (CE)
- [x] Search for tasks (`api/ce/activity`)
- [x] Returns CE activity related metrics (`api/ce/activity_status`)
- [x] Get the analysis status of a given component (`api/ce/analysis_status`)
- [x] Cancels a pending task (`api/ce/cancel`)
- [x] Cancels all pending tasks (`api/ce/cancel_all`)
- [x] Get the pending tasks, in-progress tasks and the last executed task of a given component (`api/ce/component`)
- [x] Permanently dismiss a specific analysis warning (`api/ce/dismiss_analysis_warning`)
- [x] Returns the count of projects with completed issue indexing (`api/ce/indexation_status`)
- [x] Gets information about Compute Engine (`api/ce/info`)
- [x] Requests pause of Compute Engine workers (`api/ce/pause`)
- [x] Resumes pause of Compute Engine workers (`api/ce/resume`)
- [x] Set the number of workers in the Compute Engine (`api/ce/set_worker_count`)
- [x] Submits a scanner report to the queue (`api/ce/submit`)
- [x] Give Compute Engine task details (`api/ce/task`)
- [x] List available task types (`api/ce/task_types`)
- [x] Return number of Compute Engine workers (`api/ce/worker_count`)

### Components
- [x] Coverage data required for rendering the component viewer (`api/components/app`)
- [x] Search for components (`api/components/search`)
- [x] Search for projects (`api/components/search_projects`)
- [x] Returns a component and its ancestors (`api/components/show`)
- [x] Internal WS for the top-right search engine (`api/components/suggestions`)
- [x] Navigate through components based on the chosen strategy (`api/components/tree`)

### Duplications
- [x] Get duplications (`api/duplications/show`)

### Editions
- [x] Enable a license 7-days grace period if the Server ID is invalid (`api/editions/activate_grace_period`)
- [x] Return the validity of the license (`api/editions/is_valid_license`)
- [x] Set the license for enabling features of commercial editions (`api/editions/set_license`)
- [x] Show information about currently installed license (`api/editions/show_license`)
- [x] Un-sets license (`api/editions/unset_license`)

### Favorites
- [x] Add a component as favorite (`api/favorites/add`)
- [x] Remove a component as favorite (`api/favorites/remove`)
- [x] Search for favorites (`api/favorites/search`)

### Hotspots
- [ ] Add a comment to a Security Hotspot (`api/hotspots/add_comment`)
- [ ] Assign a hotspot to an active user (`api/hotspots/assign`)
- [ ] Change the status of a Security Hotspot (`api/hotspots/change_status`)
- [ ] Delete comment from Security Hotspot (`api/hotspots/delete_comment`)
- [ ] Edit a comment (`api/hotspots/edit_comment`)
- [ ] List Security Hotpots (`api/hotspots/list`)
- [ ] Fetch and return all hotspots for a given branch (`api/hotspots/pull`)
- [ ] Search for Security Hotpots (`api/hotspots/search`)
- [ ] Provides the details of a Security Hotspot (`api/hotspots/show`)

### Issues
- [x] Add a comment (`api/issues/add_comment`)
- [ ] Receive a list of anticipated transitions (`api/issues/anticipated_transitions`)
- [x] Assign/Unassign an issue (`api/issues/assign`)
- [x] Search SCM accounts (`api/issues/authors`)
- [x] Bulk change on issues (`api/issues/bulk_change`)
- [x] Display changelog of an issue (`api/issues/changelog`)
- [ ] List tags for the issues under a given component (`api/issues/component_tags`)
- [x] Delete a comment (`api/issues/delete_comment`)
- [x] Do workflow transition on an issue (`api/issues/do_transition`)
- [x] Edit a comment (`api/issues/edit_comment`)
- [ ] Return a list of vulnerabilities in Gitlab SAST format (`api/issues/gitlab_sast_export`)
- [ ] List issues in degraded mode (`api/issues/list`)
- [ ] Fetch and return all issues for a given branch (`api/issues/pull`)
- [ ] Fetch and return all taint vulnerabilities for a given branch (`api/issues/pull_taint`)
- [ ] Reindex issues for a project (`api/issues/reindex`)
- [x] Search for issues (`api/issues/search`)
- [x] Change severity (`api/issues/set_severity`)
- [x] Set tags on an issue (`api/issues/set_tags`)
- [x] List tags matching a given query (`api/issues/tags`)

### Languages
- [ ] List supported programming languages (`api/languages/list`)

### Measures
- [ ] Return component with specified measures (`api/measures/component`)
- [ ] Navigate through components with specified measures (`api/measures/component_tree`)
- [ ] Search for project measures (`api/measures/search`)
- [ ] Search measures history of a component (`api/measures/search_history`)

### Metrics
- [ ] Search for metrics (`api/metrics/search`)
- [ ] List all available metric types (`api/metrics/types`)

### Monitoring
- [ ] Return monitoring metrics in Prometheus format (`api/monitoring/metrics`)

### New Code Periods
- [ ] Lists the new code definition for all branches in a project (`api/new_code_periods/list`)
- [ ] Updates the new code definition (`api/new_code_periods/set`)
- [ ] Shows the new code definition (`api/new_code_periods/show`)
- [ ] Unsets the new code definition (`api/new_code_periods/unset`)

### Notifications
- [ ] Add a notification (`api/notifications/add`)
- [ ] List notifications (`api/notifications/list`)
- [ ] Remove a notification (`api/notifications/remove`)

### Permissions
- [ ] Add a permission to a group (`api/permissions/add_group`)
- [ ] Add a group to a permission template (`api/permissions/add_group_to_template`)
- [ ] Add a project creator to a permission template (`api/permissions/add_project_creator_to_template`)
- [ ] Add permission to a user (`api/permissions/add_user`)
- [ ] Add a user to a permission template (`api/permissions/add_user_to_template`)
- [ ] Apply a permission template to one project (`api/permissions/apply_template`)
- [ ] Apply a permission template to several components (`api/permissions/bulk_apply_template`)
- [ ] Create a permission template (`api/permissions/create_template`)
- [ ] Delete a permission template (`api/permissions/delete_template`)
- [ ] Lists the groups with their permissions (`api/permissions/groups`)
- [ ] Remove a permission from a group (`api/permissions/remove_group`)
- [ ] Remove a group from a permission template (`api/permissions/remove_group_from_template`)
- [ ] Remove a project creator from a permission template (`api/permissions/remove_project_creator_from_template`)
- [ ] Remove permission from a user (`api/permissions/remove_user`)
- [ ] Remove a user from a permission template (`api/permissions/remove_user_from_template`)
- [ ] List permission templates (`api/permissions/search_templates`)
- [ ] Set a permission template as default (`api/permissions/set_default_template`)
- [ ] Lists the groups with their permission on a template (`api/permissions/template_groups`)
- [ ] Lists the users with their permission on a template (`api/permissions/template_users`)
- [ ] Update a permission template (`api/permissions/update_template`)
- [ ] Lists the users with their permissions (`api/permissions/users`)

### Plugins
- [ ] Get the list of all the plugins available for installation (`api/plugins/available`)
- [ ] Cancels any operation pending on any plugin (`api/plugins/cancel_all`)
- [ ] Download plugin JAR (`api/plugins/download`)
- [ ] Installs the latest version of a plugin (`api/plugins/install`)
- [ ] Get the list of all the plugins installed (`api/plugins/installed`)
- [ ] Get the list of plugins with pending operations (`api/plugins/pending`)
- [ ] Uninstalls the plugin (`api/plugins/uninstall`)
- [ ] Updates a plugin (`api/plugins/update`)
- [ ] Lists plugins with available updates (`api/plugins/updates`)

### Project Analyses
- [ ] Create a project analysis event (`api/project_analyses/create_event`)
- [ ] Delete a project analysis (`api/project_analyses/delete`)
- [ ] Delete a project analysis event (`api/project_analyses/delete_event`)
- [ ] Search a project analyses and attached events (`api/project_analyses/search`)
- [ ] Update a project analysis event (`api/project_analyses/update_event`)

### Project Badges
- [ ] Generate a badge for project's AI assurance (`api/project_badges/ai_code_assurance`)
- [ ] Generate badge for project's measure (`api/project_badges/measure`)
- [ ] Generate badge for project's quality gate (`api/project_badges/quality_gate`)
- [ ] Creates new token for project badge access (`api/project_badges/renew_token`)
- [ ] Retrieve a token for project badge access (`api/project_badges/token`)

### Project Branches
- [ ] Delete a non-main branch (`api/project_branches/delete`)
- [ ] Gets whether a project is AI Code Assured (`api/project_branches/get_ai_code_assurance`)
- [ ] List the branches of a project (`api/project_branches/list`)
- [ ] Rename the main branch (`api/project_branches/rename`)
- [ ] Protect a specific branch from automatic deletion (`api/project_branches/set_automatic_deletion_protection`)
- [ ] Set a new main branch (`api/project_branches/set_main`)

### Project Dump
- [ ] Triggers project dump (`api/project_dump/export`)
- [ ] Triggers the import of a project dump (`api/project_dump/import`)
- [ ] Provide the import and export status of a project (`api/project_dump/status`)

### Project Links
- [ ] Create a new project link (`api/project_links/create`)
- [ ] Delete existing project link (`api/project_links/delete`)
- [ ] List links of a project (`api/project_links/search`)

### Project Pull Requests
- [ ] Delete a pull request (`api/project_pull_requests/delete`)
- [ ] List the pull requests of a project (`api/project_pull_requests/list`)

### Project Tags
- [ ] Search tags (`api/project_tags/search`)
- [ ] Set tags on a project (`api/project_tags/set`)

### Projects
- [ ] Delete one or several projects (`api/projects/bulk_delete`)
- [x] Create a project (`api/projects/create`)
- [x] Delete a project (`api/projects/delete`)
- [ ] Export all findings of a project branch (`api/projects/export_findings`)
- [ ] Get whether a project contains AI code (`api/projects/get_contains_ai_code`)
- [ ] Get detected AI code (`api/projects/get_detected_ai_code`)
- [ ] Get license usage of projects (`api/projects/license_usage`)
- [x] Search for projects (`api/projects/search`)
- [ ] Return list of projects with 'Administer' permission (`api/projects/search_my_projects`)
- [ ] List projects that a user can scan (`api/projects/search_my_scannable_projects`)
- [ ] Sets if the project contains AI code (`api/projects/set_contains_ai_code`)
- [ ] Update the default visibility for new projects (`api/projects/update_default_visibility`)
- [ ] Update a project key (`api/projects/update_key`)
- [ ] Updates visibility of a project (`api/projects/update_visibility`)

### Quality Gates
- [ ] Allow a group to edit a Quality Gate (`api/qualitygates/add_group`)
- [ ] Allow a user to edit a Quality Gate (`api/qualitygates/add_user`)
- [ ] Get the quality gate status of an application (`api/qualitygates/application_status`)
- [ ] Copy a Quality Gate (`api/qualitygates/copy`)
- [ ] Create a Quality Gate (`api/qualitygates/create`)
- [ ] Add a new condition to a quality gate (`api/qualitygates/create_condition`)
- [ ] Delete a condition from a quality gate (`api/qualitygates/delete_condition`)
- [ ] Remove the association of a project from a quality gate (`api/qualitygates/deselect`)
- [ ] Delete a Quality Gate (`api/qualitygates/destroy`)
- [ ] Get the quality gate of a project (`api/qualitygates/get_by_project`)
- [ ] Get a list of quality gates (`api/qualitygates/list`)
- [ ] Get the quality gate status of a project (`api/qualitygates/project_status`)
- [ ] Remove the ability from a group to edit a Quality Gate (`api/qualitygates/remove_group`)
- [ ] Remove the ability from a user to edit a Quality Gate (`api/qualitygates/remove_user`)
- [ ] Rename a Quality Gate (`api/qualitygates/rename`)
- [ ] Search for projects associated to a quality gate (`api/qualitygates/search`)
- [ ] List the groups that are allowed to edit a Quality Gate (`api/qualitygates/search_groups`)
- [ ] List the users that are allowed to edit a Quality Gate (`api/qualitygates/search_users`)
- [ ] Associate a project to a quality gate (`api/qualitygates/select`)
- [ ] Qualify or disqualify a custom Quality Gate as AI Code Assured (`api/qualitygates/set_ai_code_assurance`)
- [ ] Set a quality gate as the default (`api/qualitygates/set_as_default`)
- [ ] Display the details of a quality gate (`api/qualitygates/show`)
- [ ] Update a condition attached to a quality gate (`api/qualitygates/update_condition`)

### Quality Profiles
- [ ] Activate a rule on a Quality Profile (`api/qualityprofiles/activate_rule`)
- [ ] Bulk-activate rules on one quality profile (`api/qualityprofiles/activate_rules`)
- [ ] Allow a group to edit a Quality Profile (`api/qualityprofiles/add_group`)
- [ ] Associate a project with a quality profile (`api/qualityprofiles/add_project`)
- [ ] Allow a user to edit a Quality Profile (`api/qualityprofiles/add_user`)
- [ ] Backup a quality profile (`api/qualityprofiles/backup`)
- [ ] Change a quality profile's parent (`api/qualityprofiles/change_parent`)
- [ ] Get the history of changes on a quality profile (`api/qualityprofiles/changelog`)
- [ ] Compare two quality profiles (`api/qualityprofiles/compare`)
- [ ] Copy a quality profile (`api/qualityprofiles/copy`)
- [ ] Create a quality profile (`api/qualityprofiles/create`)
- [ ] Deactivate a rule on a quality profile (`api/qualityprofiles/deactivate_rule`)
- [ ] Bulk deactivate rules on Quality profiles (`api/qualityprofiles/deactivate_rules`)
- [ ] Delete a quality profile (`api/qualityprofiles/delete`)
- [ ] Show a quality profile's ancestors and children (`api/qualityprofiles/inheritance`)
- [ ] List projects associated with a quality profile (`api/qualityprofiles/projects`)
- [ ] Remove the ability from a group to edit a Quality Profile (`api/qualityprofiles/remove_group`)
- [ ] Remove a project's association with a quality profile (`api/qualityprofiles/remove_project`)
- [ ] Remove the ability from a user to edit a Quality Profile (`api/qualityprofiles/remove_user`)
- [ ] Rename a quality profile (`api/qualityprofiles/rename`)
- [ ] Restore a quality profile (`api/qualityprofiles/restore`)
- [ ] Search quality profiles (`api/qualityprofiles/search`)
- [ ] List groups allowed to edit a Quality Profile (`api/qualityprofiles/search_groups`)
- [ ] List users allowed to edit a Quality Profile (`api/qualityprofiles/search_users`)
- [ ] Select the default profile for a given language (`api/qualityprofiles/set_default`)
- [ ] Show a quality profile (`api/qualityprofiles/show`)

### Rules
- [ ] Get data for 'Coding Rules' page (`api/rules/app`)
- [ ] Create a custom rule (`api/rules/create`)
- [ ] Delete custom rule (`api/rules/delete`)
- [ ] List rules (`api/rules/list`)
- [ ] List available rule repositories (`api/rules/repositories`)
- [ ] Search for a collection of relevant rules (`api/rules/search`)
- [ ] Get detailed information about a rule (`api/rules/show`)
- [ ] List rule tags (`api/rules/tags`)
- [ ] Update an existing rule (`api/rules/update`)

### Users
- [ ] Search for users (`api/users/search`)
- [ ] Get user details (`api/users/show`) - Assuming this is what's meant
- [ ] Create a new user (`api/users/create`)
- [ ] Deactivate a user (`api/users/deactivate`)
- [ ] Update user properties (`api/users/update`)
- [ ] Change user password (`api/users/change_password`)
- [ ] Get user groups (`api/users/groups`)
- [ ] Get user tokens (`api/user_tokens/search`)
- [ ] Generate a user token (`api/user_tokens/generate`)
- [ ] Revoke a user token (`api/user_tokens/revoke`)

### System
- [ ] Get system health (`api/system/health`)
- [ ] Get system metrics (`api/system/metrics`) - Not in list, but assuming
- [ ] Get system status (`api/system/status`)
- [ ] Get system upgrades (`api/system/upgrades`)
- [ ] Get system logs (`api/system/logs`)
- [ ] Get system configuration (`api/system/info`)

## Development

### Project Structure
```
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── src
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_placeholder.py
```

### Formatting

To format the code, run black:

```bash
black src tests
```

### Testing

To run the tests, use pytest:

```bash
pytest
```

## API Documentation

The SonarQube REST API documentation can be found here: https://next.sonarqube.com/sonarqube/web_api/api/
