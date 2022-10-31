import azure.functions as func

from api import Speaker


speaker = Speaker('HamidashiCreative/config.json', 'HamidashiCreative/604_epochs.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)
