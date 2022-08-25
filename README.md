# Survuval-analysis


Cancer treatment and survivorship in India- why it is so low
Cancer- A term for diseases in which abnormal cells divide without control and can
invade nearby tissues. Cancer cells can also spread to other parts of the body through the
blood and lymph systems.
Stages of cancer- Medical researchers created five specific stages of cancer to describe the
progression of the disease. Stage 4 is the most advanced and most serious cancer diagnosis
with the highest risk of mortality. However, many factors affect a person’s life expectancy.

In cancer studies, typical research questions are like:
● What is the impact of certain clinical characteristics on patient’s survival
● What is the probability that an individual survives 3 years?
● Are there differences in survival between groups of patients?
Objectives
The aim is to describe the basic concepts of survival analysis. In cancer studies, most of
survival analyses use the following methods:
● Kaplan-Meier plots to visualize survival curves
● Cox proportional hazards regression to describe the effect of variables on survival
Basic concepts
Here, we start by defining fundamental terms of survival analysis including:
● Survival time and event(death)
● Censoring
● Survival function and hazard function
Survival and hazard functions
The survival probability, also known as the survivor function S(t), is the probability that an
individual survives from the time of origin (e.g. diagnosis of cancer) to a specified future
time t.
The hazard, denoted by h(t), is the probability that an individual who is under observation at a
time t has an event at that time.
Kaplan-Meier survival estimate
The estimated probability (S(t)) is a step function that changes value only at the time of each
event. It’s also possible to compute confidence intervals for the survival probability.
The KM survival curve, a plot of the KM survival probability against time, provides a useful
summary of the data that can be used to estimate measures such as median survival time.
Toy Data :
Person time(months) event(death)
1st 2 1
2nd 3 0
3rd 6 1
4th 6 1
5th 7 1
The data is read as:
● The first person was observed for 2 months and that person died just after 2 months.
● The second person was observed for 3 months and did not die just after 3 months, but we do
not have any more date to confirm or deny that person’s death.
The Kaplan Meier analysis on the toy data :
Time(months) risk died haz 1- haz S(t)
0 5 0 0/5 5/5 100%
2 5 1 1/5 4/5 4/5= 80%
6 3 2 2/3 1/3 4/5*1/3= 26%
The above table is read as :
After 2 months
● At month 2 how many people are alive and at risk of dying = 5 people
● HAZ :How many people are at risk of dying at an instant(2), given you are alive leading up to
that instant(2) = 1/5
● S(t) : probability of surviving beyond 2months = 80%
After 6 months
● At month62 how many people are alive and at risk of dying = 3 people (because we don't
know if the second person is alive or not)
● HAZ :How many people are at risk of dying at an instant(6), given you are alive leading up to
that instant(6) = 2/3
● S(t) : probability of surviving beyond 6 months = 26%
Analysis: The data used is of lung cancer patients.
Sample of the data analysed.
https://www.key2stats.com/data-set/view/535
Time in days
Status - 1 : censored , 2 : dead
Age in years
Sex - Male : 1 , Female : 2
ph.ecog , pat.karno, meal.cal, wt.loss : Other factors on which survival depends
KM Survival curve :
Probability that a person lives upto 400 days ~ 0.4
Survival of different groups of people(Male/Female)
Conclusion : According to the data , more women are likely to survive upto an instance of
time than men.
Cox Proportional Hazard Model :
The idea behind Cox’s proportional hazard model is that the log-hazard of an individual is a
linear function of their covariates and a population-level baseline hazard that changes over
time. Mathematically:
The only time component is in the baseline hazard, b0(t). In the above equation, the partial
hazard is a time-invariant scalar factor that only increases or decreases the baseline hazard.
Thus changes in covariates will only inflate or deflate the baseline hazard.
● Here, bi represents the increase in log hazard ratio for one unit increase in xi(all other
covariates held constant).
● if bi < 0 , means increasing xi associated with lower risk(hazard) and longer survival
time.
● if bi > 0 , means increasing xi associated with increased risk(hazard) and shorter
survival time.
Fitting Cox Proportional Hazard Model:
● This graph depicts coefficients vs the log(hazard)
● Cox model estimates the time independent variables. So we can estimate the hazard
ratio.
● The above graph depicts survival probabilities of patients in different age groups.
Summary of Cox P-H Model.
covariate coef exp(coef)
age 0.01 1.01
sex -0.58 0.56
ph.karno 0.01 1.01
pat.karno -0.01 0.99
meal.cal 0 1
wt.loss -0.01 0.99
ecog_1 0.56 1.74
ecog_2 1.08 2.94
● Wt.loss has a coefficient of about -0.01.
● We can recall that in the Cox proportional hazard model, a higher hazard means more
at risk of the event occurring. The value 𝑒𝑥𝑝(− 0. 01) is called the hazard ratio.
● Here, a one unit increase in wt loss means the baseline hazard will increase by a factor
of 𝑒𝑥𝑝(− 0. 01) = 0.99 -> about a 1% decrease.
● Similarly, the values in the ecog column are: [0 = asymptomatic, 1 = symptomatic but
completely ambulatory, 2 = in bed 50\% of the day]. The value of the coefficient
associated with ecog2,𝑒𝑥𝑝(1. 20) , is the value of the ratio of hazards associated with
being "in bed 50% of the day (coded as 2)" compared to asymptomatic (coded as 0,
base category).
Cox model estimates the time independent variables. So we can estimate the hazard ratio.
Code document :
● Language used : Python
● Libraries used : numpy, pandas - for data manipulation , from lifelines library the
KaplanMeierFitter and CoxPHFitter classes were used, and matplotlib to plot graphs.
● First we format the data into a form that is standard to the in-build classes in the lifelines
● Input the time and event data into the KaplanMeierFitter to get the survival analysis using the
Kaplan Meier method.
● We can then use matplotlib to plot the survival curve.
● We can also plot survival curves for different groups using the KaplanMeierFitter
● For implementing the CPH model we again modify data so that each of the survival
determining factors only have two outcomes. (by creating dummy columns)
● We then input the time and status variables into the CoxPHFitter and plot the required graphs.
● The CoxPHFitter outputs a summary containing the hazards for each of the factors and their
corresponding hazard ratios, and we can analyze which factor affects the survival time of the
group of patients the most.
References-
● CANCER PREVENTION AND CONTROL IN INDIA
● Is Any Stage IV Cancer Curable? Survival Rates & Treatment Options
● Cancer survival rate: A tool to understand your prognosis - Mayo Clinic
● Is stage 4 cancer curable? Survival rates and outlook
● https://utswmed.org/medblog/team-s-doubling-cancer-survival-rates/
● How Long Can You Live with Stage 4 Cancer without Treatment? | Lung Cancer
Lawsuit Lawyers | Pintas & Mullins Law Firm
● https://www.mayoclinic.org/tests-procedures/cancer-treatment/about/pac-20393344
● Survival regression — lifelines 0.27.0 documentation
● https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_survival/BS704_Survival_p
rint.html
