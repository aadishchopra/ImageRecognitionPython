# install code runner extension 
# Run below code to clear your terminal 
import os 
os.system("cls")

# Write a function to load all the required libraries at startup

def load_libraries_on_startup():

    import os 
    base_packages=['pip']
    packages_list=['numpy','scipy','scikit-learn','Pillow']
    base_len=len(base_packages)
    pack_len=len(packages_list)

    for package in range(base_len):
        print("Importing "+base_packages[package])
        exec('import ' +base_packages[package])
        
    for package in range(pack_len):
        print("Installing "+packages_list[package])
        os.system('pip install '+packages_list[package])
        print("Importing "+packages_list[package])
        if(packages_list[package]=="scikit-learn"):
            exec('import sklearn')
        elif(packages_list[package]=="Pillow"):
            exec('from PIL import Image')
        else:            
            exec('import ' +packages_list[package]) 
        




