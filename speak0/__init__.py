import azure.functions as func

from api import Speaker


speaker = Speaker('Zeronotsukaima/config.json', 'Zeronotsukaima/616_epochs.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)
