import azure.functions as func

from api import Speaker


speaker = Speaker('genshin.json', 'G_xm37_361200.pth')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return speaker.main(req)
