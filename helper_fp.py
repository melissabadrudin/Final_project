import pickle

def run_model(mylist):
    #receives a list and stores it in a variable x_new
    X_new = [mylist]
    stand_virtual = 'finalized_model.pkl'    
    #Loads the trained model from the pickle file
    with open(stand_virtual, 'rb') as file:
        pickle_model = pickle.load(file)
    
    prediction = pickle_model.predict(X_new)
    return prediction


#print(pickle_model.predict([[0.3,model,0.5,0.5]]))


#print(run_model([0,2020,1000000,5,5,5,112,1600,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1]))

#Simulate input
user_inputs = {'Brand' : 'Renault' , 'Fuel' :'Gasolina' , 'Transmission' : 'Manual', 'AC':'ACIndependente','Condition':'Usados'}
extra_inputs = {"Year" : 2019, "Km" : 20000, "Door": 5, "Seats": 5, "TransmissionNr":6, "Power":110, "Cylinder Engine":1600}

# definir uma função para receber os inputs e dar o final product


import pandas as pd
data = pd.read_csv('df_dummie.csv')
data=data.drop(['Unnamed: 0','Year','Km','Doors','Seats','TransmissionNr','Power','Cylinder Engine','Price'], axis=1)

new_data=data.columns.str.replace("Brand_","").str.replace("Fuel_","").str.replace("Transmission_","").str.replace("AC_","").str.replace("Condition_","")
new=pd.DataFrame(new_data)

newnew=new.rename(columns={0:'keys'})
keys= newnew['keys']


new_dict= {}

for key in keys:
    new_dict[key]=0
    
for in_key in user_inputs.keys():
    for key in new_dict.keys():
        if user_inputs[in_key]in key:
            new_dict[key]+=1
data_1 = pd.DataFrame.from_dict(new_dict, orient = 'index').T
data_2 = pd.DataFrame.from_dict(extra_inputs, orient = 'index').T
final_result = pd.concat([data_2,data_1], axis = 1)       
        
print(final_result)
        
        