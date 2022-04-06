from fastapi import FastAPI, Request
from smart import *
app = FastAPI()

 

@app.get("/")
def home(request: Request):
    return {"hello"}
@app.post("/gr")
def gr(request: dict):


        evaluator = CannyEval()
        input_json = request 
        report = evaluator.report_card(data_json=input_json)
        print(report)
        
        
        return report
#{"1":["Disaster Management is very crucial after what has happened on 21st October 1996.", [["Disaster Management is very important after what has happened on 21st October 1996."], ["Disaster Management is very crucial after what has happened on 22nd October 1996."]]], 
#"2":["Hitler is a very cruel person. Hitler has tortured many people in Germany.", [["Gandhi is a very cruel person. Gandhi has tortured many people in Germany"], ["Gandhi is a very cruel person. Gandhi has tortured many people in India"] ] ]}

#
''''
from fastapi import FastAPI, Request
 
app = FastAPI()

 

@app.get("/")
def home(request: Request):
    return {"hello"}
@app.get("/gr")
def gr(request: Request):

    return {"a":1}

'''