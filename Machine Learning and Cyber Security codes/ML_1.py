import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

hours = [10, 9, 2, 15, 10, 16, 11, 16]
risk_score = [95, 80, 10, 50, 45, 98, 38, 93]

hours_mean = np.mean(hours)
print("The mean of hours :", hours_mean)
risk_score_mean = np.mean(risk_score)
print("The mean of risk_score :", risk_score_mean)

numerator = 0
denominator = 0
for _ in range(len(hours)):
    numerator += (hours[_] - hours_mean) * (risk_score[_] - risk_score_mean)
    denominator += (hours[_] - hours_mean)**2
print("The numerator :", numerator)
print("The denominator :", denominator)
b1 = numerator/denominator
b0 = risk_score_mean - (b1*hours_mean)
print("b0 (intercept) :", b0)
print("b1 (Slope) :", b1)

best_fit_line = []
for _ in range(len(hours)):
    best_fit_line.append((b1*hours[_])+b0)
print("Best fit line :", best_fit_line)

# Plotting the line
plt.plot(hours, best_fit_line, c='r', label="Line of best fit")

# Plotting the points
plt.scatter(hours, risk_score, c='b', label="Data points")

# Legend and extra info
plt.legend(loc="upper left")
plt.xlabel("Hours")
plt.ylabel("Risk Score")
plt.show()

# RMSE
rmse = 0
for _ in range(len(hours)):
    rmse += np.square(best_fit_line[_] - risk_score[_])
print("RMSE :", np.sqrt(rmse/len(hours)))

# r2/ Coefficient of determination
ss_r = 0
ss_t = 0
for _ in range(len(hours)):
    ss_r += np.square(best_fit_line[_] - risk_score[_])
    ss_t += np.square(risk_score[_] - risk_score_mean)
print("The r2 value :", 1-(ss_r/ss_t))

# Linear Regression using Library

# hours = np.array(hours).reshape(np.array(hours).shape[0], 1)
hours = np.array(hours).reshape(len(hours), 1)
model = LinearRegression()
print(hours)
model.fit(hours, risk_score)
print("r2 score:", model.score(hours, risk_score))
predicted = model.predict(hours)
print("The predicted values: ", predicted)
plt.plot(hours, predicted, c='r', label="Line of best fit")
plt.legend("upper left")
plt.scatter(hours, risk_score, c='b', label="Data points")
plt.xlabel("Hours")
plt.ylabel("Risk Score")
plt.show()
