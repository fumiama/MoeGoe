import azure.functions as func

from api import Speaker


speaker = Speaker('DRACU-RIOT!/config.json', 'DRACU-RIOT!/639_epochs.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)
