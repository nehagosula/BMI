from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = ""
    category = ""
    weight = ""
    height = ""

    if request.method == "POST":
        try:
            weight = request.form.get("weight")
            height = request.form.get("height")

            weight = float(weight)
            height = float(height)

            if height <= 0:
                bmi = "Height must be greater than zero"
            else:
                bmi_val = weight / (height * height)
                bmi = f"{bmi_val:.2f}"

                # Classify BMI
                if bmi_val < 18.5:
                    category = "Underweight"
                elif bmi_val < 25:
                    category = "Normal weight"
                elif bmi_val < 30:
                    category = "Overweight"
                elif bmi_val < 35:
                    category = "Obesity Class I (Moderate)"
                elif bmi_val < 40:
                    category = "Obesity Class II (Severe)"
                else:
                    category = "Obesity Class III (Very severe / Morbid obesity)"

        except (ValueError, TypeError):
            bmi = "Invalid input"

    return render_template(
        "bmi1.html",
        bmi=bmi,
        category=category,
        weight=weight,
        height=height
    )

if __name__ == "__main__":
    app.run(debug=True)
