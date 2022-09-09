import os

CSV_FILE_PATH = 'enter_path'


PORT_NUMBER = 9999

# MODEL_FILE_PATH = r"D:\RahulK\Velocity_May_22\08_17_Flask_medical_insurence_KNN\artifacts\KNN_Regression_Model.pkl"
# MODEL_FILE_PATH = r"G:\4)Velocity\08-Aug\08_17_Flask_medical_insurence_KNN\artifacts\KNN_Regression_Model.pkl"
MODEL_FILE_PATH = os.path.join('artifacts','KNN_Regression_Model.pkl')

# JSON_FILE_PATH = r"D:\RahulK\Velocity_May_22\08_17_Flask_medical_insurence_KNN\artifacts\project_data.json"
# JSON_FILE_PATH = r"G:\4)Velocity\08-Aug\08_17_Flask_medical_insurence_KNN\artifacts\project_data.json"
JSON_FILE_PATH = os.path.join('artifacts',"project_data.json")


# SCALING_FILE_PATH = r'D:\RahulK\Velocity_May_22\08_17_Flask_medical_insurence_KNN\artifacts\Std_Scaling.pkl'
# SCALING_FILE_PATH = r"G:\4)Velocity\08-Aug\08_17_Flask_medical_insurence_KNN\artifacts\Std_Scaling.pkl"
SCALING_FILE_PATH = os.path.join('artifacts',"Std_Scaling.pkl")

