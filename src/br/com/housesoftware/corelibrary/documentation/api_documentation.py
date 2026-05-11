from br.com.housesoftware.corelibrary.config.core_constants import CoreConstants


class ApiDocumentation:

    @staticmethod
    def common_responses() -> dict:
        return {
            400: CoreConstants.Documentation.ResponsesErros.ERROR_400,
            401: CoreConstants.Documentation.ResponsesErros.ERROR_401,
            403: CoreConstants.Documentation.ResponsesErros.ERROR_403,
            404: CoreConstants.Documentation.ResponsesErros.ERROR_404,
            500: CoreConstants.Documentation.ResponsesErros.ERROR_500,
        }

    @staticmethod
    def pageable_parameters() -> list[dict]:
        return [
            {
                "name": "page",
                "in": "query",
                "description": "Número da página (0..N)",
                "type": "integer",
                "default": 0,
            },
            {
                "name": "size",
                "in": "query",
                "description": "Quantidade de elementos por página (0..N)",
                "type": "integer",
                "default": 10,
            },
            {
                "name": "sort",
                "in": "query",
                "description": "Critério de ordenação: propriedades(asc|desc)",
                "examples": ["nome", "nome,asc", "nome,desc"],
            },
        ]

    @staticmethod
    def read_parameter() -> dict:
        return {
            "summary": CoreConstants.Documentation.Summary.READ,
            "description": CoreConstants.Documentation.Summary.READ_DESCRIPTION,
            "response_code": 200,
            "security": CoreConstants.Documentation.SECURITY_SCHEME_NAME,
        }

    @staticmethod
    def create_parameter() -> dict:
        return {
            "summary": CoreConstants.Documentation.Summary.CREATE,
            "description": CoreConstants.Documentation.Summary.CREATE_DESCRIPTION,
            "response_code": 201,
            "security": CoreConstants.Documentation.SECURITY_SCHEME_NAME,
        }

    @staticmethod
    def update_parameter() -> dict:
        return {
            "summary": CoreConstants.Documentation.Summary.UPDATE,
            "description": CoreConstants.Documentation.Summary.UPDATE_DESCRIPTION,
            "response_code": 200,
            "security": CoreConstants.Documentation.SECURITY_SCHEME_NAME,
        }

    @staticmethod
    def delete_parameter() -> dict:
        return {
            "summary": CoreConstants.Documentation.Summary.DELETE,
            "description": CoreConstants.Documentation.Summary.DELETE_DESCRIPTION,
            "response_code": 204,
            "security": CoreConstants.Documentation.SECURITY_SCHEME_NAME,
        }

    @staticmethod
    def upload_parameter() -> dict:
        return {
            "summary": CoreConstants.Documentation.Summary.UPLOAD,
            "description": CoreConstants.Documentation.Summary.UPLOAD_DESCRIPTION,
            "response_code": 200,
            "media_type": "multipart/form-data",
            "security": CoreConstants.Documentation.SECURITY_SCHEME_NAME,
        }

    @staticmethod
    def custom_parameter(summary: str, description: str) -> dict:
        return {
            "summary": summary,
            "description": description,
            "response_code": 200,
            "security": CoreConstants.Documentation.SECURITY_SCHEME_NAME,
        }