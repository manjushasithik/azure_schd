
import datetime
import logging
import azure.functions as func
import requests
app = func.FunctionApp()

@app.function_name(name="mytimer")
@app.schedule(schedule="* * * * * *", 
              arg_name="mytimer",
              run_on_startup=True) 
def test_function(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')
    response = requests.get("https://detention-api.azurewebsites.net/test")
    
    
    
# import logging
# import azure.functions as func
# import requests
# app = func.FunctionApp()

# @app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
#               use_monitor=False) 
# def bbb(myTimer: func.TimerRequest) -> None:
#     if myTimer.past_due:
#         logging.info('The timer is past due!')
#     response = requests.get("https://detention-api.azurewebsites.net/test")
#     logging.info('Python timer trigger fwunction executed.')
