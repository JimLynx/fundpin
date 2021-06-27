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

## Manual Site Testing

## Deployment
