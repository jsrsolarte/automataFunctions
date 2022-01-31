import json
import logging

import azure.functions as func
from comunes.services.automata_service import get_dataFrame_from_automata, validar

from comunes.utils.validations import validate_automata


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    reconocer = json.loads(req.get_body())
    automata = reconocer["automata"]

    v = validate_automata(automata)
    if not v["status"]:
        return func.HttpResponse(v["message"], status_code=400)

    if automata['type'] == 1:
        return func.HttpResponse("Only support 'automata deterministico'", status_code=400)

    df = get_dataFrame_from_automata(automata)

    return validar(df, reconocer["expression"]).to_JSON()
