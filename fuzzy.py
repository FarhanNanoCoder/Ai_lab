
def getMembershipTemperature(temp):
    degree={}

    if temp<0 or temp>58:
        degree["c"]=0
        degree["w"]=0
        degree["h"]=0
    elif temp>=0 and temp<=12:
        degree["c"]=1
        degree["w"]=0
        degree["h"]=0
    elif temp>12 and temp<20:
        degree["c"]=float((20-temp)*(1.0/(20-12)))
        degree["w"]=float((temp-12)*(1.0/(20-12)))
        degree["h"]=0
    elif temp>=20 and temp<=38:
        degree["c"]=0
        degree["w"]=1
        degree["h"]=0
    elif temp>38 and temp<48:
        degree["c"]=0
        degree["w"]=float((48-temp)*(1.0/(48-38)))
        degree["h"]=float((temp-38)*(1.0/(48-38)))
    elif temp>=48 and temp<=58:
        degree["c"]=0
        degree["w"]=0
        degree["h"]=1   
    return degree


def getmembershipHumidity(hum):
    degree={}
    if hum<0 or hum>100:
        degree["l"]=0
        degree["h"]=0
    elif hum>=0 and hum<=40:
        degree["l"]=1
        degree["h"]=0
    elif hum>40 and hum<60:
        degree["l"]=float((60-hum)*(1.0/(60-40)))
        degree["h"]=float((hum-40)*(1.0/(60-40)))
    elif hum>=60 and hum<=100:
        degree["l"]=0
        degree["h"]=1
    
    return degree

def ruleEvaluationAssessment(temp,hum):
    high = max(temp["c"],hum["h"])
    low = max(temp["h"],min(temp["w"],hum["h"]))
    moderate = min(temp["w"],hum["l"])
    return high,moderate,low

def defzzificationAssestment(high,moderate,low):
    x=0
    y=0
    for i in range(15,31):
        if i<=20:
            x=x+i*low
            y=y+low
        elif i<=25:
            x=x+i*moderate
            y=y+moderate
        elif i<=30:
            x=x+i*high
            y=y+high

    return x/y







s = input("Enter temperature and humidity: ")
temp, hum = s.split()
temp = int(temp)
hum = int(hum)


tempDegree = getMembershipTemperature(temp)
humDegree = getmembershipHumidity(hum)

print("Temperature: ",tempDegree)
print("Humidity: ",humDegree)

high,moderate,low = ruleEvaluationAssessment(tempDegree,humDegree)

print("High: ",high)
print("Moderate: ",moderate)
print("Low: ",low)

print("Defuzzification: ",defzzificationAssestment(high,moderate,low))
