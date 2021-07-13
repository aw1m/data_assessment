## Problem

You are a data engineer for an E-Learning platform and have been tasked with converting raw data from the platform to a data warehouse using modern tools.
The platform delivers various assessments (questionnaires) to our learners and we must use those results to provide insights to our customers.
Data is provided from the application in JSON Format. Data about the learners comes in the `users.json` file.  A submitted questionnaire will be stored in the `questionnaire-attempt.json` file. The questions that appear on the questionnaire
are provided on the `questions.json` file. Finally information about the Questionnaire itself comes on the `questionnaire.json` file. 
Using a combination of Python and SQL, process the four files and create a usable data model that can be leveraged to create insights/visualizations.  The data model should follow data warehousing best practices.
After you have decided on a model, write 3-5 queries that could produce information of value to our partners.

Things to note:
- Each User, Questionnaire, Question, and Choice has it's own unique UUID
- Questionnaires are made up of questions
- Questions have choices
- Choices can be correct or incorrect

## Criteria
- Initialize the project using git
- Commit regularly
- Host on GitHub, GitLab, etc OR zip the entire repo and email

## Bonus Points
- Testing suite
- Add your own query to pull out something interesting