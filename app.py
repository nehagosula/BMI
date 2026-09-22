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
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))

            # Check for invalid values
            if weight <= 0 or height <= 0:
                bmi = "Please enter positive values."

            else:
                # BMI formula
                bmi_value = weight / (height ** 2)

                # Round BMI to 2 decimal places
                bmi = f"{bmi_value:.2f}"

                # Determine BMI category
                if bmi_value < 18.5:
                    category = "Underweight"

                elif bmi_value < 25:
                    category = "Normal weight"

                elif bmi_value < 30:
                    category = "Overweight"

                elif bmi_value < 35:
                    category = "Obesity Class I"

                elif bmi_value < 40:
                    category = "Obesity Class II"

                else:
                    category = "Obesity Class III"

        except (ValueError, TypeError):
            bmi = "Invalid input. Please enter numbers."


    return render_template(
        "index.html",
        bmi=bmi,
        category=category,
        weight=weight,
        height=height
    )


if __name__ == "__main__":
    app.run(debug=True)