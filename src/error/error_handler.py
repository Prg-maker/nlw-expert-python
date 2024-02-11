from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprossable_entity import HttpUnprocessableEntityError

def handle_erros(error:Exception) -> HttpResponse:

    if isinstance(error, HttpUnprocessableEntityError):


        # enviar para um log
        # enviar um email de notificaçao
        return  HttpResponse(
            status_code=error.status_code,
            body = {
                "erros": [{
                    "title":error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "erros":[{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )