![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Simple - Blog / Mockup plaatje / Live Link

Table of contents

- [UX](#ux)

  - [Agile User Stories/Epics/Milestones](#agile-user-stories)
  - [Site Goals](#site-goals)
  - [Wireframes](#wireframes)
  - [Images](#images)
  - [Logo](#logo)
  - [Favicon](favicon)
  - [Colour Scheme](colour-scheme)
  - [Fonts](fonts)
  - [Databases](databases)
  - [Features](Features)
  - [Bugs](bugs)
  - [Testing](testing)
  - [Deployment](deployment)
  - [Credits](credits)

# UX

## Agile User Stories/Epics/Milestone

## Site Goals

Lorem ipsum dolor sit amet. Sed galisum praesentium est quia voluptatum ut quaerat voluptatem qui quod eligendi et obcaecati illum. Qui enim quia qui laboriosam incidunt aut natus doloremque ut eveniet nihil! Et consequatur quam aut tenetur adipisci ea illum voluptatum hic deserunt consequuntur est obcaecati dolorum aut optio cupiditate et alias nobis.

A dolore praesentium ea officia sequi est quos soluta ea magni veniam? Aut doloribus commodi qui tempore officia et totam temporibus quo quod error sed beatae eligendi et nihil rerum.

## User Stories

As a user I want:

- Lorem ipsum dolor sit amet. Sit quibusdam voluptates vel iusto dolorem qui aliquid Quis a incidunt explicabo ab neque dolorum sed libero.
- Vel laudantium praesentium aut provident laudantium et ducimus dolor ea magni similique.
- To be able to set a Cipher-Key, this is a handy feature to add a extra level of complexity to obscure your passwords.
- To set up a default user login, makes the UX more user friendly.
- To always be able to change the 'master password' to access the password-manager.
- **note** There was a **copy/paste** password clipboard feature available but that I need to removed because it was not possible to integrate that
  in Heroku cloud environment.

As the administrator I want:

-  Est odio quia At repellat velit ut corporis quae ut consequatur fugiat non magnam libero id odit iste est voluptatibus libero.
- Quis a incidunt explicabo ab neque dolorum sed libero

## Deployment

### Heroku Deployment
This site was deployed to and is currently [hosted on the Heroku platform](https://mysimpleblog-1c6e9d449421.herokuapp.com/). The steps for deploying to Heroku, using PostgreSQL as the database host, are as follows:

#### Create a new PostgreSQL Code Institute database.

From codeinstitute every student can maintain up to eight databases to run there projects. Here is a step by step guide to install PostgreSQL from Code Institurte to the clould!

  1. Navigate to [PostgreSQL from Code Institute](https://dbs.ci-dbs.net//) and log in with your LMS account
  ![PostgreSQL database creation step1](static/images/readme-images/001.png)

  2. After you filled in your LMS account the PostgresSQL database manager will automaticly generate a new database for you.
  ![PostgreSQL database creation step2](static/images/readme-images/002.png)

  3. You now have a brand new PostgreSQL Code Institute database
  The link to this database and how to manage all your other databases will be send my email. 
  ![PostgreSQL database creation step3](static/images/readme-images/003.png)
  4. Do note these databases are limted in time and have a life time of operation of 18 months after the date of creation.
  ![PostgreSQL database creation step3](static/images/readme-images/004.png)
 
#### Django Project Settings
  7. In the project workspace, navigate to/create a file named 'Procfile' (remember the capital 'P')
  8. Add the following code replacing ```<myapp>``` with the actual app name then save the file:
      ``` python
      web: gunicorn <myapp>.wsgi
      ```
  9. Now navigate to/create a file named 'env.py'
  10. Add the following code, replacing ```<myurl>``` with the URL just copied from ElephantSQL and ```<mykey>``` with a string of your choice then save the file:
      ``` python
      import os

      os.environ["DATABASE_URL"]=<myurl>
      os.environ["SECRET_KEY"]=<mykey>
      ```
  11. Open 'settings.py' and add the following near the top of the code:
      ```python
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
        import env
      ```
  12. Further down the page, replace any current instance of the SECRET_KEY variable with:
      ``` python
      SECRET_KEY = os.environ.get('SECRET_KEY')
      ```
  13. Replace the DATABASES variable with
      ```python
      DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
      ```
  14. Save the file then run ```python manage.py migrate``` in the terminal
  15. Commit and push these changes to the repository

#### Heroku Setup
  16. Navigate to [Heroku](https://heroku.com) and create an account/log in
  17. Click 'New' in the top right and select 'Create New App'
  18. Enter an App name (must be unique), choose a region, and then click 'Create app'
  19. Select 'Settings' in the menubar
  20. Click 'Reveal Config Vars' and add the following:<br>
    - DATABASE_URL: the DATABASE_URL copied from ElephantSQL<br>
    - SECRET_KEY: The SECRET_KEY string you created<br>
    - PORT: 8000
  21. Click 'Deploy' in the menubar tab then 'GitHub' under 'Deployment method'
  22. Select the repository you want to deploy and click 'Connect'
  23. Scroll down and click 'Deploy Branch' to complete the process

### Forking the Repository
1. Login to/create your [GitHub](https://github.com) account
2. Navigate to the EastSt. GitHub Repository: https://github.com/ndsurgenor/east-street
3. Towards the top right, under the main banner, click 'Fork'
4. Adjust the form fields if desired, then click 'Create fork' to finish

### Cloning the Repository/Running Locally
1. Login to/create your [GitHub](https://github.com) account
2. Navigate to the EastSt. GitHub Repository: https://github.com/ndsurgenor/east-street
3. Click the '<> Code' dropdown button and ensure 'HTTPS' is selected
4. Click the copy icon (two overlapped squares) beside the repository URL
5. Open your local IDE and create a new project, ensuring git is installed
6. Run ```git clone copied-git-url``` in the terminal to finish


## Credits

### w3 schools

> Used to reference Python Structure

### Stack Overflow

> Used to reference different syntax issues from existing older boards. Also used to query clear function issues when I ran into them as referenced in the bug section.

## Acknowledgements

### Daisy McGirr

- My Mentor with Code Institute who has provided me with excellent feedback and guidance through this project.