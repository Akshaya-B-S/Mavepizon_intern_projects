from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import pickle

app = Flask(__name__)
# Secret key is REQUIRED to use sessions in Flask
app.secret_key = "your_secret_key_here"

# Load saved model files
model = pickle.load(open("model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))


@app.route("/", methods=["GET"])
def home():
    # Retrieve result from session, then clear it so a refresh resets the page
    prediction_text = session.pop("prediction_text", None)
    form_data = session.pop("form_data", None)

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        form_data=form_data
    )


@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "Age": [int(request.form["Age"])],
        "Gender": [request.form["Gender"]],
        "Item Purchased": [request.form["Item Purchased"]],
        "Purchase Amount (USD)": [float(request.form["Purchase Amount (USD)"])],
        "Location": [request.form["Location"]],
        "Size": [request.form["Size"]],
        "Color": [request.form["Color"]],
        "Season": [request.form["Season"]],
        "Review Rating": [float(request.form["Review Rating"])],
        "Subscription Status": [request.form["Subscription Status"]],
        "Payment Method": [request.form["Payment Method"]],
        "Shipping Type": [request.form["Shipping Type"]],
        "Discount Applied": [request.form["Discount Applied"]],
        "Promo Code Used": [request.form["Promo Code Used"]],
        "Previous Purchases": [int(request.form["Previous Purchases"])],
        "Preferred Payment Method": [request.form["Preferred Payment Method"]],
        "Frequency of Purchases": [request.form["Frequency of Purchases"]]
    }

    df = pd.DataFrame(data)
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    pred = model.predict(df)
    category = le.inverse_transform(pred)[0]

    # Save to session
    session["prediction_text"] = f"Predicted Category : {category}"
    session["form_data"] = request.form.to_dict()

    # Redirect back to home route (GET request)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)