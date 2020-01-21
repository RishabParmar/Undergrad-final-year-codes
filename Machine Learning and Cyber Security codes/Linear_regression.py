import statistics
import matplotlib.pyplot as plt


def calculateProduct(hours, risk_score):
    product = []
    count = len(hours)
    for i in range(0, count):
        product.append(hours[i] * risk_score[i])
    product = sum(product)
    return product


def calculateHoursSquare(hours):
    hours_sum = 0
    for x in hours:
        hours_sum += x * x
    return hours_sum


def plot_best_fit_line(equation, hours, risk_score, slope):
    best_fit_line = []
    for x in hours:
        # First replaces the 'x' in y = mx+c and then eval() internally converts the string into a math statement and
        # solves it
        plot_point = eval(equation.replace("x", "*" + str(x)))
        best_fit_line.append(plot_point)
    plt.plot(hours, best_fit_line, c='r', label="Line of best fit")
    plt.scatter(hours, risk_score, c='#336699', label="Data points")
    plt.legend(loc="upper left")
    if slope < 0:
        plt.legend("upper right")
    plt.xlabel("Hours of driving")
    plt.ylabel("Score")
    plt.show()


def linear_regression():
    # independent data
    #  8, 2, 11, 6, 5, 4, 12, 9, 6, 1
    hours = [10, 9, 2, 15, 10, 16, 11, 16]
    # dependent data
    #  3, 10, 3, 6, 8, 12, 1, 4, 9, 14
    risk_score = [95, 80, 10, 50, 45, 98, 38, 93]

    hours_mean = statistics.mean(hours)
    risk_score_mean = statistics.mean(risk_score)

    print("Hours mean :", hours_mean)
    print("Risk score mean :", risk_score_mean)

    combined_product = calculateProduct(hours, risk_score)
    print("The combined product :", combined_product)

    hours_square = calculateHoursSquare(hours)
    print("The squared hours sum :", hours_square)

    Sxy = combined_product - (sum(hours) * sum(risk_score)) / len(hours)
    print("Sxy :", Sxy)
    Sxx = hours_square - (sum(hours) * sum(hours)) / len(hours)
    print("Sxx :", Sxx)

    # Calculating regression slope
    regression_slope = Sxy / Sxx
    print("The regression_slope :", regression_slope)
    # Calculating intercept
    intercept = risk_score_mean - (regression_slope * hours_mean)
    print("The intercept :", intercept)
    # Equation of best fit line : y = mx + c => y = regression_slope*x + intercept
    equation_best_fit_line = str(regression_slope) + "x" + " " + "+" + " " + str(intercept)
    print("The equation of best fit line :", equation_best_fit_line)

    # Plotting the best fit line:
    plot_best_fit_line(equation_best_fit_line, hours, risk_score, regression_slope)


if __name__ == '__main__':
    linear_regression()
