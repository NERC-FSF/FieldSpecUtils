"""Functions to convolve hyperspectral data to the equivalent bands of a selection of common satellite based sensors"""

import os
from pathlib import Path
import numpy as np
import pandas as pd
import shutil

def S2(spectra, Bands):
    """Sentinel-2 convolution""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')
        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        Band_2 = (np.trapezoid((convolution_process.iloc[89:184, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[89:184, 1]), axis = 0))
        Band_3 = (np.trapezoid((convolution_process.iloc[188:233, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[188:233, 2])))
        Band_4 = (np.trapezoid((convolution_process.iloc[296:344, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[296:344, 3]), axis = 0))
        Band_5 = (np.trapezoid((convolution_process.iloc[345:364, 4]), axis = 0)) / (np.trapezoid((Bands.iloc[345:364, 4]), axis = 0))
        Band_6 = (np.trapezoid((convolution_process.iloc[381:399, 5]), axis = 0)) / (np.trapezoid((Bands.iloc[381:399, 5]), axis = 0))
        Band_7 = (np.trapezoid((convolution_process.iloc[419:447, 6]), axis = 0)) / (np.trapezoid((Bands.iloc[419:447, 6]), axis = 0))
        Band_8 = (np.trapezoid((convolution_process.iloc[423:557, 7]), axis = 0)) / (np.trapezoid((Bands.iloc[423:557, 7]), axis = 0))
        Band_8a = (np.trapezoid((convolution_process.iloc[497:531, 8]), axis = 0)) / (np.trapezoid((Bands.iloc[497:531, 8]), axis = 0))
        Band_11 = (np.trapezoid((convolution_process.iloc[1189:1332, 11]), axis = 0)) / (np.trapezoid((Bands.iloc[1189:1332, 11]), axis = 0))
        Band_12 = (np.trapezoid((convolution_process.iloc[1728:1970, 12]), axis = 0)) / (np.trapezoid((Bands.iloc[1728:1970, 12]), axis = 0))
        convolved = {'Band name and centre wavelength (nm)': ["Band 2 - 490", "Band 3 - 560", "Band 4 - 665", "Band 5 - 705",
                                   "Band 6 - 740","Band 7 - 783", "Band 8 - 842", "Band 8a - 865",
                                   "Band 11 - 1610", "Band 12 - 2190"],
                         file_name+'SRF': [Band_2, Band_3, Band_4, Band_5, Band_6, Band_7, Band_8, Band_8a, Band_11, Band_12]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name and centre wavelength (nm)', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('Plots_with_convolved_bands.csv')
    
    shutil.rmtree(bands_Dir)
    shutil.rmtree(convolved_Dir)
    
def WV2(spectra, Bands):
    """WorldView-2 convolution, minus panchromatic""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')
        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        Coastal = (np.trapezoid((convolution_process.iloc[46:109, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[46:109, 0]), axis = 0))
        Blue = (np.trapezoid((convolution_process.iloc[92:166, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[92:166, 1]), axis = 0))
        Green = (np.trapezoid((convolution_process.iloc[156:237, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[156:237, 2]), axis = 0))
        Yellow = (np.trapezoid((convolution_process.iloc[234:283,3]), axis = 0)) / (np.trapezoid((Bands.iloc[234:283,3]), axis = 0))
        Red = (np.trapezoid((convolution_process.iloc[274:345,4]), axis = 0)) / (np.trapezoid((Bands.iloc[274:345,4]), axis = 0))
        RedEdge = (np.trapezoid((convolution_process.iloc[349:400, 5]), axis = 0)) / (np.trapezoid((Bands.iloc[349:400, 5]), axis = 0))
        NIRI = (np.trapezoid((convolution_process.iloc[415:552, 6]), axis = 0)) / (np.trapezoid((Bands.iloc[415:552, 6]), axis = 0))
        NIRII = (np.trapezoid((convolution_process.iloc[506:694, 7]), axis = 0)) / (np.trapezoid((Bands.iloc[506:694, 7]), axis = 0))
        convolved = {'Band name': ["Coastal", "Blue", "Green", "Yellow", "Red", "Red-Edge", "NIR I", "NIR II"],
                         file_name+'SRF': [Coastal, Blue, Green, Yellow, Red, RedEdge, NIRI, NIRII]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('WV2_Convolved.csv')
    
    shutil.rmtree(bands_Dir)
    shutil.rmtree(convolved_Dir)

def ASTER(spectra, Bands):
    """WorldView3 ASTER convolution Band 1 -- Band 9""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
        
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')
        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        Band_1 = (np.trapezoid((convolution_process.iloc[131:294, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[131:294, 0]), axis = 0))
        Band_2 = (np.trapezoid((convolution_process.iloc[240:381, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[240:381, 1]), axis = 0))
        Band_3N = (np.trapezoid((convolution_process.iloc[370:561, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[370:561, 2]), axis = 0))
        Band_3B = (np.trapezoid((convolution_process.iloc[370:561, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[370:561, 3]), axis = 0))
        Band_4 = (np.trapezoid((convolution_process.iloc[1178:1418, 4]), axis = 0)) / (np.trapezoid((Bands.iloc[1178:1418, 4]), axis = 0))
        Band_5 = (np.trapezoid((convolution_process.iloc[1754:1945, 5]), axis = 0)) / (np.trapezoid((Bands.iloc[1754:1945, 5]), axis = 0))
        Band_6 = (np.trapezoid((convolution_process.iloc[1777:1947, 6]), axis = 0)) / (np.trapezoid((Bands.iloc[1777:1947, 6]), axis = 0))
        Band_7 = (np.trapezoid((convolution_process.iloc[1850:2042, 7]), axis = 0)) / (np.trapezoid((Bands.iloc[1850:2042, 7]), axis = 0))
        Band_8 = (np.trapezoid((convolution_process.iloc[1898:2096, 8]), axis = 0)) / (np.trapezoid((Bands.iloc[1189:1332, 8]), axis = 0))
        Band_9 = (np.trapezoid((convolution_process.iloc[1946:2148, 9]), axis = 0)) / (np.trapezoid((Bands.iloc[1946:2148, 9]), axis = 0))
        convolved = {'Band name and centre wavelength (nm)': ["Band 1 - 560", "Band 2 - 665", "Band 3 Nadir - 820 ", "Band 3 Backward - 820",
                                   "Band 4 - 1650","Band 5 - 2165", "Band 6 - 2205", "Band 7 - 2260", "Band 8 - 2330", "Band 9 - 2395"],
                         file_name+'SRF': [Band_1, Band_2, Band_3N, Band_3B, Band_4, Band_5, Band_6, Band_7, Band_8, Band_9]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name and centre wavelength (nm)', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('Plots_with_convolved_bands.csv')
    
    shutil.rmtree(bands_Dir)
    shutil.rmtree(convolved_Dir)

def Dove(spectra, Bands):
    """Dove convolution""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')
        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        Blue = (np.trapezoid((convolution_process.iloc[91:650, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[91:650, 0]), axis = 0))
        Green = (np.trapezoid((convolution_process.iloc[180:250, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[180:250, 1]), axis = 0))
        Red = (np.trapezoid((convolution_process.iloc[284:595, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[284:595, 2]), axis = 0))
        NIR = (np.trapezoid((convolution_process.iloc[490:544, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[490:544, 3]), axis = 0))
        convolved = {'Band name': ["Blue", "Green", "Red", "NIR"],
                         file_name+'SRF': [Blue, Green, Red, NIR]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('Dove_Convolved.csv')
    
    shutil.rmtree(bands_Dir)
    shutil.rmtree(convolved_Dir)

def SuperDove(spectra, Bands):
    """Dove convolution""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')
        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        CoastalBlue = (np.trapezoid((convolution_process.iloc[77:110, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[77:110, 0]), axis = 0))
        Blue = (np.trapezoid((convolution_process.iloc[91:650, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[91:650, 1]), axis = 0))
        GreenI = (np.trapezoid((convolution_process.iloc[157:208, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[157:208, 2]), axis = 0))
        GreenII = (np.trapezoid((convolution_process.iloc[180:250, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[180:250, 3]), axis = 0))
        Yellow = (np.trapezoid((convolution_process.iloc[243:284, 4]), axis = 0)) / (np.trapezoid((Bands.iloc[243:284, 4]), axis = 0))
        Red = (np.trapezoid((convolution_process.iloc[284:595, 5]), axis = 0)) / (np.trapezoid((Bands.iloc[284:595, 5]), axis = 0))
        RedEdge = (np.trapezoid((convolution_process.iloc[342:373, 6]), axis = 0)) / (np.trapezoid((Bands.iloc[342:373, 6]), axis = 0))
        NIR = (np.trapezoid((convolution_process.iloc[490:544, 7]), axis = 0)) / (np.trapezoid((Bands.iloc[490:544, 7]), axis = 0))
        convolved = {'Band name': ["Coastal Blue", "Blue", "Green-I", "Green-II", "Yellow", "Red", "Red Edge", "NIR"],
                         file_name+'SRF': [CoastalBlue, Blue, GreenI, GreenII, Yellow, Red, RedEdge, NIR]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('Superdove_Convolved.csv')

def GeoEYE(spectra, Bands):
    """GeoEYE convolution""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')
        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        Blue = (np.trapezoid((convolution_process.iloc[0:650, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[0:650, 0]), axis = 0))
        Green = (np.trapezoid((convolution_process.iloc[0:650, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[0:650, 1]), axis = 0))
        Red = (np.trapezoid((convolution_process.iloc[0:650, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[0:650, 2]), axis = 0))
        NIR = (np.trapezoid((convolution_process.iloc[0:650, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[0:650, 3]), axis = 0))
        convolved = {'Band name': ["Blue 484.52", "Green 547.870", "Red 675.19", "NIR 836.52"],
                         file_name+'SRF': [Blue, Green, Red, NIR]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('GeoEYE_Convolved.csv')

def WV3(spectra, Bands):
    """Maxar WorldView-3 convolution""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')

        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        CoastalBlue = (np.trapezoid((convolution_process.iloc[0:760, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 0]), axis = 0))
        Blue = (np.trapezoid((convolution_process.iloc[0:760, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 1]), axis = 0))
        Green = (np.trapezoid((convolution_process.iloc[0:760, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 2]), axis = 0))
        Yellow = (np.trapezoid((convolution_process.iloc[0:760, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 3]), axis = 0))
        Red = (np.trapezoid((convolution_process.iloc[0:760, 4]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 4]), axis = 0))
        RedEdge = (np.trapezoid((convolution_process.iloc[0:760, 5]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 5]), axis = 0))
        NIRI = (np.trapezoid((convolution_process.iloc[0:760, 6]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 6]), axis = 0))
        NIRII = (np.trapezoid((convolution_process.iloc[0:760, 7]), axis = 0)) / (np.trapezoid((Bands.iloc[0:760, 7]), axis = 0))
        SWIRI = (np.trapezoid((convolution_process.iloc[792:1293, 8]), axis = 0)) / (np.trapezoid((Bands.iloc[792:1293, 8]), axis = 0))
        SWIRII = (np.trapezoid((convolution_process.iloc[1139:1291, 9]), axis = 0)) / (np.trapezoid((Bands.iloc[1139:1291, 9]), axis = 0))        
        SWIRIII = (np.trapezoid((convolution_process.iloc[1270:1350, 10]), axis = 0)) / (np.trapezoid((Bands.iloc[1270:1350, 10]), axis = 0))        
        SWIRIV = (np.trapezoid((convolution_process.iloc[1330:1445, 11]), axis = 0)) / (np.trapezoid((Bands.iloc[1330:1445, 11]), axis = 0))        
        SWIRV = (np.trapezoid((convolution_process.iloc[1760:1870, 12]), axis = 0)) / (np.trapezoid((Bands.iloc[1760:1870, 12]), axis = 0))        
        SWIRVI = (np.trapezoid((convolution_process.iloc[1800:1920, 13]), axis = 0)) / (np.trapezoid((Bands.iloc[1800:1920, 13]), axis = 0))        
        SWIRVII = (np.trapezoid((convolution_process.iloc[1855:1970, 14]), axis = 0)) / (np.trapezoid((Bands.iloc[1855:1970, 14]), axis = 0))        
        SWIRVIII = (np.trapezoid((convolution_process.iloc[1900:2045, 15]), axis = 0)) / (np.trapezoid((Bands.iloc[1900:2045, 15]), axis = 0))
        convolved = {'Band name': ["Coastal Blue 427.38 nm ", "Blue 481.92 nm", "Green 547.14 nm",
                                   "Yellow 604.23 nm", "Red 660.11 nm", "RedEdge 722.73 nm", "NIR-I 824.04 nm", "NIR-II 913.65 nm",
                                   "SWIR-I 1209.06 nm", "SWIR-II 1571.61 nm", "SWIR-III 1661.10 nm", "SWIR-IV 1729.54 nm",
                                   "SWIR-V 2163.69 nm", "SWIR-VI 2202.16 nm", "SWIR-VII 2259.32 nm", "SWIR-VIII 2329.22 nm", ],
                         file_name+'SRF': [CoastalBlue, Blue, Green, Yellow, Red, RedEdge, NIRI, NIRII,
                                           SWIRI, SWIRII, SWIRIII, SWIRIV, SWIRV, SWIRVI, SWIRVII, SWIRVIII]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

def Legion1(spectra, Bands):
    """Maxar Legion (Sensor 1) convolution""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')

        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        CoastalBlue = (np.trapezoid((convolution_process.iloc[39:150, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[39:150, 0]), axis = 0))
        Blue = (np.trapezoid((convolution_process.iloc[39:559, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[39:559, 1]), axis = 0))
        Green = (np.trapezoid((convolution_process.iloc[39:559, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[39:559, 2]), axis = 0))
        Pan = (np.trapezoid((convolution_process.iloc[49:500, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[49:500, 3]), axis = 0))
        Yellow = (np.trapezoid((convolution_process.iloc[199:350, 4]), axis = 0)) / (np.trapezoid((Bands.iloc[199:350, 4]), axis = 0))        
        Red = (np.trapezoid((convolution_process.iloc[249:400, 5]), axis = 0)) / (np.trapezoid((Bands.iloc[249:400, 5]), axis = 0))        
        RedEdgeI = (np.trapezoid((convolution_process.iloc[299:400, 6]), axis = 0)) / (np.trapezoid((Bands.iloc[299:400, 6]), axis = 0))
        RedEdgeII = (np.trapezoid((convolution_process.iloc[349:450, 7]), axis = 0)) / (np.trapezoid((Bands.iloc[349:450, 7]), axis = 0))        
        NIRI = (np.trapezoid((convolution_process.iloc[349:559, 8]), axis = 0)) / (np.trapezoid((Bands.iloc[349:559, 8]), axis = 0))
        convolved = {'Band name': ["Coastal Blue 425.18 nm ", "Blue 481.26 nm", "Green 546.50 nm",
                                   "Panchromatic 630.14 nm", "Yellow 604.17 nm", "Red 660.69 nm",
                                   "RedEdgeI 703.98 nm", "RedEdgeII 737.34 nm", "NIRI 831.57 nm" ],
                         file_name+'SRF': [CoastalBlue, Blue, Green, Pan, Yellow, Red, RedEdgeI, RedEdgeII, NIRI]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('MaxarLegionI_Convolved.csv')
    
    shutil.rmtree(bands_Dir)
    shutil.rmtree(convolved_Dir)

def Legion2(spectra, Bands):
    """Maxar Legion (Sensor 2) convolution""" 
    cwd = Path.cwd()
    Home_Dir = cwd
    bands_Dir = str(cwd / "bands") 
    convolved_Dir = str(cwd / "convolved")
    if (Path(bands_Dir)).exists() and (Path(bands_Dir)).is_dir():
        shutil.rmtree(Path(bands_Dir))
        os.mkdir(bands_Dir)
    else:
        os.mkdir(bands_Dir)
    if (Path(convolved_Dir)).exists() and (Path(convolved_Dir)).is_dir():
        shutil.rmtree(Path(convolved_Dir))
        os.mkdir(convolved_Dir)
    else:
        os.mkdir(convolved_Dir)
        
    while True:
        water_bands_removed = input("Are there regions where water bands have been removed in your data (Y or N)?: ")
        if water_bands_removed == "Y":
            np.seterr(divide="ignore")
            break
        elif water_bands_removed == "N":
            break
        else:
            print("Input a valid option (Y or N)")
            continue
    
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')

        
    for band_file in os.scandir(bands_Dir):
        file_name = Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        CoastalBlue = (np.trapezoid((convolution_process.iloc[43:105, 0]), axis = 0)) / (np.trapezoid((Bands.iloc[43:105, 0]), axis = 0))
        Blue = (np.trapezoid((convolution_process.iloc[94:169, 1]), axis = 0)) / (np.trapezoid((Bands.iloc[94:169, 1]), axis = 0))        
        Green = (np.trapezoid((convolution_process.iloc[143:243, 2]), axis = 0)) / (np.trapezoid((Bands.iloc[143:243, 2]), axis = 0))        
        Pan = (np.trapezoid((convolution_process.iloc[91:475, 3]), axis = 0)) / (np.trapezoid((Bands.iloc[91:475, 3]), axis = 0))        
        Yellow = (np.trapezoid((convolution_process.iloc[214:308, 4]), axis = 0)) / (np.trapezoid((Bands.iloc[214:308, 4]), axis = 0))        
        Red = (np.trapezoid((convolution_process.iloc[265:368, 5]), axis = 0)) / (np.trapezoid((Bands.iloc[265:368, 5]), axis = 0))        
        RedEdgeI = (np.trapezoid((convolution_process.iloc[338:372, 6]), axis = 0)) / (np.trapezoid((Bands.iloc[338:372, 6]), axis = 0))        
        RedEdgeII = (np.trapezoid((convolution_process.iloc[350:429, 7]), axis = 0)) / (np.trapezoid((Bands.iloc[350:429, 7]), axis = 0))        
        NIRI = (np.trapezoid((convolution_process.iloc[405:558, 8]), axis = 0)) / (np.trapezoid((Bands.iloc[349:558, 8]), axis = 0))        
        convolved = {'Band name': ["Coastal Blue 425.54 nm ", "Blue 480.89 nm", "Green 546.15 nm",
                                   "Panchromatic 628.90 nm", "Yellow 605.22 nm", "Red 660.53 nm",
                                   "RedEdgeI 704.68 nm", "RedEdgeII 739.76 nm", "NIRI 830.50 nm" ],
                         file_name+'SRF': [CoastalBlue, Blue, Green, Pan, Yellow, Red, RedEdgeI, RedEdgeII, NIRI]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('MaxarLegionII_Convolved.csv')
    
    shutil.rmtree(bands_Dir)
    shutil.rmtree(convolved_Dir)
