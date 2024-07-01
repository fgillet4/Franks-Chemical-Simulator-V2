# Frank's Chemical Simulator V2

This application is designed for chemical engineering and process design. It 
provides various tools and functionalities specific to the field of chemical 
engineering.

## Getting Started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes.

### Prerequisites

Before running the application, you will need to have Node.js and npm 
installed on your system. You can download them from [Node.js 
website](https://nodejs.org/).

### Installing

To get a development environment running, clone the repository and install 
the dependencies.

1. **Clone the repository**
   ```bash
   git clone https://github.com/fgillet4/Franks-Chemical-Simulator-V2.git
   cd Franks-Chemical-Simulator-V2
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```
3. **Run Application**
   ```bash
   npm start
   ```

4. **Running the Tests**
   Explain how to run the automated tests for this system (if applicable).

5. **Contributing**
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

6. **Authors**
Francis Gillet
See also the list of contributors who participated in this project.

7. **License**
This project is licensed under the ISC License - see the LICENSE.md file for details.

8. **Acknowledgments**
Send me a tip to any of my crypto wallets if you want me to keep developing certain features!!

BTC:bc1qsph06nm9qtwx4ydg7p0p0cv9yv3cstw7ghkvwz

ETH:0x17fede1a0c5cfbcce54e7f25ede69d0ba08a269c

POLYGON:0x17fede1a0c5cfbcce54e7f25ede69d0ba08a269c

BNBBEACON:bnb1lz7ev4kmkrgzfaqfy24xcm5dwvs53fv2wefary

TRON:TBNTaBKHSXZCbi18BGNfyKvYvojTzZJeQJ

BNB:0x17fede1a0c5cfbcce54e7f25ede69d0ba08a269c

AVAX:0x17fede1A0c5cFbCCe54E7F25Ede69D0ba08A269C

ARBITRUM:0x17fede1a0c5cfbcce54e7f25ede69d0ba08a269c

ARETH:0x82aF49447D8a07e3bd95BD0d56f35241523fBab1

DOGECOIN:DK8mD7gG6oh6bKnhn7QNgra8FbsVNEjzFr

CARDANO:addr1q8n8p6rq5a9nusf7vycpgxnc6e2hvg59glm6ehmrpxz379lca33un224ugrr9rytg2jyemahdaykqmm35ptjl7rj6leqhpw6as

SOLANA:4kmifrvanBVbeGRz8gi5o9bJ6e6y1ixtGPSagHxaa4jT


### Steps to stage changes made and update repo

1. **If you want to add all new or modified files at once, use:**
   ```bash 
   git add .
   ``` 
2. **If you prefer to add specific files, use:**
   ```bash
   git add path/to/your/file
   ```
3. **For example:**
   ```bash
   git add src/renderer/index.html
   ```
4. **For example:**
   ```bash
   git add src/renderer/styles.css
   ```
### Steps to commit changes made
5. **Once you've staged your changes, commit them with a descriptive message:**
   ```bash
   git commit -m "Change made"
   ```
6. **After committing your changes, push them to your GitHub repository:**
   ```bash
   git push origin main
   ```

7. **If it's the first time you're pushing or if you've recently re-initialized your Git repository, you might need to set the upstream for your local branch:**
   ```bash
   git push -u origin main
   ```

   
### Explaination of all files and folders

`assets/`: This directory contains all the static resources that the application uses.

`css/`: Stores Cascading Style Sheets for styling the application's user interface.

`js/`: Contains JavaScript files that might include libraries or utility scripts used by the application's front-end.

`images/`: Holds image files such as icons, background images, or any other images used in the application.

`fonts/`: Includes custom font files that can be used across the application for consistent typography.

`node_modules/`: Generated by npm, this directory contains all the Node.js modules that your project depends on.

`src/`: The source directory where the application's main codebase resides.

`main/`: Contains the entry point and main process files for the Electron application.

`index.js`: The main process file that initializes the application, creates windows, and manages application events.

`renderer/`: Holds the files that are rendered in the Electron window (the front end).

`index.html`: The main HTML file that serves as the entry point for the application's user interface.

`script.js`: The accompanying JavaScript file for the renderer process, handling UI logic and interactions.

`common/`: Shared utilities and functions that can be used both by the main and renderer processes.

`utils.js`: A utility file with common functions that are reusable throughout the application.

`simulation/`: Core logic for the simulation aspect of the application.

`flowsheetModel.js`: Defines the structure and behavior of the hydraulic model used in simulations.

`solver.js`: Implements the solver algorithms that process the simulation data.

`database/`: Interacts with a local or remote database, managing data storage and retrieval.

`dbHandler.js`: Manages database operations such as queries, updates, and transactions.

`data/`: Used for persisting data related to the application.

`flowsheets/`: Stores serialized representations of flowsheet simulations, likely in JSON format.

`results/`: Saves the outputs from the simulations, which may include calculation results and figures.

`tests/`: Contains all the test cases and testing scripts for the application, ensuring code quality and functionality.

`.gitignore`: A Git configuration file that specifies which files and directories should be ignored by version control.

`package.json`: The manifest file for the project that includes metadata like the project's name, version, dependencies, and scripts.

`package-lock.json`: Automatically generated by npm, it keeps track of the exact versions of npm packages installed.

`README.md`: A markdown file that provides an overview of the project, setup instructions, and other essential information.

`LICENSE.md`: Includes the license under which the software is distributed, detailing how it can be used, modified, and shared.

`CONTRIBUTING.md`: Guidelines for how other developers can contribute to the project, including coding standards, pull request processes, etc.

`scripts/`: Custom scripts that can be used for automating builds, deployments, or other development tasks.

`dist/`: The directory where the final, packaged Electron application is stored after the build process. This is what you distribute to users.




Install Git: Ensure you have Git installed on your local machine. You can download it from git-scm.com.

Create a Repository (Repo): Start by creating a new repo on GitHub. Provide a name, description, and initialize with a README if you like.

Clone the Repo:

To clone the repo to your local machine, use:
bash
Copy code
git clone https://github.com/your-username/your-repository-name.git
This will create a directory with the name of your repo and download all of its contents.
Create a Branch:

Before making changes, it’s good practice to create a new branch:
bash
Copy code
git checkout -b new-feature
This switches you to a new branch called new-feature.
Make Changes:

Make changes to files in your local project directory.
Stage Changes:

To stage your changes for commit, use:
bash
Copy code
git add .
This adds all the changed files to the staging area.
Commit Changes:

To commit these changes, use:
bash
Copy code
git commit -m "Add a relevant commit message"
Replace "Add a relevant commit message" with a message that describes the changes you made.
Push Changes to GitHub:

To push your branch and changes to GitHub, use:
bash
Copy code
git push origin new-feature
This will upload your changes to the new-feature branch on GitHub.
Create a Pull Request (PR):

On GitHub, you can now open a pull request from your new branch to the main branch.
This is a request to review your changes and merge them into the main codebase.
Review, Merge, and Pull:

Once your PR is reviewed and approved, you can merge it into the main branch.
After merging, pull the changes to your local main branch to keep it up to date:
bash
Copy code
git checkout main
git pull origin main
Tagging Releases:

For version control, you can tag significant points (like a release) in your commit history for future reference:
bash
Copy code
git tag v1.0.0
git push origin v1.0.0
Replace v1.0.0 with your version number.
Handling Merge Conflicts:

If there are conflicts between your branch and the main branch, you’ll need to resolve these before merging.
Git will mark the files with conflicts, and you’ll manually need to resolve these by editing the files and then committing the resolved version.
Repeat:

The process of making changes, committing, and pushing continues as you develop your project.
Here are some additional tips:

Commit Often: Make small, frequent commits with meaningful commit messages.
Branch: Use branches for new features or bug fixes.
Pull Requests: Use pull requests to merge branches, which allows for code review.

# Getting Set Up on Fedora Linux

To get your Electron project up and running on a new Linux machine, you'll need to follow these steps to install Node.js, npm, and the required packages for your project.

## Step-by-Step Guide

### 1. Install Node.js and npm

First, ensure that Node.js and npm are installed on your Fedora system. You can install them using the following commands:

´´´sh
sudo dnf install nodejs npm
´´´

### 2. Navigate to Your Project Directory

Change to the directory of your Electron project:

´´´sh
cd /path/to/your/project/Franks-Chemical-Simulator-V2
´´´

### 3. Install Project Dependencies

Install the dependencies listed in your `package.json` file, including Electron:

´´´sh
npm install
´´´

### 4. Install Electron Globally (Optional)

If you prefer to install Electron globally, you can use:

´´´sh
npm install -g electron
´´´

However, it's usually recommended to install Electron as a dev dependency within your project to ensure consistency across different environments.

### 5. Run Your Project

Now you can start your project using npm:

´´´sh
npm start
´´´

Fetch Often: Regularly git fetch to stay updated with what's happening in the remote repo.
Remember, the key to version control is regular commits and clear, descriptive messages that explain what each commit does. This practice helps you and others understand the project's history and makes collaboration easier.
