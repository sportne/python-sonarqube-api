# python-sonarqube-api

A Python wrapper for the Sonarqube Web API that allows you to easily interact with your SonarQube instance.

This library provides access to almost the full functionality of the SonarQube API, allowing you to automate tasks, extract data, and integrate SonarQube into your existing workflows.

## Features Checklist

This is a list of features that have been implemented in this SonarQube Python API client.

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
- [x] Add a comment to a Security Hotspot (`api/hotspots/add_comment`)
- [x] Assign a hotspot to an active user (`api/hotspots/assign`)
- [x] Change the status of a Security Hotspot (`api/hotspots/change_status`)
- [x] Delete comment from Security Hotspot (`api/hotspots/delete_comment`)
- [x] Edit a comment (`api/hotspots/edit_comment`)
- [x] List Security Hotpots (`api/hotspots/list`)
- [x] Fetch and return all hotspots for a given branch (`api/hotspots/pull`)
- [x] Search for Security Hotpots (`api/hotspots/search`)
- [x] Provides the details of a Security Hotspot (`api/hotspots/show`)

### Issues
- [x] Add a comment (`api/issues/add_comment`)
- [x] Receive a list of anticipated transitions (`api/issues/anticipated_transitions`)
- [x] Assign/Unassign an issue (`api/issues/assign`)
- [x] Search SCM accounts (`api/issues/authors`)
- [x] Bulk change on issues (`api/issues/bulk_change`)
- [x] Display changelog of an issue (`api/issues/changelog`)
- [x] List tags for the issues under a given component (`api/issues/component_tags`)
- [x] Delete a comment (`api/issues/delete_comment`)
- [x] Do workflow transition on an issue (`api/issues/do_transition`)
- [x] Edit a comment (`api/issues/edit_comment`)
- [x] Return a list of vulnerabilities in Gitlab SAST format (`api/issues/gitlab_sast_export`)
- [x] List issues in degraded mode (`api/issues/list`)
- [x] Fetch and return all issues for a given branch (`api/issues/pull`)
- [x] Fetch and return all taint vulnerabilities for a given branch (`api/issues/pull_taint`)
- [x] Reindex issues for a project (`api/issues/reindex`)
- [x] Search for issues (`api/issues/search`)
- [x] Change severity (`api/issues/set_severity`)
- [x] Set tags on an issue (`api/issues/set_tags`)
- [x] List tags matching a given query (`api/issues/tags`)

### Languages
- [x] List supported programming languages (`api/languages/list`)

### Measures
- [x] Return component with specified measures (`api/measures/component`)
- [x] Navigate through components with specified measures (`api/measures/component_tree`)
- [x] Search for project measures (`api/measures/search`)
- [x] Search measures history of a component (`api/measures/search_history`)

### Metrics
- [x] Search for metrics (`api/metrics/search`)
- [x] List all available metric types (`api/metrics/types`)

### Monitoring
- [x] Return monitoring metrics in Prometheus format (`api/monitoring/metrics`)

### New Code Periods
- [x] Lists the new code definition for all branches in a project (`api/new_code_periods/list`)
- [x] Updates the new code definition (`api/new_code_periods/set`)
- [x] Shows the new code definition (`api/new_code_periods/show`)
- [x] Unsets the new code definition (`api/new_code_periods/unset`)

### Notifications
- [x] Add a notification (`api/notifications/add`)
- [x] List notifications (`api/notifications/list`)
- [x] Remove a notification (`api/notifications/remove`)

### Permissions
- [x] Add a permission to a group (`api/permissions/add_group`)
- [x] Add a group to a permission template (`api/permissions/add_group_to_template`)
- [x] Add a project creator to a permission template (`api/permissions/add_project_creator_to_template`)
- [x] Add permission to a user (`api/permissions/add_user`)
- [x] Add a user to a permission template (`api/permissions/add_user_to_template`)
- [x] Apply a permission template to one project (`api/permissions/apply_template`)
- [x] Apply a permission template to several components (`api/permissions/bulk_apply_template`)
- [x] Create a permission template (`api/permissions/create_template`)
- [x] Delete a permission template (`api/permissions/delete_template`)
- [x] Lists the groups with their permissions (`api/permissions/groups`)
- [x] Remove a permission from a group (`api/permissions/remove_group`)
- [x] Remove a group from a permission template (`api/permissions/remove_group_from_template`)
- [x] Remove a project creator from a permission template (`api/permissions/remove_project_creator_from_template`)
- [x] Remove permission from a user (`api/permissions/remove_user`)
- [x] Remove a user from a permission template (`api/permissions/remove_user_from_template`)
- [x] List permission templates (`api/permissions/search_templates`)
- [x] Set a permission template as default (`api/permissions/set_default_template`)
- [x] Lists the groups with their permission on a template (`api/permissions/template_groups`)
- [x] Lists the users with their permission on a template (`api/permissions/template_users`)
- [x] Update a permission template (`api/permissions/update_template`)
- [x] Lists the users with their permissions (`api/permissions/users`)

### Plugins
- [x] Get the list of all the plugins available for installation (`api/plugins/available`)
- [x] Cancels any operation pending on any plugin (`api/plugins/cancel_all`)
- [x] Download plugin JAR (`api/plugins/download`)
- [x] Installs the latest version of a plugin (`api/plugins/install`)
- [x] Get the list of all the plugins installed (`api/plugins/installed`)
- [x] Get the list of plugins with pending operations (`api/plugins/pending`)
- [x] Uninstalls the plugin (`api/plugins/uninstall`)
- [x] Updates a plugin (`api/plugins/update`)
- [x] Lists plugins with available updates (`api/plugins/updates`)

### Project Analyses
- [x] Create a project analysis event (`api/project_analyses/create_event`)
- [x] Delete a project analysis (`api/project_analyses/delete`)
- [x] Delete a project analysis event (`api/project_analyses/delete_event`)
- [x] Search a project analyses and attached events (`api/project_analyses/search`)
- [x] Update a project analysis event (`api/project_analyses/update_event`)

### Project Badges
- [x] Generate a badge for project's AI assurance (`api/project_badges/ai_code_assurance`)
- [x] Generate badge for project's measure (`api/project_badges/measure`)
- [x] Generate badge for project's quality gate (`api/project_badges/quality_gate`)
- [x] Creates new token for project badge access (`api/project_badges/renew_token`)
- [x] Retrieve a token for project badge access (`api/project_badges/token`)

### Project Branches
- [x] Delete a non-main branch (`api/project_branches/delete`)
- [x] Gets whether a project is AI Code Assured (`api/project_branches/get_ai_code_assurance`)
- [x] List the branches of a project (`api/project_branches/list`)
- [x] Rename the main branch (`api/project_branches/rename`)
- [x] Protect a specific branch from automatic deletion (`api/project_branches/set_automatic_deletion_protection`)
- [x] Set a new main branch (`api/project_branches/set_main`)

### Project Dump
- [x] Triggers project dump (`api/project_dump/export`)
- [x] Triggers the import of a project dump (`api/project_dump/import`)
- [x] Provide the import and export status of a project (`api/project_dump/status`)

### Project Links
- [x] Create a new project link (`api/project_links/create`)
- [x] Delete existing project link (`api/project_links/delete`)
- [x] List links of a project (`api/project_links/search`)

### Project Pull Requests
- [x] Delete a pull request (`api/project_pull_requests/delete`)
- [x] List the pull requests of a project (`api/project_pull_requests/list`)

### Project Tags
- [x] Search tags (`api/project_tags/search`)
- [x] Set tags on a project (`api/project_tags/set`)

### Projects
- [x] Delete one or several projects (`api/projects/bulk_delete`)
- [x] Create a project (`api/projects/create`)
- [x] Delete a project (`api/projects/delete`)
- [x] Export all findings of a project branch (`api/projects/export_findings`)
- [x] Get whether a project contains AI code (`api/projects/get_contains_ai_code`)
- [x] Get detected AI code (`api/projects/get_detected_ai_code`)
- [x] Get license usage of projects (`api/projects/license_usage`)
- [x] Search for projects (`api/projects/search`)
- [x] Return list of projects with 'Administer' permission (`api/projects/search_my_projects`)
- [x] List projects that a user can scan (`api/projects/search_my_scannable_projects`)
- [x] Sets if the project contains AI code (`api/projects/set_contains_ai_code`)
- [x] Update the default visibility for new projects (`api/projects/update_default_visibility`)
- [x] Update a project key (`api/projects/update_key`)
- [x] Updates visibility of a project (`api/projects/update_visibility`)

### Quality Gates
- [x] Allow a group to edit a Quality Gate (`api/qualitygates/add_group`)
- [x] Allow a user to edit a Quality Gate (`api/qualitygates/add_user`)
- [x] Get the quality gate status of an application (`api/qualitygates/application_status`)
- [x] Copy a Quality Gate (`api/qualitygates/copy`)
- [x] Create a Quality Gate (`api/qualitygates/create`)
- [x] Add a new condition to a quality gate (`api/qualitygates/create_condition`)
- [x] Delete a condition from a quality gate (`api/qualitygates/delete_condition`)
- [x] Remove the association of a project from a quality gate (`api/qualitygates/deselect`)
- [x] Delete a Quality Gate (`api/qualitygates/destroy`)
- [x] Get the quality gate of a project (`api/qualitygates/get_by_project`)
- [x] Get a list of quality gates (`api/qualitygates/list`)
- [x] Get the quality gate status of a project (`api/qualitygates/project_status`)
- [x] Remove the ability from a group to edit a Quality Gate (`api/qualitygates/remove_group`)
- [x] Remove the ability from a user to edit a Quality Gate (`api/qualitygates/remove_user`)
- [x] Rename a Quality Gate (`api/qualitygates/rename`)
- [x] Search for projects associated to a quality gate (`api/qualitygates/search`)
- [x] List the groups that are allowed to edit a Quality Gate (`api/qualitygates/search_groups`)
- [x] List the users that are allowed to edit a Quality Gate (`api/qualitygates/search_users`)
- [x] Associate a project to a quality gate (`api/qualitygates/select`)
- [x] Qualify or disqualify a custom Quality Gate as AI Code Assured (`api/qualitygates/set_ai_code_assurance`)
- [x] Set a quality gate as the default (`api/qualitygates/set_as_default`)
- [x] Display the details of a quality gate (`api/qualitygates/show`)
- [x] Update a condition attached to a quality gate (`api/qualitygates/update_condition`)

### Quality Profiles
- [x] Activate a rule on a Quality Profile (`api/qualityprofiles/activate_rule`)
- [x] Bulk-activate rules on one quality profile (`api/qualityprofiles/activate_rules`)
- [x] Allow a group to edit a Quality Profile (`api/qualityprofiles/add_group`)
- [x] Associate a project with a quality profile (`api/qualityprofiles/add_project`)
- [x] Allow a user to edit a Quality Profile (`api/qualityprofiles/add_user`)
- [x] Backup a quality profile (`api/qualityprofiles/backup`)
- [x] Change a quality profile's parent (`api/qualityprofiles/change_parent`)
- [x] Get the history of changes on a quality profile (`api/qualityprofiles/changelog`)
- [x] Compare two quality profiles (`api/qualityprofiles/compare`)
- [x] Copy a quality profile (`api/qualityprofiles/copy`)
- [x] Create a quality profile (`api/qualityprofiles/create`)
- [x] Deactivate a rule on a quality profile (`api/qualityprofiles/deactivate_rule`)
- [x] Bulk deactivate rules on Quality profiles (`api/qualityprofiles/deactivate_rules`)
- [x] Delete a quality profile (`api/qualityprofiles/delete`)
- [x] Show a quality profile's ancestors and children (`api/qualityprofiles/inheritance`)
- [x] List projects associated with a quality profile (`api/qualityprofiles/projects`)
- [x] Remove the ability from a group to edit a Quality Profile (`api/qualityprofiles/remove_group`)
- [x] Remove a project's association with a quality profile (`api/qualityprofiles/remove_project`)
- [x] Remove the ability from a user to edit a Quality Profile (`api/qualityprofiles/remove_user`)
- [x] Rename a quality profile (`api/qualityprofiles/rename`)
- [x] Restore a quality profile (`api/qualityprofiles/restore`)
- [x] Search quality profiles (`api/qualityprofiles/search`)
- [x] List groups allowed to edit a Quality Profile (`api/qualityprofiles/search_groups`)
- [x] List users allowed to edit a Quality Profile (`api/qualityprofiles/search_users`)
- [x] Select the default profile for a given language (`api/qualityprofiles/set_default`)
- [x] Show a quality profile (`api/qualityprofiles/show`)

### Rules
- [x] Get data for 'Coding Rules' page (`api/rules/app`)
- [x] Create a custom rule (`api/rules/create`)
- [x] Delete custom rule (`api/rules/delete`)
- [x] List rules (`api/rules/list`)
- [x] List available rule repositories (`api/rules/repositories`)
- [x] Search for a collection of relevant rules (`api/rules/search`)
- [x] Get detailed information about a rule (`api/rules/show`)
- [x] List rule tags (`api/rules/tags`)
- [x] Update an existing rule (`api/rules/update`)

### Sources
- [ ] Get source code as line number / text pairs (`api/sources/index`)
- [ ] Get code snippets involved in an issue or hotspot (`api/sources/issue_snippets`)
- [ ] Show source code with line oriented info (`api/sources/lines`)
- [ ] Get source code as raw text (`api/sources/raw`)
- [ ] Get SCM information of source files (`api/sources/scm`)
- [ ] Get source code (`api/sources/show`)

### System
- [x] Get system health (`api/system/health`)
- [x] Get system metrics (`api/system/metrics`)
- [x] Get system status (`api/system/status`)
- [x] Get system upgrades (`api/system/upgrades`)
- [x] Get system logs (`api/system/logs`)
- [x] Get system configuration (`api/system/info`)
- [ ] Temporarily changes level of logs (`api/system/change_log_level`)
- [ ] Provide liveness of SonarQube (`api/system/liveness`)
- [ ] Migrate the database (`api/system/migrate_db`)
- [ ] Answers "pong" as plain-text (`api/system/ping`)
- [ ] Restarts server (`api/system/restart`)

### User Tokens
- [x] Generate a user access token (`api/user_tokens/generate`)
- [x] Revoke a user access token (`api/user_tokens/revoke`)
- [x] List the access tokens of a user (`api/user_tokens/search`)

### Users
- [x] Change user password (`api/users/change_password`)
- [ ] Get the details of the current authenticated user (`api/users/current`)
- [ ] Dismiss a notice for the current user (`api/users/dismiss_notice`)
- [ ] List the external identity providers (`api/users/identity_providers`)
- [ ] Set AI tool usage (`api/users/set_ai_tool_usage`)
- [ ] Set homepage of current user (`api/users/set_homepage`)

### Views
- [ ] Add an existing application to a portfolio (`api/views/add_application`)
- [ ] Add a branch of an application selected in a portfolio (`api/views/add_application_branch`)
- [ ] Add an existing portfolio to the structure of another portfolio (`api/views/add_portfolio`)
- [ ] Add a project to a portfolio (`api/views/add_project`)
- [ ] Add a branch of a project selected in a portfolio (`api/views/add_project_branch`)
- [ ] List applications which the user has access to that can be added to a portfolio (`api/views/applications`)
- [ ] Create a new portfolio (`api/views/create`)
- [ ] Delete a portfolio definition (`api/views/delete`)
- [ ] List root portfolios (`api/views/list`)
- [ ] Move a portfolio (`api/views/move`)
- [ ] List possible portfolio destinations (`api/views/move_options`)
- [ ] List portfolios that can be referenced (`api/views/portfolios`)
- [ ] List projects manually selected in a portfolio (`api/views/projects`)
- [ ] Return projects with a failed quality gate (`api/views/projects_status`)
- [ ] Refresh one or all of the portfolios (`api/views/refresh`)
- [ ] Remove an application from a portfolio (`api/views/remove_application`)
- [ ] Remove a branch of an application selected in a portfolio (`api/views/remove_application_branch`)
- [ ] Remove a reference to a portfolio (`api/views/remove_portfolio`)
- [ ] Remove a project from a portfolio (`api/views/remove_project`)
- [ ] Remove a branch of a project selected in a portfolio (`api/views/remove_project_branch`)
- [ ] Search for portfolios (`api/views/search`)
- [ ] Set the projects selection mode of a portfolio on manual selection (`api/views/set_manual_mode`)
- [ ] Set the projects selection mode of a portfolio to none (`api/views/set_none_mode`)
- [ ] Set the projects selection mode of a portfolio on regular expression (`api/views/set_regexp_mode`)
- [ ] Set the projects selection mode of a portfolio on unassociated projects in hierarchy (`api/views/set_remaining_projects_mode`)
- [ ] Set the projects selection mode of a portfolio on project tags (`api/views/set_tags_mode`)
- [ ] Show the details of a portfolio (`api/views/show`)
- [ ] Update a portfolio (`api/views/update`)

### Webhooks
- [ ] Create a Webhook (`api/webhooks/create`)
- [ ] Delete a Webhook (`api/webhooks/delete`)
- [ ] Get the recent deliveries (`api/webhooks/deliveries`)
- [ ] Get a webhook delivery by its id (`api/webhooks/delivery`)
- [ ] Search for webhooks (`api/webhooks/list`)
- [ ] Update a Webhook (`api/webhooks/update`)

### Web Services
- [ ] List web services (`api/webservices/list`)
- [ ] Display web service response example (`api/webservices/response_example`)

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
│   ├── __init__.py
│   └── sonarqube
│       ├── __init__.py
│       ├── client.py
│       └── ...
├── tests
│   ├── __init__.py
│   ├── test_applications.py
│   └── ...
└── documentation
    ├── index.md
    └── ...
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

## Future Work

- Implement the missing API endpoints.
- Add more examples and use cases to the documentation.
