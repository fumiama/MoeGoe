import azure.functions as func

from api import Speaker


speaker = Speaker('ToLOVERu/config.json', 'ToLOVERu/1113_epochs.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)
