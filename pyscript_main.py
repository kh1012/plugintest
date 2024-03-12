'''
██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗██║████╗  ██║
██████╔╝ ╚████╔╝     ██╔████╔██║███████║██║██╔██╗ ██║
██╔═══╝   ╚██╔╝      ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██║        ██║       ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═╝        ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

@description This is a sample code for python script.
'''

# this is sample code for python script.
# if you want to use other python files, import here and functions export your javascript code.
import json
import math
from pyscript_engineers_web import set_g_values, get_g_values, requests_json
from pyscript_engineers_web import MidasAPI, Product
def HelloWorld():
	return (f'Hello World! this message is from def HelloWorld of PythonCode.py')

def ApiGet():
	values = json.loads(get_g_values())
	base_uri = values["g_base_uri"]
	res = requests_json.get(url=f'https://{base_uri}/health', headers={
		'Content-Type': 'application/json'
	})
	return json.dumps(res)

# Basic CRUD Sample
def py_db_create(item_name, items):
	civil = MidasAPI(Product.CIVIL, "KR")
	return json.dumps(civil.db_create(item_name, json.loads(items)))

def py_db_create_item(item_name, item_id, item):
	civil = MidasAPI(Product.CIVIL, "KR")
	return json.dumps(civil.db_create_item(item_name, item_id, json.loads(item)))

def py_db_read(item_name):
	civil = MidasAPI(Product.CIVIL, "KR")
	return json.dumps(civil.db_read(item_name))

def py_db_read_item(item_name, item_id):
	civil = MidasAPI(Product.CIVIL, "KR")
	return json.dumps(civil.db_read_item(item_name, item_id))

def py_db_update(item_name, items):
	civil = MidasAPI(Product.CIVIL, "KR")
	return json.dumps(civil.db_update(item_name, json.loads(items)))

def py_db_update_item(item_name, item_id, item):
	civil = MidasAPI(Product.CIVIL, "KR")
	return json.dumps(civil.db_update_item(item_name, item_id, json.loads(item)))

def py_db_delete(item_name, item_id):
	civil = MidasAPI(Product.CIVIL, "KR")
	return json.dumps(civil.db_delete(item_name, item_id))

'''

██╗    ██╗██████╗ ██╗████████╗███████╗    ██╗  ██╗███████╗██████╗ ███████╗
██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝    ██║  ██║██╔════╝██╔══██╗██╔════╝
██║ █╗ ██║██████╔╝██║   ██║   █████╗      ███████║█████╗  ██████╔╝█████╗  
██║███╗██║██╔══██╗██║   ██║   ██╔══╝      ██╔══██║██╔══╝  ██╔══██╗██╔══╝  
╚███╔███╔╝██║  ██║██║   ██║   ███████╗    ██║  ██║███████╗██║  ██║███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                                          
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ write a main logic here ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
'''

def CalFoundationCoordinates(Width, Length):
	FoundationCoordinates = []
	FoundationCoordinates.append([0, 0])
	FoundationCoordinates.append([0, Width])
	FoundationCoordinates.append([Length, Width])
	FoundationCoordinates.append([Length, 0])
	FoundationCoordinates.append([0, 0])
	return json.dumps(FoundationCoordinates)

def extract_numbers(input_string):
	parts = input_string.replace(',', ' ').split()
	
	result = []
	for part in parts:
		if '@' in part:
			sub_parts = part.split('@')
			try:
				num1 = int(sub_parts[0])
				num2 = float(sub_parts[1])
				result += [num2] * num1
			except:
				pass
		else:
			try:
				num = float(part)
				result.append(num)
			except:
				pass
	return json.dumps(result)

## 각 pile의 좌표 계산
def CalPileCoordinates(PileTableData, PileLocationData):
    
    ## Width는 Y축, Length는 X축
    ## PileDia는 Pile의 지름
    ## MajorRefValue는 X축의 기준점 (1일 경우 원점, 2일 경우 Length)
    ## MinorRefValue는 Y축의 기준점 (1일 경우 원점, 2일 경우 Width)
    
	pileTableData = json.loads(PileTableData)
	pileLocationData = json.loads(PileLocationData)
	Coordinates = []
	for i in range(len(pileLocationData)):
		GroupCoordinates = []
		for j in range(len(pileLocationData[i])):
			Diameter = float(pileTableData[i]['concreteDiameter'])/1000
			EachPileCoordinates = []
			for angle in range(0, 360, 30):
				## Dia 단위가 mm
				x = float(pileLocationData[i][j][0]) + Diameter/2 * math.cos(math.radians(angle))
				y = float(pileLocationData[i][j][1]) + Diameter/2 * math.sin(math.radians(angle))
				EachPileCoordinates.append([x, y])
			EachPileCoordinates.append(EachPileCoordinates[0])
			GroupCoordinates.append(EachPileCoordinates)
		Coordinates.append(GroupCoordinates)
	return json.dumps(Coordinates)
			

## 각 파일의 중심 좌표 계산 (각 파일 타입 별로 받음)
def CalPileCenterCoordinates(PileData, FoundationWidth, SideLength):

	pileData = json.loads(PileData)
	foundationWidth = json.loads(FoundationWidth)
	sideLength = json.loads(SideLength)
	majorSpace = json.loads(extract_numbers(pileData['majorSpace']))
	
	CenterX = []
	if pileData['majorRefValue'] == 1:
		CenterX = [float(pileData['majorStartPoint'])]
		for i in range(len(majorSpace)):
			CenterX.append(float(CenterX[i]+float(majorSpace[i])))
	elif pileData['majorRefValue'] == 2:
		CenterX = [float(sideLength)-float(pileData['majorStartPoint'])]
		for i in range(len(majorSpace)):
			CenterX.append(float(CenterX[i]-float(majorSpace[i])))

	CenterCoordinates = []
	if pileData['minorRefValue'] == 1:
		for i in range(len(CenterX)):
			CenterCoordinates.append([CenterX[i], float(pileData['minorStartPoint'])])
	elif pileData['minorRefValue'] == 2:
		for i in range(len(CenterX)):
			CenterCoordinates.append([CenterX[i], float(foundationWidth)-float(pileData['minorStartPoint'])])
	return json.dumps(CenterCoordinates)

## 각 파일의 각도 계산
def CalPileDegree(PileData):
    
	pileData = json.loads(PileData)

	majorDegree = json.loads(extract_numbers(pileData['majorDegree']))
	minorDegree = json.loads(extract_numbers(pileData['minorDegree']))
	degree = []
	## 각 파일의 각도의 개수를 조정하는 코드 추가 필요함
	for i in range(len(majorDegree)):
		degree.append([majorDegree[i], minorDegree[i]])
	return json.dumps(degree)

## 상시, 지진시 말뚝 특성치 계산
def CalBeta(SoilData, PileTableData, Condition, SlopeEffectState):
    
	pileTableData = json.loads(PileTableData)
	soilData = json.loads(SoilData)
	
	Beta = [1 for i in range(len(pileTableData))]
	Avg_alpha_E0 = [0 for i in range(len(pileTableData))]
	Bh = [0 for i in range(len(pileTableData))]
	Kh0 = [0 for i in range(len(pileTableData))]
	Kh = [0 for i in range(len(pileTableData))]
	Alpha_HTheta = [[1 for j in range(len(SoilData))] for i in range(len(pileTableData))]
	for i in range(len(pileTableData)):
		## Area, Modulus, SecInertia, Diameter, SteelArea, CementArea, SteelModulus, CementModulus, SteelInertia, CementInertia
		Property = json.loads(CalProperties(json.dumps(pileTableData[i])))
		
		Diameter = Property[3]
		InitialBeta = 1/(float(pileTableData[i]['pileLength'])/4)
		
		Modulus = 0
		## 복합말뚝 / 보강 단면인 경우 확인 필요
		if (pileTableData[i]['pileType'] == '소일시멘트말뚝'):
			## 소일시멘트 말뚝이면 강관 modulus 사용
			Modulus = Property[6]
		else:
			Modulus = Property[1]

		## 단면이 여러개인 경우 2차단면모멘트 값 확인 필요
		SecInertia = 0
		if (pileTableData[i]['pileType'] == '소일시멘트말뚝'):
			## 소일시멘트 말뚝이면 강관 2차단면모멘트 사용
			SecInertia = Property[8]
		else:
			SecInertia = Property[2]

		tolorence = 0.000001
		
		while True:
			LayerDepth = 0
			Avg_alpha_E0[i] = 0
			for j in range(len(soilData)):
				LayerDepth += float(soilData[j]['Depth'])
				if LayerDepth < (1/InitialBeta):
					if (Condition == 'normal'):
						Avg_alpha_E0[i] += float(soilData[j]['aE0'])*float(soilData[j]['Depth'])
					elif (Condition == 'seismic'):
						Avg_alpha_E0[i] += float(soilData[j]['aE0_Seis'])*float(soilData[j]['Depth'])
				else:
					if (Condition == 'normal'):
						Avg_alpha_E0[i] += float(soilData[j]['aE0'])*((1/InitialBeta)-(LayerDepth-float(soilData[j]['Depth'])))
						break
					elif (Condition == 'seismic'):
						Avg_alpha_E0[i] += float(soilData[j]['aE0_Seis'])*((1/InitialBeta)-(LayerDepth-float(soilData[j]['Depth'])))
						break
			Avg_alpha_E0[i] = Avg_alpha_E0[i]/(1/InitialBeta)
			Bh[i] = math.sqrt(Diameter/InitialBeta)
			Kh0[i] = Avg_alpha_E0[i] / (0.3)
			Kh[i] = Kh0[i] * math.pow((Bh[i]/0.3),(-3/4))
			Beta[i] = math.pow((Kh[i]*Diameter/(4*Modulus*SecInertia)),(1/4))
			
			if abs(Beta[i]-InitialBeta) > tolorence:
				InitialBeta = Beta[i]
			elif abs(Beta[i]-InitialBeta) <= tolorence:
				break
	
	if (SlopeEffectState == True):
		for i in range(len(pileTableData)):
			Property = json.loads(CalProperties(json.dumps(pileTableData[i])))
			for j in range(len(soilData)):
				Alpha_H = float(soilData[j]['Length'])/Property[3]
				if (Alpha_H >=0 and Alpha_H < 0.5):
					Alpha_HTheta[i][j] = 0
				elif (Alpha_H >= 0.5 and Alpha_H < 10):
					Alpha_HTheta[i][j] = 0.3*math.log(Alpha_H)+0.7
				else :
					Alpha_HTheta[i][j] = 1
	result = [Beta, Avg_alpha_E0, Bh, Kh0, Kh, Alpha_HTheta]
	return json.dumps(result)

## 고유주기 산정
def CalBeta_Period(SoilData, PileTableData, SlopeEffectState):
    
	pileTableData = json.loads(PileTableData)
	soilData = json.loads(SoilData)
	
	Beta = [1 for i in range(len(pileTableData))]
	Ed = [0 for i in range(len(pileTableData))]
	Bh = [0 for i in range(len(pileTableData))]
	Kh0 = [0 for i in range(len(pileTableData))]
	Kh = [0 for i in range(len(pileTableData))]
	Alpha_HTheta = [[1 for j in range(len(SoilData))] for i in range(len(pileTableData))]
	for i in range(len(pileTableData)):
		
		Property = json.loads(CalProperties(json.dumps(pileTableData[i])))
		
		Diameter = Property[3]
		InitialBeta = 1/(float(pileTableData[i]['pileLength'])/4)
		
		Modulus = 0
		SecInertia = 0
		## 복합말뚝 / 보강 단면인 경우 확인 필요
		if (pileTableData[i]['pileType'] == '소일시멘트말뚝'):
			## 소일시멘트 말뚝이면 강관 modulus, 2차단면모멘트 사용
			Modulus = Property[6]
			SecInertia = Property[8]
		else:
			Modulus = Property[1]
			SecInertia = Property[2]

		## 단면이 여러개인 경우 2차단면모멘트 값 확인 필요



		tolorence = 0.000001
		
		while True:
			LayerDepth = 0
			Ed[i] = 0
			for j in range(len(soilData)):
				LayerDepth += float(soilData[j]['Depth'])
				if LayerDepth < (1/InitialBeta):
					Ed[i] += float(soilData[j]['ED'])*float(soilData[j]['Depth'])
				else:
					Ed[i] += float(soilData[j]['ED'])*((1/InitialBeta)-(LayerDepth-float(soilData[j]['Depth'])))
					break

			Ed[i] = Ed[i]/(1/InitialBeta)
			Bh[i] = math.sqrt(Diameter/InitialBeta)
			Kh0[i] = Ed[i] / (0.3)
			Kh[i] = Kh0[i] * math.pow((Bh[i]/0.3),(-3/4))
			Beta[i] = math.pow((Kh[i]*Diameter/(4*Modulus*SecInertia)),(1/4))
			if abs(Beta[i]-InitialBeta) > tolorence:
				InitialBeta = Beta[i]
			elif abs(Beta[i]-InitialBeta) <= tolorence:
				break
	
	if (SlopeEffectState == True):
		for i in range(len(pileTableData)):
			Property = json.loads(CalProperties(json.dumps(pileTableData[i])))
			for j in range(len(soilData)):
				Alpha_H = float(soilData[j]['Length'])/Property[3]
				if (Alpha_H >=0 and Alpha_H < 0.5):
					Alpha_HTheta[i][j] = 0
				elif (Alpha_H >= 0.5 and Alpha_H < 10):
					Alpha_HTheta[i][j] = 0.3*math.log(Alpha_H)+0.7
				else :
					Alpha_HTheta[i][j] = 1
	result = [Beta, Ed, Bh, Kh0, Kh, Alpha_HTheta]

	return json.dumps(result)

def CalKv(PileTableData):
    
	pileTableData = json.loads(PileTableData)
	Alpha1 =[0 for i in range(len(pileTableData))]
	Alpha2 =[0 for i in range(len(pileTableData))]
	Kv = [0 for i in range(len(pileTableData))]

	for i in range(len(pileTableData)):
		if (pileTableData[i]['constructionMethod'] == '타격말뚝(타격 공법)'):
			Alpha1[i] = 0.014
			Alpha2[i] = 0.72
		elif (pileTableData[i]['constructionMethod'] == '타격말뚝(바이브러 해머공법)'):
			Alpha1[i] = 0.017
			Alpha2[i] = -0.014
		elif (pileTableData[i]['constructionMethod'] == '현장타설말뚝'):
			Alpha1[i] = 0.031
			Alpha2[i] = -0.15
		elif (pileTableData[i]['constructionMethod'] == '중굴착 말뚝'):
			Alpha1[i] = 0.01
			Alpha2[i] = 0.36
		elif (pileTableData[i]['constructionMethod'] == 'preboring 말뚝'):
			Alpha1[i] = 0.013
			Alpha2[i] = 0.53
		elif (pileTableData[i]['constructionMethod'] == '강관 소일시멘트 말뚝'):
			Alpha1[i] = 0.040
			Alpha2[i] = 0.15
		elif (pileTableData[i]['constructionMethod'] == '회전말뚝'):
			Alpha1[i] = 0.013
			Alpha2[i] = 0.54
			
		## Area, Modulus, SecInertia, Diameter, SteelArea, CementArea, SteelModulus, CementModulus, SteelInertia, CementInertia	
		Property = json.loads(CalProperties(json.dumps(pileTableData[i])))

		if (pileTableData[i]['pileType'] == '소일시멘트말뚝'):
			Asp = Property[4]
			Esp = Property[6]
			Asc = Property[5]
			Esc = Property[7]
			Length = float(pileTableData[i]['pileLength'])
			Diameter = Property[3]
			Alpha = Alpha1[i] * (Length/Diameter) + Alpha2[i]
			Kv[i] = Alpha*(Asp*Esp + Asc*Esc)/Length
		else:
			Ap = Property[0]
			Ep = Property[1]
			Length = float(pileTableData[i]['pileLength'])
			Diameter = Property[3]
			Alpha = Alpha1[i] * (Length/Diameter) + Alpha2[i]
			Kv[i] = Alpha*Ap*Ep/Length

	result = [Kv, Alpha1, Alpha2]
	return json.dumps(result)

def CalKValue(PileTableData, GroundLevel, TopLevel, SoilData, Condition, SlopeEffectState):
    
	pileTableData = json.loads(PileTableData)

	h = float(TopLevel) - float(GroundLevel)
	##print ('h : ', h)
	CalBetaResult = json.loads(CalBeta(SoilData, PileTableData, Condition, SlopeEffectState))
	Kvalue = [[0,0,0,0] for i in range(len(pileTableData))]
	for i in range(len(pileTableData)):
		
		## Area, Modulus, SecInertia, Diameter, SteelArea, CementArea, SteelModulus, CementModulus, SteelInertia, CementInertia
		Property = json.loads(CalProperties(json.dumps(pileTableData[i])))

		if (pileTableData[i]['pileType'] == '소일시멘트말뚝'):
			## 소일시멘트 말뚝이면 강관 modulus, 2차단면모멘트 사용
			Modulus = Property[6]
			SecInertia = Property[8]
		else:
			Modulus = Property[1]
			SecInertia = Property[2]
   
		Beta = float(CalBetaResult[0][i])

		##print ('Modulus : '	, Modulus)
		##print ('SecInertia : '	, SecInertia)
		##print ('Beta : '	, Beta)
		if (pileTableData[i]['headCondition'] == '강결'):
			if (h == 0):
				Kvalue[i][0] = 4*Modulus*SecInertia*math.pow(Beta,3)
				Kvalue[i][1] = 2*Modulus*SecInertia*math.pow(Beta,2)
				Kvalue[i][2] = 2*Modulus*SecInertia*math.pow(Beta,2)
				Kvalue[i][3] = 2*Modulus*SecInertia*math.pow(Beta,1)
			else:
				Kvalue[i][0] = (12*Modulus*SecInertia*math.pow(Beta,3))/(math.pow(1+Beta*h,3)+2)
				Kvalue[i][1] = Kvalue[i][0]*(h+1/Beta)/2
				Kvalue[i][2] = Kvalue[i][0]*(h+1/Beta)/2
				Kvalue[i][3] = (4*Modulus*SecInertia*Beta)/(1+Beta*h)*(math.pow(1+Beta*h,3)+0.5)/(math.pow(1+Beta*h,3)+2)
		
		elif (pileTableData[i]['headCondition'] == '힌지'):
			if (h == 0):
				Kvalue[i][0] = 2*Modulus*SecInertia*math.pow(Beta,3)
				Kvalue[i][1] = 0
				Kvalue[i][2] = 0
				Kvalue[i][3] = 0
			else:
				Kvalue[i][0] = (3*Modulus*SecInertia*math.pow(Beta,3))/(math.pow(1+Beta*h,3)+0.5)
				Kvalue[i][1] = 0
				Kvalue[i][2] = 0
				Kvalue[i][3] = 0
	
	return json.dumps(Kvalue)

def CalKValue_Period(PileTableData, GroundLevel, TopLevel, SoilData, SlopeEffectState):
    
	pileTableData = json.loads(PileTableData)

	h = float(TopLevel) - float(GroundLevel)
	CalBetaResult = json.loads(CalBeta_Period(SoilData, PileTableData, SlopeEffectState))
	
	Kvalue = [[0,0,0,0] for i in range(len(pileTableData))]
	for i in range(len(pileTableData)):
		## Area, Modulus, SecInertia, Diameter, SteelArea, CementArea, SteelModulus, CementModulus, SteelInertia, CementInertia
		Property = json.loads(CalProperties(json.dumps(pileTableData[i])))

		if (pileTableData[i]['pileType'] == '소일시멘트말뚝'):
			## 소일시멘트 말뚝이면 강관 modulus, 2차단면모멘트 사용
			Modulus = Property[6]
			SecInertia = Property[8]
		else:
			Modulus = Property[1]
			SecInertia = Property[2]
   
		Beta = float(CalBetaResult[0][i])
		if (pileTableData[i]['headCondition'] == '강결'):
			if (h == 0):
				Kvalue[i][0] = 4*Modulus*SecInertia*math.pow(Beta,3)
				Kvalue[i][1] = 2*Modulus*SecInertia*math.pow(Beta,2)
				Kvalue[i][2] = 2*Modulus*SecInertia*math.pow(Beta,2)
				Kvalue[i][3] = 2*Modulus*SecInertia*math.pow(Beta,2)
			else:
				Kvalue[i][0] = (12*Modulus*SecInertia*math.pow(Beta,3))/(math.pow(1+Beta*h,3)+2)
				Kvalue[i][1] = Kvalue[i][0]*(h+1/Beta)/2
				Kvalue[i][2] = Kvalue[i][0]*(h+1/Beta)/2
				Kvalue[i][3] = (4*Modulus*SecInertia*Beta)/(1+Beta*h)*(math.pow(1+Beta*h,3)+0.5)/(math.pow(1+Beta*h,3)+2)
		
		elif (pileTableData[i]['headCondition'] == '힌지'):
			if (h == 0):
				Kvalue[i][0] = 2*Modulus*SecInertia*math.pow(Beta,3)
				Kvalue[i][1] = 0
				Kvalue[i][2] = 0
				Kvalue[i][3] = 0
			else:
				Kvalue[i][0] = (3*Modulus*SecInertia*math.pow(Beta,3))/(math.pow(1+Beta*h,3)+0.5)
				Kvalue[i][1] = 0
				Kvalue[i][2] = 0
				Kvalue[i][3] = 0
	
	return json.dumps(Kvalue)

def CalProperties(PileData):

	pileData = json.loads(PileData)
	Area = 0
	Modulus = 0
	SecInertia = 0
	Diameter = 0
	SteelArea = 0
	CementArea = 0
	SteelModulus = 0
	CementModulus = 0
	SteelInertia = 0
	CementInertia = 0
	if (pileData['pileType'] == '현장타설말뚝'):
		Area = math.pi/4 * (float(pileData['concreteDiameter'])/1000)**2
		Modulus = float(pileData['concreteModulus'])
		SecInertia = (math.pi * (float(pileData['concreteDiameter'])/1000)**4)/64
		Diameter = float(pileData['concreteDiameter'])/1000
	elif (pileData['pileType'] == 'PHC말뚝'):
		Area = (float(pileData['concreteDiameter'])/1000-float(pileData['concreteThickness'])/1000) * math.pi * (float(pileData['concreteThickness'])/1000) + (float(pileData['steelModulus'])/float(pileData['concreteModulus'])-1)*float(pileData['steelDiameter'])/1000000
		Modulus = float(pileData['concreteModulus'])
		Ic = math.pi/64 * (math.pow(float(pileData['concreteDiameter'])/1000,4)-math.pow((float(pileData['concreteDiameter'])/1000-2*float(pileData['concreteThickness'])/1000),4))
		Is = ((float(pileData['steelModulus']))/(float(pileData['concreteModulus']))-1)*(1/2)*float(pileData['steelDiameter'])/1000000*math.pow(float(pileData['steelCorThickness'])/1000,2)
		SecInertia = Ic + Is
		Diameter = float(pileData['concreteDiameter'])/1000
	elif (pileData['pileType']=='SC말뚝'):
		Area1 = math.pi/4 * (math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['steelCorThickness'])/1000,2) - math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['concreteThickness'])/1000,2))
		Area2 = math.pi/4 * (float(pileData['steelModulus'])/float(pileData['concreteModulus'])-1)*(math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['steelCorThickness'])/1000,2)-math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['steelThickness'])/1000,2))
		Area = Area1 + Area2
		Modulus = float(pileData['concreteModulus'])
		Ic = math.pi/64*(math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['steelCorThickness'])/1000,4)-math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['concreteThickness'])/1000,4))
		Is = math.pi/64*(float(pileData['steelModulus'])/float(pileData['concreteModulus'])-1)*(math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['steelCorThickness'])/1000,4)-math.pow(float(pileData['concreteDiameter'])/1000-2*float(pileData['steelThickness'])/1000,4))
		SecInertia = Ic + Is
		Diameter = float(pileData['concreteDiameter'])/1000-float(pileData['steelCorThickness'])/1000
	elif (pileData['pileType']=='강관말뚝'):
		Area = math.pi/4 * (math.pow(float(pileData['steelDiameter'])/1000 - 2*float(pileData['steelCorThickness'])/1000,2)-math.pow(float(pileData['steelDiameter'])/1000-2*float(pileData['steelThickness'])/1000,2))
		Modulus = float(pileData['steelModulus'])
		SecInertia = math.pi/64 * (math.pow(float(pileData['steelDiameter'])/1000 - 2*float(pileData['steelCorThickness'])/1000,4)-math.pow(float(pileData['steelDiameter'])/1000-2*float(pileData['steelThickness'])/1000,4))
		Diameter = float(pileData['steelDiameter'])/1000-float(pileData['steelCorThickness'])/1000
	elif (pileData['pileType']=='소일시멘트말뚝'):
		SteelArea = math.pi/4 * (math.pow(float(pileData['steelDiameter'])/1000-2*float(pileData['steelCorThickness'])/1000,2)-math.pow(float(pileData['steelDiameter'])/1000-2*float(pileData['steelThickness'])/1000,2))
		SteelModulus = float(pileData['steelModulus'])
		SteelInertia = math.pi/64 * (math.pow(float(pileData['steelDiameter'])/1000-2*float(pileData['steelCorThickness'])/1000,4)-math.pow(float(pileData['steelDiameter'])/1000-2*float(pileData['steelThickness'])/1000,4))
		CementArea = math.pi/4*math.pow(float(pileData['concreteDiameter'])/1000,2) - SteelArea
		CementModulus = float(pileData['concreteModulus'])
		CementInertia = math.pi/64 * math.pow(float(pileData['concreteDiameter'])/1000,4) - SteelInertia
		Diameter = float(pileData['concreteDiameter'])/1000
	result = [Area, Modulus, SecInertia, Diameter, SteelArea, CementArea, SteelModulus, CementModulus, SteelInertia, CementInertia]

	return json.dumps(result)

def CalDistFromCentriod(PileTableData, FoundationWidth, SideLength):
    
	pileTableData = json.loads(PileTableData)
	foundationWidth = json.loads(FoundationWidth)
	sideLength = json.loads(SideLength)
	TotalPileNums = 0
	CenterX = 0
	CenterY = 0
	CentroidX = 0
	CentroidY = 0
	for pileData in pileTableData:
		CenterCoordinates = json.loads(CalPileCenterCoordinates(json.dumps(pileData), json.dumps(foundationWidth), json.dumps(sideLength)))
		for i in range(len(CenterCoordinates)):
			CenterX = CenterX + float(CenterCoordinates[i][0])
			CenterY = CenterY + float(CenterCoordinates[i][1])
		TotalPileNums += len(CenterCoordinates)
	CentroidX = CenterX / TotalPileNums
	CentroidY = CenterY / TotalPileNums
	DistFromCentroid = []
	for pileData in pileTableData:
		CenterCoordinates = json.loads(CalPileCenterCoordinates(json.dumps(pileData), json.dumps(foundationWidth), json.dumps(sideLength)))
		for i in range(len(CenterCoordinates)):
			CenterCoordinates[i][0] = CenterCoordinates[i][0] - CentroidX
			CenterCoordinates[i][1] = CenterCoordinates[i][1] - CentroidY
		
		DistFromCentroid.append(CenterCoordinates)
	##print (DistFromCentroid)
	return json.dumps(DistFromCentroid)
    
def CalMatrix(PileTableData, FoundationWidth, SideLength, GroundLevel, TopLevel, SoilData, SlopeEffectState, ResultType, Direction):
	pileTableData = json.loads(PileTableData)
	foundationWidth = json.loads(FoundationWidth)
	sideLength = json.loads(SideLength)
	soilData = json.loads(SoilData)
	disFromCentroid = json.loads(CalDistFromCentriod(json.dumps(pileTableData), json.dumps(foundationWidth), json.dumps(sideLength)))
	PileDegree = []
	for pileData in pileTableData:
		PileDegree.append(json.loads(CalPileDegree(json.dumps(pileData))))

	## PileDegree 안의 모든 값을 radian으로 변환
	for i in range(len(PileDegree)):
		for j in range(len(PileDegree[i])):
			PileDegree[i][j][0] = math.radians(PileDegree[i][j][0])
			PileDegree[i][j][1] = math.radians(PileDegree[i][j][1])
   
	##print (PileDegree)

	CalKvResult = json.loads(CalKv(json.dumps(pileTableData)))
	Kv = CalKvResult[0]
	##print (Kv)
	if (ResultType == 'normal'):
		KValue = json.loads(CalKValue(json.dumps(pileTableData), GroundLevel, TopLevel, json.dumps(soilData), 'normal', SlopeEffectState))
	elif (ResultType == 'seismic'):
		KValue = json.loads(CalKValue(json.dumps(pileTableData), GroundLevel, TopLevel, json.dumps(soilData), 'seismic', SlopeEffectState))
	elif (ResultType == 'period'):
		KValue = json.loads(CalKValue_Period(json.dumps(pileTableData), GroundLevel, TopLevel, json.dumps(soilData), SlopeEffectState))
	Axx = 0 
	Axy = 0 
	Axa = 0 
	Ayy = 0
	Aya = 0
	Aaa = 0
	if (Direction == 'X'):
		for i in range(len(Kv)):
			for j in range(len(PileDegree[i])):
				Axx = Axx + float(KValue[i][0])*math.pow(math.cos(PileDegree[i][j][0]),2) + float(Kv[i])*math.pow(math.sin(PileDegree[i][j][0]),2)
				Axy = Axy + (float(Kv[i])-float(KValue[i][0]))*math.sin(PileDegree[i][j][0])*math.cos(PileDegree[i][j][0])
				Axa = Axa + (float(Kv[i])-float(KValue[i][0]))*float(disFromCentroid[i][j][0])*math.sin(PileDegree[i][j][0])*math.cos(PileDegree[i][j][0])-float(KValue[i][1])*math.cos(PileDegree[i][j][0])
				Ayy = Ayy + float(Kv[i])*math.pow(math.cos(PileDegree[i][j][0]),2) + float(KValue[i][0])*math.pow(math.sin(PileDegree[i][j][0]),2)
				Aya = Aya + (float(Kv[i])*math.pow(math.cos(PileDegree[i][j][0]),2) + float(KValue[i][0])*math.pow(math.sin(PileDegree[i][j][0]),2))*float(disFromCentroid[i][j][0])+float(KValue[i][1])*math.sin(PileDegree[i][j][0])
				Aaa1 = (float(Kv[i])*math.pow(math.cos(PileDegree[i][j][0]),2) + float(KValue[i][0])*math.pow(math.sin(PileDegree[i][j][0]),2))*math.pow(float(disFromCentroid[i][j][0]),2)
				Aaa2 = (float(KValue[i][1])+float(KValue[i][2]))*float(disFromCentroid[i][j][0])*math.sin(PileDegree[i][j][0])+float(KValue[i][3])
				Aaa = Aaa + Aaa1 + Aaa2
	
	elif (Direction == 'Z'):
		for i in range(len(Kv)):
			for j in range(len(PileDegree[i])):
				Axx = Axx + float(KValue[i][0])*math.pow(math.cos(PileDegree[i][j][1]),2) + float(Kv[i])*math.pow(math.sin(PileDegree[i][j][1]),2)
				Axy = Axy + (float(Kv[i])-float(KValue[i][0]))*math.sin(PileDegree[i][j][1])*math.cos(PileDegree[i][j][1])
				Axa = Axa + (float(Kv[i])-float(KValue[i][0]))*float(disFromCentroid[i][j][1])*math.sin(PileDegree[i][j][1])*math.cos(PileDegree[i][j][1])-float(KValue[i][1])*math.cos(PileDegree[i][j][1])
				Ayy = Ayy + float(Kv[i])*math.pow(math.cos(PileDegree[i][j][1]),2) + float(KValue[i][0])*math.pow(math.sin(PileDegree[i][j][1]),2)
				Aya = Aya + (float(Kv[i])*math.pow(math.cos(PileDegree[i][j][1]),2) + float(KValue[i][0])*math.pow(math.sin(PileDegree[i][j][1]),2))*float(disFromCentroid[i][j][1])+float(KValue[i][1])*math.sin(PileDegree[i][j][1])
				Aaa1 = (float(Kv[i])*math.pow(math.cos(PileDegree[i][j][1]),2) + float(KValue[i][0])*math.pow(math.sin(PileDegree[i][j][1]),2))*math.pow(float(disFromCentroid[i][j][1]),2)
				Aaa2 = (float(KValue[i][1])+float(KValue[i][2]))*float(disFromCentroid[i][j][1])*math.sin(PileDegree[i][j][1])+float(KValue[i][3])
				Aaa = Aaa + Aaa1 + Aaa2
	##print (Axx, Axy, Axa, Ayy, Aya, Aaa)
	result = [Axx, Axy, Axa, Ayy, Aya, Aaa]
	return json.dumps(result)