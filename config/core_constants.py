class CoreConstants:
    class Messages:
        NOT_FOUND = "Não Encontrado"
        OPERACAO_NAO_PERMITIDA = "recurso.operacao-nao-permitida"
        MENSAGEM_INVALIDA = "mensagem.invalida"
        IMAGE_PROCESS_ERROR = "Erro ao processar imagem."

    class Documentation:
        RESOURCES = "Todos os recursos referentes a "

        class Summary:
            FIND_ALL = "Listar todos os registros."
            CREATE = "Cadastrar novo registro."
            UPDATE = "Atualizar registro."
            DELETE = "Excluir registro."
            FIND_BY_ID = "Buscar registro por id."
            UPLOAD = "Realiza o upload de um arquivo utilizando multipart/form-data"
            READ = "Listar/Pesquisar registros"

            READ_DESCRIPTION = "Use esse end-point para listar/pesquisar os registros."
            CREATE_DESCRIPTION = "Use esse end-point para criar um novo registro."
            UPDATE_DESCRIPTION = "Use esse end-point para atualizar o registro."
            DELETE_DESCRIPTION = "Use esse end-point para delete o registro"
            UPLOAD_DESCRIPTION = (
                "Use esse end-point para realizar o upload de um arquivo "
                "utilizando multipart/form-data"
            )

        class ResponseSuccess:
            FIND_ALL = "Listar localizados com sucesso."
            CREATE = "Registro cadastrado com sucesso."
            UPDATE = "Registro atualizar com sucesso."
            DELETE = "Registro excluído com sucesso."
            FIND_BY_ID = "Registro localizado."
            CODE_204 = "Sucesso, sem retorno"

        class ResponsesErros:
            ERROR_400 = "Operação não permitida"
            ERROR_404 = "Recurso não encontrado"
            ERROR_401 = "Acesso negado"
            ERROR_403 = "Permissões Insuficientes"
            ERROR_500 = "Erro interno"

        class User:
            TAG = "Usuários"
            TAG_DESCRIPTION = "Todos os recursos referentes a Usuários"
            RESET_PASSWORD_SUMMARY = "Recuperar senha do usuário"
            CHANGE_PASSWORD_SUMMARY = "Alterar a senha do usuário"
            EDIT_PROFILE_SUMMARY = "Editar perfil do usuário"
            CHANGE_STATUS_SUMMARY = "Recuso para alterar status do usuário"

        class Group:
            TAG = "Grupos"
            TAG_DESCRIPTION = "Todos os recursos referentes a Grupos"

        class Log:
            TAG = "Logs"
            TAG_DESCRIPTION = "Todos os recursos referentes a Logs"
            SEARCH = "Pesquisar logs."
            LOAD_METHODS = "Listar métodos"

        class Login:
            TAG = "Login"
            TAG_DESCRIPTION = "Todos os recursos referentes a Login"
            SUMMARY = "Autenticar usuário"
            DESCRIPTION = "Use esse end-point para autenticar o usuário."

            SUMMARY_REFRESH = "Refresh token"
            DESCRIPTION_REFRESH = "Use esse end-point para efetuar o refresh do usuário."

        SECURITY_SCHEME_NAME = "bearerAuth"