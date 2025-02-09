# Testing

## Manual Testing

- Manual testing was carried out on the local and deployed sites.

|        Location       |           Feature          |                                                                                                           Expected Outcome                                                                                                          | Pass/Fail |                                                                    Notes                                                                   |
|:---------------------:|:--------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------:|:------------------------------------------------------------------------------------------------------------------------------------------:|
| Header                | Home button                | Takes user to home page on click                                                                                                                                                                                                    | PASS      |                                                                                                                                            |
| Header                | Log-in button              | Takes user to log-in page on click                                                                                                                                                                                                  | PASS      | If user is not logged in, the register and log-in buttons will be displayed but if they are logged in, only the log-out button will appear |
| Header                | Register button            | Takes user to registration page on click                                                                                                                                                                                            | PASS      |                                                                                                                                            |
| Header                | Logout button              | Logs out user on click, displays "successfully logged out" message                                                                                                                                                                  | PASS      |                                                                                                                                            |
| Header                | about button               | Takes user to about page on click                                                                                                                                                                                                   | PASS      |                                                                                                                                            |
| Header                | shared button              | Takes user to shared maniestations page on click                                                                                                                                                                                    | PASS      |                                                                                                                                            |
| Header                | profile button             | Takes user to profile page on click                                                                                                                                                                                                 | PASS      |                                                                                                                                            |
| Log-in page           | Log-in function            | When user enters an unknown username, the user will not be logged in                                                                                                                                                                | PASS      |                                                                                                                                            |
| Log-in page           | Log-in function            | When user enters an unknown password, the user will not be logged in                                                                                                                                                                | PASS      |                                                                                                                                            |
| Log-in page           | Log-in function            | When user enters a known username AND password, the user will be logged in                                                                                                                                                          | PASS      |                                                                                                                                            |
| Register page         | Register function          | If user does not enter information into any of the fields, they will be prompted to fill in the field                                                                                                                               | PASS      |                                                                                                                                            |
| Register page         | Register function          | If user does not enter a password which fits the criteria, will not be registered                                                                                                                                                   | PASS      |                                                                                                                                            |
| Register page         | Register function          | If user does not enter a matching password into the password (again) box, they will not be registered                                                                                                                               | PASS      |                                                                                                                                            |
| Register page         | Register function          | If user enters appropriate details, they will be registered                                                                                                                                                                         | PASS      |                                                                                                                                            |
| Logout page           | Sign out button            | Signs user out on click                                                                                                                                                                                                             | PASS      |                                                                                                                                            |
| Home page             | New manifestation button   | Takes user to form to create new manifestation                                                                                                                                                                                      | PASS      |                                                                                                                                            |
| Home page             | Manifestation link         | If user has a previously created a manifestations, the manifestation wil be listed on the home page with a link to view the manifestation in full                                                                                   | PASS      |                                                                                                                                            |
| Home page             | Manifestation Status       | Icons to indicate manifestation is_charged status, is_public, and is_approved are shown for each manifestation                                                                                                                      | PASS      |                                                                                                                                            |
| Create manifestation  | Create new manifestation   | If user fills out forms correctly, a new manifestation will be created with a unique slug url                                                                                                                                       | PASS      |                                                                                                                                            |
| View manifestation    | Charge manifestation       | If user is the owner of the manifestation, they can click to charge their manifestation for 24 hours                                                                                                                                | PASS      |                                                                                                                                            |
| View manifestation    | Edit manifestation         | Takes user to edit_manifestation on click                                                                                                                                                                                           | PASS      |                                                                                                                                            |
| View manifestation    | Delete manifestation       | Takes user to delete_manifestation view on click                                                                                                                                                                                    | PASS      |                                                                                                                                            |
| View manifestation    | Back to home button        | Takes user to Home page on click                                                                                                                                                                                                    | PASS      |                                                                                                                                            |
| View manifestation    | can_charge status          | If user is the owner of the manifestation and 12 hours has passed since the manifestation was charged, the user can click "charge" button to charge the manifestation for a futher 24 hours                                         | PASS      |                                                                                                                                            |
| View manifestation    | can_charge status          | If user is the owner of the manifestation and 12 hours have not passed since the manifestation was last charged, the "charge" button is not visible and a time is displayed to show when the charge function will next be available | PASS      |                                                                                                                                            |
| Shared Manifestations | Public manifestations list | If a manfestation has been set to is_public and has been approved by an administrator, the manifestation will be listed and visible to all users.                                                                                   | PASS      |                                                                                                                                            |
| Profile               | Logout button              | Logs out user on click, displays "successfully logged out" message                                                                                                                                                                  | PASS      |                                                                                                                                            |
| Profile               | Change Password Button     | Takes user to change_password view on click                                                                                                                                                                                         | PASS      |                                                                                                                                            |
| Profile               | Delete Account Button      | Takes user to delete_account view on click                                                                                                                                                                                          | PASS      |                                                                                                                                            |
| Delete_manifestation  | "Yes, delete" button       | Deletes chosen manifestation on click, displays "manifestation successfully deleted" message                                                                                                                                        | PASS      |                                                                                                                                            |
| Delete_manifestation  | "Cancel" button            | Returns user to manifestation view on click                                                                                                                                                                                         | PASS      |                                                                                                                                            |
| Edit_manifestation    | Edit manifestation         | If user fills out forms correctly, the manifestation will be updated with the user's changes. Message, 'Your manifestation has been updated successfully. If it is set to public, it will be reviewed by an admin.' is shown.       | PASS      |                                                                                                                                            |
| Edit_manifestation    | "Cancel" button            | Returns user to manifestation view on click                                                                                                                                                                                         | PASS      |                                                                                                                                            |
| Edit_manifestation    | is_approved update         | If a user edits a previously public and approved manifestation, it will be resubmitted for admin approval before it can be viewed by users other than the manifestation owner.                                                      | PASS      |                                                                                                                                            |
| Change_password       | Change password form       | Is user correctly fills out change password form, the user's password is changed and redirects user to success.html                                                                                                                 | PASS      |                                                                                                                                            |
| Delete_account        | Delete user account        | On click, deletes user account, returns user to homepage and displays message, 'Your account has been deleted successfully.'                                                                                                        | PASS      |                                                                                                                                            |
| Delete_account        | "Cancel" button            | Returns user to profile view on click.                                                                                                                                                                                              | PASS      |                                                                                                                                            |

- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing:**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]


## Code validators
### HTML
- The [W3C Validator](https://validator.w3.org/) was used to validate the HTML.
#### Home
- ![Home page validator screenshot]()

#### Logout page
- ![Logout page validator screenshot]()

#### Login page
- ![Login page validator screenshot]()

#### Register page
- ![Register page validator screenshot]()

- ![Register page validator screenshot code]()


### CSS custom code
- The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
- ![CSS validator screenshot]()

### Python
- The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python files.
- admin.py
- ![PEP8 screenshot](static/manifest/images/admin.pyPEP8.png)
- account/apps.py
- ![PEP8 screenshot](static/manifest/images/apps.pyPEP8.png)
- manifest/apps.py
- ![PEP8 screenshot](static/manifest/images/manifest-apps.pyPEP8.png)
- account/forms.py
- ![PEP8 screenshot](static/manifest/images/accout-forms.pyPEP8.png)
- manifest/forms.py
- ![PEP8 screenshot]()
- models.py
- ![PEP8 screenshot]()
- settings.py
- ![PEP8 screenshot]()
- pixelwitch/urls.py
- ![PEP8 screenshot]()
- manifest/urls.py
- ![PEP8 screenshot]()
- account/urls.py
- ![PEP8 screenshot]()
- views.py
- ![PEP8 screenshot]()
- wsgi.py
- ![PEP8 screenshot]()

### Lighthouse
#### Home
- ![Lighthouse screenshot for home page]()

#### Register
- ![Lighthouse screenshot for register page]()

#### Login
- ![Lighthouse screenshot for login page]()

#### Logout
- ![Lighthouse screenshot for logout page]()




#### Future improvements based on Lighthouse
- 



## Responsiveness
#### Mobile
- ![mobile responsiveness screenshot- home]()
- ![mobile responsiveness screenshot- register]()
- ![mobile responsiveness screenshot- view_manifestation]()

#### Tablet
- ![tablet responsiveness screenshot- home]()
- ![tablet responsiveness screenshot- register]()
- ![tablet responsiveness screenshot- view_manifestation]()

#### Desktop
- ![laptop responsiveness screenshot- home]()
- ![laptop responsiveness screenshot- register]()
- ![laptop responsiveness screenshot- view_manifestation]()

## Browsers
- I use Google Chrome as my browser so all screenshots above are from Google Chrome.
- The site was tested on Microsoft Edge:
- ![Microsoft Edge screenshot]()
- The site was tested on Opera:
- ![Opera screrenshot]()

## Bugs
- Add bugs here
