# Project Title (python-group-quiz-app)
- Image and short bio of project
- OR Demo GIF and bio

## Description

Provide a short description explaining the what, why, and how of your project. Use the following questions as a guide:

- What was your motivation?
- Why did you build this project?
- What problem does it solve?
- What did you learn?

## Table of Contents (Optional)

If your README is long, add a table of contents to make it easy for users to find what they need.

- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [Technologies](#technologies)
- [Features & Implementation](#features--implementation)
- [Upcoming Features](#upcoming-features)
- [Feedback](#feedback)
- [Tests](#tests)
- [License](#license)


## Installation
1. Install python & pipenv
  - pip installation might be required as well

2. To enter the virtual environment
    ```shell
    pipenv shell
    ```

3. To install the required dependencies:
    ```shell
    pipenv install -r requirements.txt
    ```

```TODO: Add commands for upgrading the database & seeding```

4. To start the server:
    ```shell
    flask run
    ```

In case of Pylance import errors on VSCode, try:
1. Run:
    - Open the command palette
    - Go to Python Clear Cache and Reload
2. Run:
    - pipenv --venv
    - Open the command palette
    - Go to Python Select Interpreter
    - Then manually enter the interpreter path as the Python interpreter
    - This is in the command palette on VSCode

The above is also true for if Pycharm notifies you that there is no python interpreter configured! To solve via the Pycharm GUI:

1. Get the location of your pipenv virtual environment by running 'pipenv --venv'
2. Click configure python interpreter
3. Click add New interpreter
4. Click add local interpreter
5. Click the 'Existing' radio buton, then the ... icon.
6. Paste the location of the pipenv virtual environment
7. Look for the bin folder to your corresponding virtual environment
8. Select the file which corresponds to your version of python (for this case, python3.9) and hit OK

## Usage

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

## Acknowledgements

List your collaborators, if any, with links to their GitHub profiles.
Collaborators:
1.
2.
3.
4.
5.

If you used any third-party assets that require attribution, list the creators with links to their primary web presence in this section.
Credits:

	Design:
		Website (url)

	Icons:
		Website (url)

	Other:
		Animations - Website (url)
		Menu - Website (url)

If you followed tutorials, include links to those here as well.

## Technologies
Select from below
- JavaScript
- ReactJS
- Redux
- ExpressJS
- NodeJS
- Python
- Flask
- SQL
- PostgreSQL
- Sequelize
- SQLAlchemy
- HTML
- CSS
- Mocha
- Chai
- Pytest
- Docker

## Features & Implementation

If your project has a lot of features, list them here.
1. Feature 1
2. Feature 2
3. Implementation 1
4. Implementation 2
5. Ditto
6. Ditto

## Upcoming Features
- Planning to add

## Feedback
Feel free to send me feedback by filing an issue. Feature requests are always welcome.

If you wish to contribute or if there's anything you would like to chat about, reach out at [TBD]

## Tests

Go the extra mile and write tests for your application. Then provide examples on how to run them here.

## License

The last section of a high-quality README file is the license. This lets other developers know what they can and cannot do with your project. If you need help choosing a license, refer to [choosealicense.com](https://choosealicense.com/).
