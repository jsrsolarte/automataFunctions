import json
import logging

import azure.functions as func
from tabulate import tabulate
from Utils.validations import validate_automata

from services.automata_service import agrupar_semejantes, eliminar_extraños, get_automata, get_dataFrame_from_automata


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    automata = json.loads(req.get_body())

    v = validate_automata(automata)
    if not v["status"]:
        return func.HttpResponse(v["message"], status_code=400)

    if automata['type'] == 1:
        return func.HttpResponse("Only support 'automata deterministico'", status_code=400)

    df = get_dataFrame_from_automata(automata)
    logging.info(tabulate(df, headers='keys', tablefmt='psql'))

    df = eliminar_extraños(df)

    df = agrupar_semejantes(df)

    logging.info(tabulate(df, headers='keys', tablefmt='psql'))

    return get_automata(df).to_JSON()










