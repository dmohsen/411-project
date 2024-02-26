# Recipe Finder App Requirements

## Project Description
The Recipe Finder App is designed to allow users to input ingredients they have at home to discover matching recipes. It leverages the Spoonacular and Edamam APIs for recipe searches and to provide nutritional information. The app features a recommendation system where users can save their favorite recipes and receive suggestions for similar ones. A SQLite database is implemented to store saved recipes and ingredient lists.

## Product Requirements

### Goal
Enhance culinary creativity and reduce food waste through an easy-to-use web interface.

### Non-Goal
Serve as a comprehensive nutrition planner or dietary management tool.

### Non-Functional Requirements

#### Security
- **Functional Requirements:**
  - Use OAuth authentication or 2FA.
  - Ensure data encryption and secure API communication through TLS.

#### Performance and Scalability
- **Functional Requirements:**
  - Optimize API calls to ensure quick search results.
  - Implement a scalable database solution that can efficiently handle growing numbers of users and their saved recipes.

## Product Management

### Theme
Impress the user by showing them recipes that are quick, easy, and use ingredients they already have.

### Epic: Website Beta

#### User Story 1
_As a repeat user, I want to be able to save recipes that I like._

- **Task:** Save recipes
  - **Ticket 1:** Design and create a database in SQLite that does not need to be fancy or special. We can also use just one table for this.
  - **Ticket 2:** Allow the user to “save” or “favorite” recipes they like and create a tab on the website where they can view this information.

#### User Story 2
_As a new user, I do not want to memorize a new password for another website._

- **Task:** Use 3rd party OAuth
  - **Ticket 1:** Use Google account authentication.
  - **Ticket 2:** Use data encryption and secure API communication through TLS.
