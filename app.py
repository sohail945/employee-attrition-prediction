from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('E:\\Flask\\model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get data from form
        satisfaction_level = float(request.form['satisfaction_level'])
        last_performance_rating = float(request.form['last_performance_rating'])
        number_of_projects = int(request.form['number_of_projects'])
        avg_monthly_hours = float(request.form['avg_monthly_hours'])
        years_at_company = float(request.form['years_at_company'])
        had_work_accident = int(request.form['had_work_accident'])
        promoted_in_last_5_years = int(request.form['promoted_in_last_5_years'])
        department = int(request.form['department'])
        salary = int(request.form['salary'])  # New salary feature

        # Arrange the input data in the correct format for prediction
        input_data = np.array([[satisfaction_level, last_performance_rating, number_of_projects, 
                                avg_monthly_hours, years_at_company, had_work_accident, 
                                promoted_in_last_5_years, department, salary]])  # Updated to include salary

        # Predict whether the employee has left or not
        result = model.predict(input_data)

        # Interpret the prediction result
        prediction = "Employee will leave the company" if result[0] == 1 else "Employee will not leave the company"
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
