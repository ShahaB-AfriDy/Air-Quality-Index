from django.shortcuts import render,HttpResponseRedirect
from joblib import load
import warnings
from XGB.form import XGB_Form

# Create your views here.


Model_path = "E:\Python in Sublime\DJango Framework\Machine Learning\Air_Pollution\XGB\static\model\XGB_Model.joblib"


predicted_value = None

def XGB_Model(request):
    global predicted_value
    if request.method == 'POST':
        XGB_form = XGB_Form(request.POST)
        if XGB_form.is_valid():
            input_list = XGB_form.cleaned_data.values()
            input_list = list(map(float,input_list))           
            # input_list = array(input_list).reshape(1,6)
            predicted_value = load_model(input_list)
            XGB_form = XGB_Form()
            return HttpResponseRedirect("/XGB-result/")
         
    else:
        XGB_form = XGB_Form()

    return render(request,template_name="XGB.html",context={"XGB_form":XGB_form})




def XGB_Result(request):
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
    return render(request,template_name='XGB_Result.html',context={"prediction":result})

def load_model(Input_data):
    model = load(Model_path)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # predictions = model.predict([[68.99, 189.57, 27.86, 1.07, 11.69, 91.18]])
        predictions = model.predict([Input_data])
    return predictions

