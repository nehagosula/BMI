def bmi(choice,height,weight):
    if choice==1:
     return (weight/(height**2))*703
    elif choice==2:
        return (weight/(height**2))
    else:
        print("Enter valid values in appropriate units\n")
print(" Below 18.5	Underweight\n 18.5 – 24.9	Normal weight\n 25.0 – 29.9	Overweight\n 30.0 – 34.9	Obesity Class I\n 35.0 – 39.9	Obesity Class II\n 40.0 and above	Obesity Class III (Severe)\n")
print("1-Imperial Units (pounds or inches)\n2-Metric Units (kgs and m)")
print("Enter your choice")
choice=int(input())
if choice==1:
    height=float(input("Enter height in Inches\n"))
    weight=float(input("Enter weight in pounds\n"))
    BMI=bmi(choice,height,weight)
    print("Your BMI is: ",BMI)
elif choice==2:
    height=float(input("Enter height in meters\n"))
    weight=float(input("Enter weight in kilograms\n"))
    BMI=(weight/(height**2))
    print("Your BMI is: ",BMI)
else:
    bmi(0,0,0)
if BMI<18.5 and BMI>0:
    print("Underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("Normal weight")
elif BMI>=25.0 and BMI<=29.9:
    print("Overweight")
elif BMI>=30.0 and BMI<=34.9:
    print("Obesity class I")
elif BMI>=35.0 and BMI<=39.9:
    print("Obesity Class II")
elif BMI>=40.0:
    print("Obesity Class III(Severe)")
else:
  print("Invalid value of BMI")
