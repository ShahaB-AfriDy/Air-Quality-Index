from django.shortcuts import render,HttpResponseRedirect
from joblib import load
import warnings
from MLR.form import MLR_Form

# Create your views here.


Model_path = "E:\Python in Sublime\DJango Framework\Machine Learning\Air_Pollution\MLR\static\model\MLR_Model.joblib"


predicted_value = None

def MLR_Model(request):
    global predicted_value
    if request.method == 'POST':
        MLR_form = MLR_Form(request.POST)
        if MLR_form.is_valid():
            input_list = MLR_form.cleaned_data.values()
            input_list = list(map(float,input_list))
            print(input_list)
           
            # input_list = array(input_list).reshape(1,6)
            predicted_value = load_model(input_list)
            MLR_form = MLR_Form()
            return HttpResponseRedirect("/MLR-result/")
         
    else:
        MLR_form = MLR_Form()

    return render(request,template_name="MLR.html",context={"MLR_form":MLR_form})




def MLR_Result(request):
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
    return render(request,template_name='MLR_Result.html',context={"prediction":result})

def load_model(Input_data):
    model = load(Model_path)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # predictions = model.predict([[68.99, 189.57, 27.86, 1.07, 11.69, 91.18]])
        predictions = model.predict([Input_data])
    return predictions

