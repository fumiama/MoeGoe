import azure.functions as func

from api import Cleaner


cleaner = Cleaner('genshin_xm37.config')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return cleaner.main(req)
