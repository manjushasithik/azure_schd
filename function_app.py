import logging
import azure.functions as func
import requests

app = func.FunctionApp()


@app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timerrrrrrrrrrrrrrrrrr trigger function executed.')
    
@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def cbm_trigger_1(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')
    
    response= requests.post("https://detention-api.azurewebsites.net/test")

    if response.status_code == 200:
        # Request was successful
        logging.info('HTTP GET request to the URL was successful.')
        # You can access the content of the response using response.text, response.content, etc.
    else:
        # Request failed
        logging.error('HTTP GET request to the URL failed with status code: %d', response.status_code)

    logging.info('Pythonnnnnnnnnnnn timer trigger function executed.')
    

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def cbm_trigger(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def cbm_trigger_10(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger111(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
