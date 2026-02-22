# ---
# Project: AI Exam Score Predictor
# Author: Pramod Wickramanayake
# Model: Linear Regression (Scikit-learn)
# ---

import numpy as np
from sklearn.linear_model import LinearRegression

def ai_score_predictor():
    # 1. Past Data: Study Hours vs Exam Score
    hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]). reshape(-1, 1)
    scores = np.array([35, 45, 50, 58, 65, 75, 82, 90])

    # 2. Creating and Trainning the AI Model
    model = LinearRegression()
    model.fit(hours, scores)

    # 3. Making aPrediction
    test_hours = 10
    predicted_val = model.predict(np.array([[test_hours]]))

    print(f"___ AI Exam Predictor ___")
    print(f"If you study for {test_hours} hours, predicted score is: {predicted_val[0]:.2f}%")
    
if __name__ == "__main__":
    ai_score_predictor()