from django.shortcuts import   render, redirect
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from jupyter_console import app
from sklearn.preprocessing import StandardScaler
#app = Django(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
#model = pickle.load(open('decision_tree.pkl', 'rb'))
#model = pickle.load(open('D:\ML Project/rg.pkl', 'rb'))
def index(request):
    return render(request, 'index.html')
#@app.route('/',methods=['GET'])
'''
import gdown
numpy==1.21.2
file_id = "1Cd8y2riT1HpM1PUsWjOja7OJPjm3ZWmS"
file_url = f"https://drive.google.com/uc?id={file_id}"
output_path = "rg.pkl"  # Updated file name

## Download the file
gdown.download(file_url, output_path, quiet=False)

## Load the .pkl file
with open(output_path, 'rb') as file:
    model = pickle.load(file)

print("Data loaded from .pkl file:", model)


'''
standard_to = StandardScaler()
#@app.route("/predict", methods=['POST'])

context ={
    'prediction_texts' : 0,
}

def predictt(request):
    print("Hello")
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.POST['Year'])
        Present_Price=float(request.POST['Present_Price'])
        Kms_Driven=int(request.POST['Kms_Driven'])
        Kms_Driven2=np.log(Kms_Driven)
        Owner=int(request.POST['Owner'])
        Fuel_Type_Petrol=request.POST['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        elif(Fuel_Type_Diesel=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        Year=2021-Year
        Seller_Type_Individual=request.POST['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        Transmission_Mannual=request.POST['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0

        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        #prediction = model.predict([[7,45000,1,6,1,0,0,1]])

        output=round(prediction[0],2)
        if output < 0:
            context['prediction_texts'] = "Sorry you cannot sell this car"
            return redirect('/predictt/')
        else:
            context['prediction_texts'] = "You Can Sell The Car at {}".format(output)
            return redirect('/predictt/')
    else:
        return render(request, 'index.html',context)

#if __name__=="__main__":
 #   app.run(debug=True)

