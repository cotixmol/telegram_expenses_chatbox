from fastapi.responses import JSONResponse


def standard_response(status_code: int, message: str):
    return JSONResponse(
        content={
            "status": status_code,
            "message": message,
        }
    )
