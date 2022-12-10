
# Team palm: Employee Satisfaction Project 

The purpose of the project is to provide tools for the analyzis of the 2021 Federal Employee Viewpoint Survey filtering by demographics, agencies and different survey questions. Moreover, we want to predict whether employees are planning to leave their organization and identify key questions when people are making this decision.

This project is part of the Fall 2022 data science bootcamp directed by [The Erdős Institute](https://www.erdosinstitute.org/).

## Data

The dataset is the public release data file of the 2021 Federal Employee Viewpoint Survey that can be accessed [here](https://www.opm.gov/fevs/public-data-file). The survey is administered by the U.S. Office of Personnel Management (OPM) to measure federal employees' opinions about their work environment in aspects such as the relationship with supervisors, goal achievements within agencies, support during COVID-19 pandemic, etc.

The dataset includes about 180 000 respondents with answers to all the questions. The survey includes 
information about:

1. 31 federal agencies such as the departments of Homeland Security, Agriculture, Labor, and the National Science Foundation.

2. 50+ likert-type questions with 5-point scales such as « Strongly Disagree to Strongly Agree » and « Very dissatisfied to Very Satisfied ». Example survey questions are:

    - Q7  - I know how my work relates to the agency's goals.
    - Q22 - My agency is successful at accomplishing its mission.
    - Q43 - Considering everything, how satisfied are you with your pay?
    - Q48 - My organization’s senior leaders demonstrate commitment to employee health and safety.

3. Employees' demographic information has 9 variables that include:

    - Individuals with disability.
    - Age group (under 40 or over 40).
    - Supervisory status.
    - Whether they plan to leave the organization within the next year.

## Methodology

For the analysis of likert-type survey questions and as way to justify the use of averages and correlations based on numeric answers, we show that the Pearson and Kendall correlation matrices show no significant difference -- as it is the case with polychoric correlations.

Since our data is completely categorical, we used box-plots (considering numeric 1 to 5 answers, negative to positive), stacked bar-plots and heatmaps to visualize the distribution of the answers, filtering by different subgroups across demographics, agencies and questions in pairwise agency comparison, respectively. With the help of the `ipywidgets` python module, the interested reader can quickly create these plots by choosing the preferred subgroup from a dropdown menu, as can be seen here:

![alt text](https://github.com/PSha98/Employee-Satisfaction-project/blob/main/stacked_barplot.gif)

We also used the nonparametric [Mann-Whitney U](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test) procedure to identify, given any two chosen agencies, whether there is enough statistical evidence to claim the median answers to each of the survey questions is different for these populations.

Finally, we trained and run a random forest model on the survey data to predict, given an employee's answers to the survey (questions + demographic - intent to leave), whether the individual is planning to leave the organization within the next year.
For better guidance on training the model, we first check if it's possible to extract important factors from the features using [Bartlett’s test of sphericity](https://en.wikipedia.org/wiki/Bartlett%27s_test) and [Kaiser-Meyer-Olkin Test](https://en.wikipedia.org/wiki/Kaiser%E2%80%93Meyer%E2%80%93Olkin_test). And use the number of factors to help train the model.


## Results 

Training with Random Forest with some paramters obtained from the previous section, we get the following prediction on the test data:

![alt text](https://github.com/PSha98/Employee-Satisfaction-project/blob/main/prediction.png)

We are able to get a accuracy of around 76% and a f1 score of roughly 0.75 compared with a f1 score 0.48 when predicting everyone leaves. 

Also, checking the importance of the questions from our trained model, we noticed the following questions plays important roles, in other words, these questions are the main factors when an employee decides to leave:

1. Q42 - Considering everything, how satisfied are you with your job?
2. Q44 - Considering everything, how satisfied are you with your organization?
3. Q23 - I recommend my organization as a good place to work.
4. Q6  - My talents are used well in the workplace.
5. Q3  - My work gives me a feeling of personal accomplishment.

