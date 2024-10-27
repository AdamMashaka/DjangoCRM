## Adding Django CRM users

After completing the previous steps of this instruction, you can begin adding users. But in order for sales managers to be able to use all the features of [Django CRM](https://github.com/DjangoCRM/django-crm/), they must follow the remaining points of this instruction.  
Please review the following sections before adding users.

### Permissions for users

There are four permissions for users in relation to objects (e.g., Tasks, Deals, etc.):  

- add (create)
- view
- change
- delete

Permissions can be assigned to individual users or groups of users.  
In relation to a particular object instance, CRM can dynamically change the permissions set for the object type. For example, a user who has permission to modify emails will not be able to modify an email if it is an incoming email.

### User groups (roles)

Groups are a convenient way to assign users a specific set of permissions or attributes. A user can belong to any number of groups. For example, the head of the sales department needs to be added to the "managers", "department heads" groups and the group of the department in which he works (for example, "Global sales").  
The "department heads" and "Global sales" groups give their members the appropriate attribute but do not provide any permissions.  
The "managers" (sales managers) group provides its members with sets of permissions in relation to such objects as: Request, Deal, Lead, Company, Contact person, etc.  
A group that gives its members certain rights is called a role.

The following roles are available:

- chiefs (company executives)
- managers (sales managers)
- operators (employees who receive commercial requests coming to the company. For example, a secretary or receptionist)
- superoperators (the same as operator but with the rights to serve several sales departments)
- accountants
- co-workers (this group is added to all users by default to work with TASKS)
- task_operators (allows you to edit Memos (Office notes) and Tasks objects owned by other users)

You can view the permission sets for each role here:  
 `(ADMIN site) Home > Authentication and Authorization > Groups`

A user can have multiple roles.  
For example, if your company does not have an employee who could perform the role of operator, then this role should be given to an employee with the role of sales manager.  
Attention! It is possible that some combinations of roles can lead to incorrect CRM operation. In this case, you can create several accounts for the user in CRM with different roles.

### Departments

The Department object contains the name and properties of a specific department.
You need to create a department on the page:  
`(ADMIN site) Home > Common > Departments`

When creating a department, a group with the same name is automatically created.  
**Please note** that creating a group for use as a department without creating a Department object will result in CRM not working correctly.
The following departments are preinstalled in CRM:  

- Global sales,
- Local sales,
- Bookkeeping.

You can rename them or add new ones.

### Adding users

`(ADMIN site) Home > Authentication and Authorization > Users`

To allow user access to the CRM website, check the following check-boxes:  
Active and Staff status.

If there is no suitable role for a user, then the set of permissions for him can be set individually.
All users must be added to their department group. The only exceptions are company managers (users with the "chiefs" roles).
For superusers (CRM administrators), assigning a department is optional.

A User profile is automatically created for each user. You can specify additional data in the User profile.  
 `(ADMIN site) Home > Common > User profiles`

This profile will be available to all CRM users at:  
 `(CRM site) Home > Common > User profiles`

## User access to applications and objects

CRM may contain commercial information or confidential information. Therefore, a user's access to applications and objects is determined by his role (set of rights).  
The rights can be permanent or dynamic.  
For example, if a company has two sales departments, sales managers can always see only objects (Requests, Deals, Reports, etc.) related to their department.

Dynamic rights can depend on many factors. For example, the value of filters. Even company managers or CRM administrators who can see all objects will not be able to see an object belonging to a department different from the current one selected in the department filter. To see this object, you need to select the corresponding department in the filter or select the "all" value.

## Helping users to master Django CRM

Before starting to work in Django CRM, users should be informed about the following:  

- It is important to familiarize yourself with the user guide to learn the CRM more easily.
- Many CRM pages have a button to go to the help page - (?). It is located in the upper right corner. Help pages should be read.
- Many page elements such as buttons, icons, links have tooltips. To do this, you need to hover the mouse cursor over them.  
It is also important for the administrator to help users to master the CRM.

**Pay attention!** Help pages are dynamic. Their content depends on the user's role. Users who are assigned rights individually (without a role assignment) will not be able to access the help page. Such users should be instructed to work in CRM by the administrator.