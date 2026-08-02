import threading, time

data = None

def get_input():
    global data 
    data = input("Enter data: ")

threading.Thread(target=get_input, daemon=True).start()

start = time.monotonic() 
print(" start :", start)
timeout = 30

while True:

    if data:
        print("Data Found:", data)
        break

    if time.monotonic() - start >= timeout:
        print("time.monotonic() - start :", time.monotonic() - start)
        print("Timeout")
        break

    print("Retrying...")
    time.sleep(1)


# Each line explains the purpose of the code in Telugu language. The comments are detailed and provide context for each part of the code.
"""
# import threading 
threading built-in module ని import చేస్తున్నాం, threading module యొక్క పని ఏమిటంటే, 
ఒకే programలో ఒకటి కంటే ఎక్కువ పనులను ఒకేసారి run చేసే సౌకర్యాన్ని ఇవ్వడం. 
సాధారణంగా Python program ఒక పని పూర్తయ్యాక ఇంకో పని చేస్తుంది. కానీ ఈ programలో user input కోసం wait చేస్తూనే, 
backgroundలో retry కూడా జరగాలి. ఈ రెండు పనులు parallelగా జరగాలంటే threading module అవసరం అవుతుంది. 
అందుకే program మొదట ఈ moduleని import చేసుకుంటుంది.
# import time
time built-in moduleని import చేస్తున్నాం, time module యొక్క పని ఏమిటంటే, programలో time related operations చేయడం. 
ఈ programలో timeout కోసం time moduleని ఉపయోగిస్తున్నాం, ఉదాహరణకు current time తీసుకోవడం, కొంతసేపు wait చేయించడం, 
elapsed time measure చేయడం వంటి పనులు ఇందులో ఉంటాయి. మన programలో timeoutని calculate చేయడానికి, 
అలాగే ప్రతి retry మధ్య 1 second gap ఇవ్వడానికి ఈ moduleని ఉపయోగిస్తున్నాం.


# data = None
ఈ lineలో data అనే global variableని create చేస్తున్నాం. None అనేది Pythonలో ఒక built-in constant. 
దీని అర్థం "ప్రస్తుతం ఎలాంటి value లేదు". Program start అయినప్పుడు user ఇంకా input ఇవ్వలేదు. 
కాబట్టి dataలో ఏ information లేదు అని Pythonకి చెప్పడానికి None assign చేస్తున్నాం. ఇది function బయట declare చేసినందువల్ల, 
ఈ variableని programలోని అన్ని functions access చేయగలవు.

# def get_input():
ఈ function యొక్క ఒక్క responsibility ఏమిటంటే, user దగ్గర నుండి input తీసుకుని, 
ఆ valueని data variableలో store చేయడం. Programలో inputకి సంబంధించిన మొత్తం logic ఈ functionలో ఉంటుంది.
# global data
global keywordని ఉపయోగించడం వల్ల, Pythonకి చెప్పడం ఏమిటంటే, ఈ functionలో data variableని local variableగా treat చేయకుండా,
programలో declare చేసిన global data variableని access చేయడం. Without global keyword, Python local variable create చేస్తుంది, 
మరియు programలో declare చేసిన global variableని access చేయదు. (ఈ line చాలా ముఖ్యమైనది. data variable ఇప్పటికే function 
బయట globalగా ఉంది. కానీ functionలో data = ... అని assignment చేస్తే, Python defaultగా కొత్త local variable create చేస్తుంది. 
అది బయట ఉన్న dataని మార్చదు. అందుకే global keyword ఉపయోగించి, "నేను functionలో కొత్త variable create చేయడం లేదు. 
బయట ఉన్న global variableనే update చేస్తున్నాను" అని Pythonకి explicitly చెబుతున్నాం. global అనేది Python యొక్క built-in keyword, 
functionకి special instruction ఇస్తుంది.)

# data = input("Enter data: ")

# threading.Thread(target=get_input, daemon=True).start()
Thread అనేది threading moduleలో ఉన్న ఒక class.ఇక్కడ మనం ఒక కొత్త thread objectని create చేస్తున్నాం. 
ఈ thread main programతో పాటు ఇంకో independent execution pathని create చేస్తుంది.
అంటే programలో ఇంకో workerని hire చేసినట్లే.

target అనేది Thread class constructor (__init__) లో predefined parameter name. ఈ parameter ద్వారా కొత్త thread ఏ functionని 
execute చేయాలో చెబుతున్నాం. 
ఇక్కడ get_input functionని pass చేస్తున్నాం. గమనించండి, brackets () పెట్టలేదు. ఎందుకంటే ఇప్పుడే function call చేయడం కాదు. 
కేవలం futureలో thread start అయినప్పుడు execute చేయాల్సిన function referenceని ఇస్తున్నాం.

daemon అనేది Thread classలో ఉన్న ఒక predefined property/parameter. దీని value True అయితే, main program ముగిసిన వెంటనే 
ఈ thread కూడా automatically stop అవుతుంది. అంటే ఈ thread main threadకి helperలా behave చేస్తుంది. 
Main program complete అయిన తర్వాత background thread unnecessaryగా continue కాకుండా cleanగా terminate అవ్వడానికి 
ఈ option ఉపయోగపడుతుంది.

start() అనేది Thread class యొక్క method. Thread object create చేసినంత మాత్రాన అది run అవదు. 
start() method call చేసిన తర్వాతే operating systemకి "ఈ threadని execute చేయి" అని signal వెళ్తుంది. 
ఈ moment నుంచే get_input() function backgroundలో run అవడం ప్రారంభిస్తుంది.

# start = time.monotonic()
monotonic() అనేది time moduleలో ఉన్న built-in function. దీని ప్రత్యేకత ఏమిటంటే, ఇది elapsed time measure చేయడానికి మాత్రమే 
design చేయబడింది. System clock change అయినా, user time change చేసినా, daylight saving వచ్చినా దీని value backwardకి వెళ్లదు. 
అందుకే timeout calculationsకి monotonic() safest choice. ఈ lineలో program start అయిన ఖచ్చితమైన starting pointని store చేస్తున్నాం.

# timeout = 30
ఈ lineలో program maximum ఎంతసేపు wait చేయాలో define చేస్తున్నాం. అంటే 30 seconds దాటిన తర్వాత కూడా data రాకపోతే 
program retry చేయడం ఆపి timeout ఇవ్వాలి. Hardcoded valueని variableలో పెట్టడం వల్ల futureలో 30ని 60 లేదా 120గా మార్చడం 
చాలా easy అవుతుంది.


# while True:
while అనేది Python యొక్క loop statement. True అంటే condition ఎప్పుడూ true. 
కాబట్టి ఈ loop theoretically infiniteగా run అవుతుంది. కానీ practicalగా ఇది forever run కాదు, 
ఎందుకంటే లోపల break statements ఉన్నాయి. Data వచ్చినప్పుడు లేదా timeout అయినప్పుడు break ద్వారా loopని stop చేస్తున్నాం. 
Data ఎప్పుడు వస్తుందో ముందుగా తెలియదు కాబట్టి infinite loop best choice.

#if data:
#print("Data Found:", data)
#break

#if time.monotonic() - start >= timeout:
ఈ lineలో timeout check చేస్తున్నాం. Current time నుండి program start అయిన timeని తీసి,
timeout value (30 seconds)తో compare చేస్తున్నాం. Current time - start time >= timeout అంటే, 
program 30 seconds wait చేసినా data రాలేదు అని అర్థం.
time.monotonic() - start >= timeout condition true అయితే, print statement ద్వారా "Timeout" 
message display చేసి, break statement ద్వారా loop exit అవుతుంది.
(ఇది మొత్తం programలో heart of timeout logic. time.monotonic() current elapsed timerని ఇస్తుంది. 
start అనేది program ప్రారంభమైన సమయం. రెండింటిని subtract చేస్తే "ఇప్పటివరకు ఎంతసేపు గడిచింది?" అనేది వస్తుంది. 
ఆ elapsed time 30 secondsని cross చేసిందా లేదా అని compare చేస్తున్నాం. Cross అయితే timeout condition true అవుతుంది.)
#print("Timeout")
#break

#print("Retrying...")
#time.sleep(1)
time.sleep(1) అనేది time moduleలో ఉన్న built-in function. దీని పని ఏమిటంటే, programని 1 secondకి suspend చేయడం.
అంటే program 1 second wait అవుతుంది. ఈ line run అయిన తర్వాత program 1 second wait అవుతుంది. 
Retry message display చేసిన తర్వాత program 1 second wait అవుతుంది.
(sleep() అనేది time moduleలో ఉన్న method/function. దీని పని program executionని temporaryగా pause చేయడం. 
ఇక్కడ 1 second pause ఇస్తున్నాం. Pause ఇవ్వకపోతే loop ఒక secondలో లక్షల సార్లు run అవుతుంది, CPU usage చాలా ఎక్కువ అవుతుంది. 
అందుకే ప్రతి retry మధ్య controlled gap ఇస్తున్నాం. Real-world polling systemsలో కూడా ఇదే technique ఉపయోగిస్తారు.)
"""