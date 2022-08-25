import numpy as np
import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter
import matplotlib.pyplot as plt

data = pd.read_excel(r'C:\Users\nisha\Desktop\lung.xlsx', index_col = 0)
data.head()
data.shape

data = data[['time', 'status', 'age', 'sex', 'ph.ecog', 'ph.karno','pat.karno', 'meal.cal', 'wt.loss']]
data["status"] = data["status"] - 1
data["sex"] = data["sex"] - 1
data.head()

data.dtypes

data.isnull().sum()

data.columns

data["ph.karno"].fillna(data["ph.karno"].mean(), inplace = True)
data["pat.karno"].fillna(data["pat.karno"].mean(), inplace = True)
data["meal.cal"].fillna(data["meal.cal"].mean(), inplace = True)
data["wt.loss"].fillna(data["wt.loss"].mean(), inplace = True)
data.dropna(inplace=True)
data["ph.ecog"] = data["ph.ecog"].astype("int64")

data.isnull().sum()

data.shape

T = data["time"]
E = data["status"]
plt.hist(T, bins = 50)
plt.show()


"Fitting a non-parametric model [Kaplan Meier Curve]"

kmf = KaplanMeierFitter()
kmf.fit(durations = T, event_observed = E)
kmf.plot_survival_function()
plt.ylabel('Probality of survival')
plt.xlabel('time_duration')
plt.show()

kmf.survival_function_.plot()
plt.title('Survival function')

kmf.plot_cumulative_density()
plt.ylabel('prpbablity of death')
plt.show()

kmf.median_survival_time_

from lifelines.utils import median_survival_times

median_ = kmf.median_survival_time_
median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
print(median_)
print(median_confidence_interval_)

ax = plt.subplot(111)

m = (data["sex"] == 0)

kmf.fit(durations = T[m], event_observed = E[m], label = "Male")
kmf.plot_survival_function(ax = ax)

kmf.fit(T[~m], event_observed = E[~m], label = "Female")
kmf.plot_survival_function(ax = ax, at_risk_counts = True)

plt.title("Survival of different gender group")
plt.show()



"Fitting Cox Proportional Hazard Model"

data.head()

dummies_ecog = pd.get_dummies(data["ph.ecog"],
                         prefix = 'ecog')
dummies_ecog.head(4)

dummies_ecog = dummies_ecog[["ecog_1", "ecog_2"]]
data = pd.concat([data, dummies_ecog], 
                  axis = 1)
data.head()

data = data.drop("ph.ecog", axis = 1)
data.head()

cph = CoxPHFitter()
cph.fit(data, duration_col = 'time', event_col = 'status')

cph.print_summary()

plt.subplots(figsize=(10, 6))
cph.plot()
plt.show()

cph.plot_partial_effects_on_outcome(covariates = 'age',
                                    values = [50, 60, 70, 80],
                                    cmap = 'coolwarm')
plt.xlabel("Time_period(days)")
plt.ylabel("survival probablity")
plt.show()

cph.check_assumptions(data, p_value_threshold = 0.05)


from lifelines.statistics import proportional_hazard_test

results = proportional_hazard_test(cph, data, time_transform='rank')
results.print_summary(decimals=3, model="untransformed variables")

