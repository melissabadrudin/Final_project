

import pandas as pd
import numpy as np
import pickle
def run_model(parameter_1,parameter_2,parameter_3,parameter_4,parameter_5,parameter_6,parameter_7,parameter_8,parameter_9,parameter_10,parameter_11,parameter_12):
    pickle_filename = 'finalized_model.pkl'
    # Load from fil
    my_dict={'Year':0, 'Km':0,'Door':0,'Seats':0,'TransmissionNr':0,'Power':0,'Cylinder Engine':0,'Abarth':0,'Aixam':0,'AlfaRomeo':0,'AstonMartin':0,'Audi':0,'Austin':0,'AustinHealey':0,'BMW':0,'Bellier':0,'Bentley':0,'Chatenet':0,'Chevrolet':0,'Chrysler':0,'Citroën':0,'DS':0,'Dacia':0,'Daewoo':0,'Datsun':0,'Dodge':0,'Ferrari':0,'Fiat':0,'Fisker':0,'Ford':0,'Honda':0,'Hummer':0,'Hyundai':0,'Infiniti':0,'Isuzu':0,'Jaguar':0,'Jeep':0,'Kia':0,'Lamborghini':0,'Lancia':0,'LandRover':0,'Lexus':0,'Ligier':0,'Lotus':0,'MG':0,'MINI':0,'Maserati':0,'Mazda':0,'McLaren':0,'Mercedes-Benz':0,'Microcar':0,'Mitsubishi':0,'Morgan':0,'Morris':0,'Nissan':0,'Opel':0,'Outranãolistada':0,'Peugeot':0,'Porsche':0,'Renault':0,'RollsRoyce':0,'Rover':0,'SEAT':0,'Saab':0,'Skoda':0,'Smart':0,'SsangYong':0,'Subaru':0,'Suzuki':0,'Tesla':0,'Toyota':0,'Triumph':0,'UMM':0,'VW':0,'Volvo':0,'Diesel':0,'Eléctrico':0,'GPL':0,'Gasolina':0,'Híbrido(Diesel)':0,'Híbrido(Gasolina)':0,'Automática':0,'Manual':0,'ACAutomático':0,'ACIndependente':0,'ACManual':0,'Usados':0}

    my_dict['Year']= parameter_1 
    my_dict['Km']= parameter_2
    my_dict['Door']= parameter_3
    my_dict['Seats']= parameter_4
    my_dict['TransmissionNr']= parameter_5
    my_dict['Power']= parameter_6
    my_dict['Cylinder Engine']= parameter_7
    my_dict[parameter_8]=1
    my_dict[parameter_9]=1
    my_dict[parameter_10]=1
    my_dict[parameter_11]=1
    my_dict[parameter_12]=1
    
    to_predict = np.array(list(my_dict.values()))
    with open(pickle_filename, 'rb') as file:
        pickle_filename = pickle.load(file)
        
    prediction = pickle_filename.predict([to_predict])
   
    return prediction






print(run_model(2019,10000,5,5,5,112,1600,'Ford','Gasolina','Manual','ACAutomático','Usados')) 

