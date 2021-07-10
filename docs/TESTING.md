# Table of Contents

> - [User Stories](#user-stories)
> - [Responsive Tests](#responsive-tests)
> - [Code Validation](#code-validation)
> - [Manual Site Testing](#manual-site-testing)
> - [Deployment](#deployment)  

## User Stories

### Anonymous user

#### easily navigate the site

- Responsive Bootstrap menu bar with easily identifiable icons allow the user to intuitively find what they need
- Additional links in Footer allow further ease of navigation throughout the site

#### view the site on all screen sizes

- Bootstrap Grid has been used to layout the main responsive design
- Custom media queries in external CSS files ensures fine responsive details
- Focussed responsive design on popular mobile, table and laptop/desktop dimensions:
  - Mobiles: iphone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

#### read about the company details,goals and aims

- Incorporated a brief, yet descriptive 'About Us' section on the home page.

#### search for projects

- Keyword search is incorporated in the navigation, with an easily recognisable search spyglass icon.

#### filter my search results

- Naviation dropdown sections for Project and Country allows easy navigation for firstlevel search.
- A second-level search filter appears on both Project and Country pages with a familiar drop-down filter for Alphabetical filtering of Name, Type and Country.
- User is continually informed on how mnay results each level of search displays.

#### read details about projects

- On the Project or Country pages, each project has a short introductory description.
- On clicking the 'Read More' button on each project, this navigated the user to the project description page, where detailed information on the project is displayed.

#### read details of what percentage of donations FundPIN retains

- On the Donation section of each project page, the percentage of funds that FundPIN retains is clearly detailed.
- On the checkout page, the percentage amount that FundPIN retains from the user's total donation is clearly displayed to the user before payment is made.

#### access contact details

- Contact number displayed on Contact Page.
- Contact form on contact page allows user to get in touch.

#### access social media of the company

- Social media links are clearly displayed in the Footer, with each linking to the relevant social media page of the company in a new tab.

#### register for a user profile account by choosing a username and password

- If user is not logged in, simple registration is available from the Profile icon on the navigation menu.
- User has the option to enter email address, username and password to register and is sent a confirmation email to confirm registration.

#### register for a user profile account using social media login details

- User has the option to sign into a choice of social media accounts on the Log in page.

### Registered user

#### log in and log out of my profile account

- The Profile icon in the navigation menu displays whether a user is logged in or not, and allows the user to easily log in and out of their account accordingly.

#### update my details

- The user's Profile page (accessed by the Profile icon in the nvaigation menu) allows the user to edit and save phone number and address details.

#### store my address for later use

- Details for the phone number and address fields on the Profile page persist, regardless of user logging off or clearing browser cache.

#### store my donation history

- A donation history list is visible on the user's Profile page. These details persist regardless of user logging off or clearing browser cache.

#### enter a custom amount to donate to a particular project

- users (including anonymous users) can choose to enter their own amount on the donation form displayed on each project page.

#### select an amount from a drop-down list

- users (including anonymous users) can choose to pick a pre-determined 'quick' amount from a drop-down list on the donation form displayed on each project page.

#### review my donation choices at checkout

- before confirming and paying for the donation(s), user has the ability to review and delete any donations added to their cart.

#### store my choices in checkout

- Whilst navigating the site, users (including anonymous users) can add donations to differnet projects to their donation cart, which are all stored in the checkout whilst browsing the site. The stored data is only accessible during hte session and clears if the user logs out.

#### Make secure payments

- Payment security is handled by Stripe implementation for the payment process.

#### Receive email confirmation of my donation payment

- XXXXXXXXXX email not sent XXXXXXXXXXX

### Site admin/superuser

When the Admin/Superuser account is logged into:

#### add new projects and category listings

- A menu is accessible from the Profile icon in the navigation menu. Under Project Management, a new project can be added with fields for Category and Country.

#### update project listings

- On each project page, additonal button is visible to the Superuser to Update a project.

#### delete existing project listings

- On each project page, additonal button is visible to the Superuser to Delete a project. Before deletion, added notificaiton in form of a confirmation modal appears.

#### create blogs

- A menu is accessible from the Profile icon in the navigation menu. Under Blog Management, a new blog post can be created.

#### update blog entries

- On each blog post page, additonal button is visible to the Superuser to Update a blog post.

#### delete blog entries

- On each blog post page, additonal button is visible to the Superuser to Delete a blog post. Before deletion, added notificaiton in form of a confirmation modal appears.

## Responsive Tests

- DevTools - Devices tested across a range of widths:
  - Mobiles: iphone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

- Viewed on physical devices:
  - Mobiles: small phone (320px) | large phone (414px)
  - Tablets: large tablet (768px)
  - Desktops: Medium laptop (1366px) | Large Desktop screen (1920px)

- Viewed site on above range (including Responsive mode) on various browsers: >   - Google Chrome
  - Firefox
  - Opera
  - Safari

## Code Validation

### HTML

All HTML templates checked with [Nu Html Checker](https://validator.w3.org/nu/?#textarea) by direct input.

General:

- **Error**: No p element in scope but a p end tag seen. This stems from text addition by the user/superuser using the richtext editor's WYSIWYG formatting for project descriptions and blog entries. => **Resolved**: This can safely be ignored, as the result will always be dependant on the user/superuser's input and does not affect the visual outcome of the HTML for other users once the form is submitted.

- **Warning**: The type attribute is unnecessary for JavaScript resources. => **Resolved**: Removed all `type="text/javascript"` instances as this is default for HTML5 and unnecessary.

`base.html`

- **Error**: Bad value submit for attribute type on element `a`: Subtype missing. (search button) => **Resolved**: changed `a` element to a `button` element.

- **Error**: Element `li` not allowed as child of element div in this context. (nav icons) => **Resolved**: Add missing `ul` to wrap `li`.

`index.html`

- **Error**: End tag section seen, but there were open elements. (Featured projects section) => **Resolved**: Fix missing closing div

- **Warning**: Section lacks heading. Consider using h2-h6 elements (lead-in section) => **Resolved**: Ignored as no heading is neccessary.

- **Warning**: The type attribute is unnecessary for JavaScript resources. => **Resolved**: Ignored.

`contact.html`

- No errors

`project_description.html`

- **Error**: Attribute readonly not allowed on element input at this point. (donation form) => **Resolved**: Removed readonly attribute as `type` is already set to hidden.

- **Error**: Bad value button for attribute type on element a: Subtype missing. (delete confirm modal) => **Resolved**: Remove `type` attribute. Tested delte button on modal and confirmed working as expected.

`add_project.html`

- **Error**: Duplicate attribute id. => **Unresolved**: `id="id_image"` is generated in the same input as `id="new-image"`, presumably by the JavaScript. As this is working fine, I've decided to leave this for now due to time-constraints of the project and added to bugs/issues to resolve.

`edit_project.html`

- **Error**: Quote `"` in attribute name. Probable cause: Matching quote missing somewhere earlier. => **Resolved**: Minor fix on class attribute.

- **Error**: Duplicate attribute id. => **Unresolved**: `id="id_image"` is generated in the same input as `id="new-image"`, presumably by the JavaScript. As this is working fine, I've decided to leave this for now due to time-constraints of the project and added to bugs/issues to resolve.

- **Error**: Element p not allowed as child of element strong in this context. => **Resolved**: Corrected misplacement of `p` and `strong` elements in the `custom_clearable_file_input.html` file.

`blog_list.html`

- no errors

`blog_description.html`

- **Error**: End tag section seen, but there were open elements. (blog description section) => **Resolved**: Fix missing closing div.

- **Error**: Bad value button for attribute type on element a: Subtype missing. => **Resolved**: Remove `type="button"` attribute.

- **Error**: Duplicate attribute class. => **Resolved**: Removed duplicate code.

- **Error**: No p element in scope but a p end tag seen. => **Resolved**: Caused by user's input into Richtext editor field, safely ignored.

`add_blog.html`

- **Error**: Duplicate attribute id. => **Unresolved**: `id="id_image"` is generated in the same input as `id="new-image"`, presumably by the JavaScript. As this is working fine, I've decided to leave this for now due to time-constraints of the project and added to bugs/issues to resolve.

- **Error**: Element p not allowed as child of element strong in this context. => **Resolved**: Corrected misplacement of `p` and `strong` elements in the `custom_clearable_file_input.html` file.

`edit_blog.html`

- **Error**: Duplicate attribute id. => **Unresolved**: `id="id_image"` is generated in the same input as `id="new-image"`, presumably by the JavaScript. As this is working fine, I've decided to leave this for now due to time-constraints of the project and added to bugs/issues to resolve.

`cart.html`

- **Error**: Duplicate ID in remove_(itemid) => **Unresolved**: Unable to find cause, but presumed to be from the `update_remove_donation.html`template. Due to time-constraints, this has been added to bugs/issues to resolve

`checkout.html`

- **Error**: Attribute href not allowed on element button at this point. => **Resolved**: Removed unnecessary href.

`checkout_success.html`

- No errors

`profile.html`

- **Error**: Element ol not allowed as child of element small in this context. => **Resolved**: Moved `small` element inside `ol` element.

`login.html`, `logout.html` and `signup.html`

- No errors

### CSS

Parsed all css code through [Autoprefixer](https://autoprefixer.github.io/) and tested validation via [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator)

`base.css`, `home.css`, `contact.css`, `projects.css`, `profile.css`, `checkout.css`, `cart.css` and `blog.css`

- No errors found

### JAVASCRIPT

- All files and scripts passed through [Shint](https://jshint.com/) and all passed with a few exceptions:
  - `stripe_elements.js` returned undefined variables `Stripe`and `$`, which can be ignored as these are built into Stripe.
  - `home.js` returned warnings for undefined variables, but safely ignored due to required use by SwiperJS.
  - `donationform.js` - warnings ignored:
    - line 16 - Misleading line break before '?'; readers may interpret this as an expression boundary.
    - line 17 - Expected an assignment or function call and instead saw an expression.
  - `script.js` returns unused variables `openNav` and `closeNav`, but these are being called in `mobile_nav.html`template.
  - sort script in `projects.html` returns undefined variables `sort` and `direction`, but these are defined in the if statement.
  - script tags containing JQuery return undefined variable `$`, which can be ignored as this is standard JQuery format.
  - warnings for use of `const`, `let` and `arrow functions` only available in ES6 - Safely ignored.

### PYTHON

- Installed [flake8](https://flake8.pycqa.org/en/latest/) to check errors on all Python files.
- Passed all Python files through [pep8online](http://pep8online.com/) to check [PEP8](https://www.python.org/dev/peps/pep-0008/) compliance.
- All files passed, but the following ignored:
  - `settings.py` in fundpin app - lines too long on 183, 186, 189 and 192
  - `settings.py` in fundpin app - line 18 "'env' imported but unused"
  - `views.py` in checkout app - line too long on line 78
  - `webhooks.py` in checkout app - line too long on line 41
  - `webhooks.py` in checkout app - line 26 and 29 "local variable 'e' is assigned but never used"
  - `webhook_handler.py` in checkout app - line too long on line 131
  - `webhook_handler.py` in checkout app - line 55 "local variable 'total' is assigned but never used"
  - `webhook_handler.py` in checkout app - line 123 "undefined name 'Decimal'"
  - `views.py` in home app - line 43 f-string is missing placeholders - Researched online and definitive answer not found. Line seems correct and works as expected.

## Manual Site Testing

## Deployment


