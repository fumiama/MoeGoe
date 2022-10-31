import azure.functions as func

from api import Speaker


speaker = Speaker('TheFoxAwaitsMe/config.json', 'TheFoxAwaitsMe/1164_epochs.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)
