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
  - Mobiles: iPhone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

#### read about the company details, goals and aims

- Incorporated a brief, yet descriptive 'About Us' section on the home page.

#### search for projects

- Keyword search is incorporated in the navigation, with an easily recognisable search spyglass icon.

#### filter my search results

- Navigation dropdown sections for Project and Country allows easy navigation for first-level search.
- A second-level search filter appears on both Project and Country pages with a familiar drop-down filter for Alphabetical filtering of Name, Type and Country.
- User is continually informed on how many results each level of search displays.

#### read details about projects

- On the Project or Country pages, each project has a short introductory description.
- On clicking the 'Read More' button on each project, this navigated the user to the project description page, where detailed information on the project is displayed.

#### read details of what percentage of donations FundPIN retains

- On the Donation section of each project page, the percentage of funds that FundPIN retains is clearly detailed.
- On the checkout page, the percentage amount that FundPIN retains from the user's total donation is clearly displayed to the user before payment is made.

#### access contact details

- Contact number displayed on Contact page.
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

- The user's Profile page (accessed by the Profile icon in the navigation menu) allows the user to edit and save phone number and address details.

#### store my address for later use

- Details for the phone number and address fields on the Profile page persist, regardless of user logging off or clearing browser cache.

#### store my donation history

- A donation history list is visible on the user's Profile page. These details persist regardless of user logging off or clearing browser cache.

#### enter a custom amount to donate to a particular project

- users (including anonymous users) can choose to enter their own amount on the donation form displayed on each project page.

#### select an amount from a drop-down list

- users (including anonymous users) can choose to pick a pre-determined 'quick' amount from a drop-down list on the donation form displayed on each project page.

#### review my donation choices at checkout

- Before confirming and paying for the donation(s), user has the ability to review and delete any donations added to their cart.

#### store my choices in checkout

- Whilst navigating the site, users (including anonymous users) can add donations to different projects to their donation cart, which are all stored in the checkout whilst browsing the site. The stored data is only accessible during hte session and clears if the user logs out.

#### Make secure payments

- Payment security is handled by Stripe implementation for the payment process.

#### Receive email confirmation of my donation payment

- Emails are not being sent, and this has been added as a Known Issue to the README document.

### Site admin/superuser

When the Admin/Superuser account is logged into:

#### add new projects and category listings

- A menu is accessible from the Profile icon in the navigation menu. Under Project Management, a new project can be added with fields for Category and Country.

#### update project listings

- On each project page, additional button is visible to the Superuser to Update a project.

#### delete existing project listings

- On each project page, additional button is visible to the Superuser to Delete a project. Before deletion, added notification in form of a confirmation modal appears.

#### create blogs

- A menu is accessible from the Profile icon in the navigation menu. Under Blog Management, a new blog post can be created.

#### update blog entries

- On each blog post page, additional button is visible to the Superuser to Update a blog post.

#### delete blog entries

- On each blog post page, additional button is visible to the Superuser to Delete a blog post. Before deletion, added notification in form of a confirmation modal appears.

## Responsive Tests

- DevTools - Devices tested across a range of widths:

  - Mobiles: iPhone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

- Viewed on physical devices:

  - Mobiles: small phone (320px) | large phone (414px)
  - Tablets: large tablet (768px)
  - Desktops: Medium laptop (1366px) | Large Desktop screen (1920px)

- Viewed site on above range (including Responsive mode) on various browsers: > - Google Chrome
  - Firefox
  - Opera
  - Safari

## Code Validation

### HTML

All HTML templates checked with [Nu Html Checker](https://validator.w3.org/nu/?#textarea) by direct input.

General:

- **Error**: No p element in scope but a p end tag seen. This stems from text addition by the user/superuser using the Richtext editor's WYSIWYG formatting for project descriptions and blog entries. => **Resolved**: This can safely be ignored, as the result will always be dependant on the user/superuser's input and does not affect the visual outcome of the HTML for other users once the form is submitted.

- **Warning**: The type attribute is unnecessary for JavaScript resources. => **Resolved**: Removed all `type="text/javascript"` instances as this is default for HTML5 and unnecessary.

`base.html`

- **Error**: Bad value submit for attribute type on element `a`: Subtype missing. (search button) => **Resolved**: changed `a` element to a `button` element.

- **Error**: Element `li` not allowed as child of element div in this context. (nav icons) => **Resolved**: Add missing `ul` to wrap `li`.

`index.html`

- **Error**: End tag section seen, but there were open elements. (Featured projects section) => **Resolved**: Fix missing closing div

- **Warning**: Section lacks heading. Consider using h2-h6 elements (lead-in section) => **Resolved**: Ignored as no heading is necessary.

- **Warning**: The type attribute is unnecessary for JavaScript resources. => **Resolved**: Ignored.

`contact.html`

- No errors

`project_description.html`

- **Error**: Attribute readonly not allowed on element input at this point. (donation form) => **Resolved**: Removed readonly attribute as `type` is already set to hidden.

- **Error**: Bad value button for attribute type on element a: Subtype missing. (delete confirm modal) => **Resolved**: Remove `type` attribute. Tested delete button on modal and confirmed working as expected.

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

- **Error**: Duplicate ID in remove\_(itemid) => **Unresolved**: Unable to find cause, but presumed to be from the `update_remove_donation.html`template. Due to time-constraints, this has been added to bugs/issues to resolve

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

- All files and scripts passed through [JShint](https://jshint.com/) and all passed with a few exceptions:
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

### Navigation

- Clicked on all links in Navigation menu main headings and confirmed user is directed to the desired page.
- Clicked on all Project and Country links in dropdown menus and confirmed user is directed to the filtered result on each.
- Clicked on Logo, and Home link in the menu, from all pages and reached expected result of user being returned to the home page.
- Clicked on all links in Footer 'Quick Links' list and confirmed user is directed to the desired page.
- Clicked on each Social Media icon in the Footer and each opens relevant external page in a new browser tab.
- Confirmed that Subscribe link works correctly, redirecting the user to MailChimp after entering email address and submitting the form.
- Confirmed that the 'back to top' button returns user to the top of the page once clicked (on all pages).

### Search Bar

- Clicked on the Search icon in the navigation menu and Search bar opens correctly.
- Clicked 'Cancel' button and search bar closes as expected.
- Entered keyword and pressed green search icon. The cards of projects with that keyword are filtered and displayed.
- Bug found whereby keyword entered is also displayed if part if another word - i.e. If entering 'lion', then 'billion' is also picked up - mentioned on README under Known Issues.

### Register page

- Clicked on Profile icon in the navigation menu and selected Register option, which redirects to the Registration/Sign Up page.
- Link to Login page working correctly when clicking 'sign in here' link, redirecting to the Login/Sign In page.
- Clicked 'Sign Up' button with no details and correct error message is returned for required inputs.
- Filled in form correctly and clicked 'Sign Up' button. Received email with confirmation link.
- Once clicked, I was redirected to the 'Confirm Email' page.
- Clicked on 'Confirm' button and redirected to the Log In/Sign In page with Django success message informing confirmation of email address.

### Login page

- Clicked on Profile icon in the navigation menu and selected Login option, which redirects to the Login page.
- Clicked 'Log in with GitHub' button and user is prompted to log in with GitHub credentials. Tested with own account and working as expected.
- Clicked 'Log in with Google' button and user is prompted to log in with Google credentials. Tested with own account and working as expected.
- Clicked 'Sign Up' link and correctly redirected to Register/Sign Up page.
- Clicked 'Sign In' button with no details and correct error message is returned for required inputs.
- Entered correct, registered username and password, and clicked 'Sign In' button. Django success message returned, informing the user is logged in, and returned to the Home page.

### Logout page

- Clicked on Profile icon in the navigation menu and selected Logout option, which redirects to the Logout/Sign Out page.
- Clicked the 'Cancel' button and returned to the Home page, and not logged out.
- Clicked the 'Sign Out' button and returned to the Home page, with Django success message that user is logged/signed out of the profile account.

### Home page

- Clicked on 'Donate' button in all slideshow images and each takes user to the specified filtered category page.
- Clicked on Category icons under the slideshow and each takes user to the specified filtered category page.
- Clicked on each 'Supporter' icon in the 'We Support' section and each opens relevant external page in a new browser tab.
- Hovered over project cards in 'Featured Project' section information and 'Read more' button appears as expected.
- Clicked on 'Read more' buttons and each takes the user to the desired project description page.
- Clicked on 'Read more' buttons in 'Featured Blog' section and each takes the user to the desired blog description page.
- Clicked on 'Contact Us' button in 'Keep in Touch' section and each takes the user to the Contact page.
- Checked all slideshow operations (auto scroll and option to drag left/right) and all working as expected.

### All Projects page

- Checked all 'Sort by' filters options in the filter menu and all return the correct filtering result.
- Hovered over project cards and lead-in information and 'Read more' button appears as expected.
- Clicked on 'Read more' buttons and each takes the user to the desired project description page.

### Project Description page

- Clicked on the image, which opens the image preview in new browser tab.
- Clicked on the 'Country' tag, which opens the filtered Project page for the relevant country.
- Clicked on the 'Category' tag, which opens the filtered Project page for the relevant category.
- Clicked on 'Fund this Project' button, which scrolls user down to donation form section.
- Clicked and drag/zoom inside map section and working as expected. Pin displays project name and on correct coordinates.
- Clicked on Social Media share buttons, and all open up relevant sharing (external link) options in a new browser tab. (_The Facebook button does not open relevant page, but rather shares the main site url - mentioned in README under 'Known Issues'_).
- Donation form:
  - Clicked on 'Choose an amount' and confirmed user can select a pre-determined amount from the dropdown which appears.
  - Clicked on 'Enter own amount' and confirmed user can enter an own amount and the 'Choose an amount' input is overridden.
  - Clicked on 'Enter own amount' input's increment and decrement options:
    - Each work as desired with an increase/decrease step in multiples of 10.
    - On decreasing the value, the minimum is Zero (0) and no negative values can be selected.
  - Clicked again on 'Choose an amount' and the 'Enter own amount' input is overridden.
  - Clicked on 'Back to projects' button and this returns the user to the 'All projects' page.
  - Entered an amount and clicked the Submit button:
    - User is directed to the top of the current page.
    - Cart icon in the navigation menu displays correct number of items in the cart.
    - Django success message displayed, informing the user of cart addition, information of the project donated to and a 'Secure Checkout' button.
    - Django success message also displays information on previously added project donations that are already in the cart.
  - Clicked 'Secure Checkout' button in success message popup, which directs to the cart page and shows current cart items.
  - Clicked cart icon in the Navigation menu, which directs to the cart page and shows current cart items.
- Once logged in as a Superuser, the 'Update' and 'Delete' buttons are visible.
  - Update button redirects to Update project page as expected and shows desired Django info message.
  - Delete button opens confirmation modal once clicked.
    - Cancel button (or clicking outside the modal) works as expected, closing the modal and cancelling the operation.
    - Delete button deletes project from database and returns Django success message.

### Add Project page

- Clicked on the Profile icon in the navigation menu and confirmed that the 'Add Project' option is only visible when logged in as a SuperUser.
- Clicked 'Add Project' from the dropdown and redirected to the Add Project page.
- Tested form by clicking the 'Add Project' button with no form entries, resulting in page refresh, correct error message for required fields and form is not submitted.
- Tested functionality of 'Select an Image' button, which opens up the file upload from local machine option.
- Filled in form correctly with all fields and clicked 'Add Project' button. Redirected to the new project page with success message.
- Filled in the form again and checked the 'is featured' checkbox, and the project is added to the 'Featured Projects' slideshow on the Home page.
- Filled in the form using an existing 'PIN ID' and error message is returned informing the user that the ID already exists, and the form is not submitted.
- Confirmed that all details entered, including image, is displayed in the new project added.

### Edit Project page

- The Edit Project page is a duplicate template of the Add Blog page. Tested all mentioned above for the Add Project page with same results.
- Clicked on the 'Update' button with all fields correctly filled in, page refreshes with updated entries and success message is returned.
- Tested the 'Remove' checkbox on the image field, which correctly updates the Project and removes the image.

### Cart page

- Clicked on 'Remove donation' button and Django success message displayed:
  - Informing the user of cart item deletion.
  - Current cart info is updated in this message.
  - Cart icon number display updates correctly.
- Removed all items in cart and default image with message to user, informing nothing is in the car, is displayed.
- Re-added multiple donations to the cart:
  - Donation amounts of each donation display correctly.
  - Total of all donations displays correctly.
  - Donation summary number displays correct amount of items in the cart.
- Clicked 'Secure Payment' button, which redirects to the Checkout page.

### Checkout page

- Tested form validity, by clicking the 'Complete Payment' button and correct errors returned if all required fields are not correctly filled in.
- Clicked 'Adjust cart' button, which redirects back to the cart and retains items in the cart.
- Correctly filled in form (with test credit card details) and clicked 'Complete Payment' button:
  - Loading screen loads as expected.
  - Donation confirmation (checkout success) page is displayed with correct information about the purchase.
  - Django success message displays success message, order number and that an email has been sent.
  - Email is not received by the user - Added to README under Known Issues.
- Tested 'save billing information to my profile' checkbox by changing information, selecting the box (confirming checked) and confirmed that this changes the amended information on the Profile page.

### Donation Confirmation page

- Info correctly displayed about the transaction made.
- Clicked 'Back to projects' button and redirects correctly to 'all projects' page

### Profile page

- Tested billing info form inputs and country dropdown and all working as expected.
- Changed info and clicked on 'Update' button and changes are correctly saved to the database and displayed to the user.
- Clicked on 'View donation confirmation' links (in the list of saved previous donations)
  - Correctly directs to the Donation Confirmation page for each item.
  - Displays Django info message with order details.

### Blog page

- Tested pagination functionality by adding more test blogs. Page numbers and arrows (left and right) work correctly and as expected.
- Clicked on 'Read more' button for each blog, which returns the correct Blog Description page for each.
- Once logged in as a Superuser, the 'Add Blog' button is visible. Clicking this redirects to the Add blog page.

### Blog Description page

- Clicked on Social Media share buttons, and all open up relevant sharing (external link) options in a new browser tab. (_The Facebook button does not open relevant page, but rather shares the main site url - mentioned in README under 'Known Issues'_).
- Clicked 'Post a Comment' button with no text in the text field, and correct error message displays for the required field.
- Entered a comment/text in the text field and clicked 'Post a Comment' button.
  - page refreshes, and the number of comments increments as expected, as well as the username, comment and date appearing correctly.
  - Django success message is displayed, including a list of orders currently on the cart.
- Once logged in as a Superuser, the 'Update' and 'Delete' buttons are visible.
  - Update button redirects to Update Blog page as expected and shows desired Django info message.
  - Delete button opens confirmation modal once clicked.
    - Cancel button (or clicking outside the modal) works as expected, closing the modal and cancelling the operation.
    - Delete button deletes blog from database and returns Django success message.

### Add Blog page

- Clicked on the Profile icon in the navigation menu and confirmed that the 'Add Blog Post' option is only visible when logged in as a SuperUser.
- Clicked 'Add Blog' from the dropdown and redirected to the Add Blog page.
- Tested form by clicking the 'Add Blog' button with no form entries, resulting in page refresh, correct error message for required fields and form is not submitted.
- Tested functionality of 'Select an Image' button, which opens up the file upload from local machine option.
- Filled in form correctly with all fields (selecting 'Published' from the 'Status' dropdown) and clicked 'Add Blog' button. Redirected to the new blog page with success message.
- Filled in the form and selected 'Draft' from the 'Status' dropdown. Once submitted, the new Blog post is not visible until set to 'Published' from the Admin page.
- Filled in the form and checked the 'is featured' checkbox, and the blog is added to the 'Featured Blogs' slideshow on the Home page.
- Confirmed that all details entered, including image, is displayed in the new blog post added.

### Edit Blog page

- The Edit Blog page is a duplicate template of the Add Blog page. Tested all mentioned above for the Add Blog page with same results.
- Clicked on the 'Update' button with all fields correctly filled in, page refreshes with updated entries and success message is returned.
- Tested the 'Remove' checkbox on the image field, which correctly updates the Blog Post and removes the image.

### Contact page

- Tested form by clicking the 'Send' button with no form entries, resulting in page refresh, correct error message for required fields and form is not submitted.
- Filled in form correctly with all fields and pressed 'Send' button. Redirected to Home page with success message that email has been sent.
- Confirmed that email functionality is working and email is received by user.

### Error pages

- Entered incorrect url suffix and redirected to the '404 Error' page as expected.
- Clicked on the 'Take me Back' button which successfully takes me back to the 'Home' page.
- 500 Error page is assumed to be correct. as styled the same as the 404 page, including the same link back to the home page.

## Deployment

- All tests above carried out on the [deployed url](https://fundpin.herokuapp.com/) to confirm the site is working as expected.
- Debug set to False in `settings.py` for final production push.
