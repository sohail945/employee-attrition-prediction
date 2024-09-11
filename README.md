# Employee Attrition Prediction

## Project Overview
The **Employee Attrition Prediction** project is a machine learning application that predicts whether an employee will leave or stay at a company based on various features such as job satisfaction, performance, number of projects, years at the company, and more. This project uses a Random Forest Classifier to perform binary classification and is integrated with a Flask web application.

---

## Features
- **Model**: Random Forest Classifier
- **Inputs**: 
  - Satisfaction level
  - Last performance rating
  - Number of projects
  - Average monthly hours
  - Years at company
  - Had work accident
  - Promoted in the last 5 years
  - Department (encoded)
  - Salary level (encoded)
- **Output**: Binary prediction (1 = employee will leave, 0 = employee will stay)

---

## Installation Guide

### Prerequisites
- **Python 3.x**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **Pickle**
  
### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/employee_attrition_prediction.git
   cd employee_attrition_prediction
