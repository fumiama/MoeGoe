import azure.functions as func

from api import Cleaner


cleaner = Cleaner('TheFoxAwaitsMe/config.json')


def main(req: func.HttpRequest) -> func.HttpResponse:
    return cleaner.main(req)
