import azure.functions as func

from api import Speaker


speaker = Speaker('genshin_xm37.config', 'genshin.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)
