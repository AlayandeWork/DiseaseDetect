from flask import Flask, render_template, request

app = Flask(__name)

# Route to render the symptom input form
@app.route('/')
def input_form():
    return render_template('HomePage.html')

# Route to handle form submission and display the result
@app.route('/predict', methods=['POST'])
def predict_disease():
    # Retrieve user inputs from the form
    name = request.form['name']
    age_range = request.form['age_range']
    symptoms = request.form.getlist('symptoms')  # Use getlist for checkboxes/radio buttons

    # Implement your prediction logic here using the user inputs and database

    # For now, let's assume a simple prediction
    predicted_disease = "Malaria"  # Replace with your actual prediction logic

    # Render the result page and pass the predicted disease as a variable
    return render_template('result.html', name=name, age_range=age_range, predicted_disease=predicted_disease)

if __name__ == '__main__':
    app.run(debug=True)
