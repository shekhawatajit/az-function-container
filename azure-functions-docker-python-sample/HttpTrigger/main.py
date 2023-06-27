import logging
import pyping
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        r = pyping.ping('google.com')
        if r.ret_code == 0:
            return func.HttpResponse(f"Success with {r.ret_code}. IP address if {r.destination_ip}")
        else:
            return func.HttpResponse(f"Failed with {r.ret_code}.")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )