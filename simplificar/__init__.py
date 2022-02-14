import json
import logging

import azure.functions as func
from tabulate import tabulate
from comunes.services.automata_service import agrupar_semejantes, get_automata, get_dataFrame_from_automata, hacer_deterministico_eliminar_extranos

from comunes.utils.validations import validate_automata


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    automata = json.loads(req.get_body())

    v = validate_automata(automata)
    if not v["status"]:
        return func.HttpResponse(v["message"], status_code=400)

    
    df = get_dataFrame_from_automata(automata)
    logging.info("Incial:")
    logging.info(tabulate(df, headers='keys', tablefmt='psql'))

    df = hacer_deterministico_eliminar_extranos(df)
    logging.info("Det sin extraños:")
    logging.info(tabulate(df, headers='keys', tablefmt='psql'))

    df = agrupar_semejantes(df)
    logging.info("Simplificado:")
    logging.info(tabulate(df, headers='keys', tablefmt='psql'))

    return get_automata(df).to_JSON()










