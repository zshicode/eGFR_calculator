cr_original = 80 # umol/L
gender = 'm' # 'm' or 'f', i.e., male or female
age = 30
weight = 65 # kg
height = 175 # cm
cr = cr_original/88.42 # mg/dL
bsa = 0.007184*pow(weight,0.425)*pow(height,0.725) #m^2, body surface area

def CKD_EPI(cr,gender,age):
    if gender == 'm':
        k = 0.9
        a = -0.302
    else:
        k = 0.7
        a = -0.241
    
    egfr = 142*pow(min(cr/k,1),a)*pow(max(cr/k,1),-1.2)*pow(0.9938,age)
    if gender == 'f':
        egfr *= 1.012
    
    print('CKD-EPI: ',egfr)

def Xiangya(cr,gender,age):
    egfr = 2374.78*pow(cr,-0.54753)*pow(age,-0.25011)
    if gender == 'f':
        egfr *= 0.8526126
    
    print('eGFR-CN: ',egfr)

def CG(cr,gender,age,weight,bsa):
    if gender == 'f':
        egfr = 1.73*(140-age)*weight/(85*cr*bsa)
    else:
        egfr = 1.73*(140-age)*weight/(72*cr*bsa)
    
    print('CG: ',egfr)

def MDRD_CN(cr,gender,age):
    egfr = 175*pow(cr,-1.234)*pow(age,-0.179)
    if gender == 'f':
        egfr *= 0.79
    
    print('MDRD-CN: ',egfr)

CKD_EPI(cr,gender,age)
Xiangya(cr_original,gender,age)
CG(cr,gender,age,weight)
MDRD_CN(cr,gender,age)
