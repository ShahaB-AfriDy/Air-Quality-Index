from django.shortcuts import render,HttpResponseRedirect
from joblib import load
import warnings
from RFR.form import RFR_Form

# Create your views here.


Model_path = "E:\Python in Sublime\DJango Framework\Machine Learning\Air_Pollution\RFR\static\model\RFR_Model.joblib"


predicted_value = None

def RFR_Model(request):
    global predicted_value
    if request.method == 'POST':
        RFR_form = RFR_Form(request.POST)
        if RFR_form.is_valid():
            input_list = RFR_form.cleaned_data.values()
            input_list = list(map(float,input_list))
            print(input_list)
           
            # input_list = array(input_list).reshape(1,6)
            predicted_value = load_model(input_list)
            RFR_form = RFR_Form()
            return HttpResponseRedirect("/RFR-result/")
         
    else:
        RFR_form = RFR_Form()

    return render(request,template_name="RFR.html",context={"RFR_form":RFR_form})




def RFR_Result(request):
    if 0 <= predicted_value <= 50:
        result = "Good"
    elif 51 <= predicted_value <= 100:
        result = "Satisfactory"
    elif 101 <= predicted_value <= 150:
        result = "Moderate"
    elif 151 <= predicted_value <= 200:
        result = "Moderate"
    elif 201 <= predicted_value <= 300:
        result = "Poor"
    else:
        result = "Severe"
    # elif 301 <= predicted_value <= 500:
    #     result = "Severe"
    return render(request,template_name='RFR_Result.html',context={"prediction":result})

def load_model(Input_data):
    model = load(Model_path)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # predictions = model.predict([[68.99, 189.57, 27.86, 1.07, 11.69, 91.18]])
        predictions = model.predict([Input_data])
    return predictions

