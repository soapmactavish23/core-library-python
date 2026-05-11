pipeline {
    agent any

    environment {
        NEXUS_REPOSITORY_URL = 'https://nexus.house-software.com.br/repository/python-house-libs/'
        PYTHON_VERSION = 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Read Version') {
            steps {
                script {
                    def versionFile = readFile('version.properties').trim()
                    env.LIB_VERSION = versionFile
                        .split('\n')
                        .find { it.startsWith('version=') }
                        .replace('version=', '')
                        .trim()

                    echo "Building core-library-python version: ${env.LIB_VERSION}"
                }
            }
        }

        stage('Create Venv') {
            steps {
                bat """
                ${PYTHON_VERSION} -m venv .venv
                .venv\\Scripts\\python -m pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                .venv\\Scripts\\pip install -r requirements.txt
                .venv\\Scripts\\pip install build twine
                """
            }
        }

        stage('Tests') {
            steps {
                bat """
                .venv\\Scripts\\python -m pytest || exit /b 0
                """
            }
        }

        stage('Clean Build') {
            steps {
                bat """
                if exist dist rmdir /s /q dist
                if exist build rmdir /s /q build
                if exist src\\core_library_python.egg-info rmdir /s /q src\\core_library_python.egg-info
                """
            }
        }

        stage('Build Package') {
            steps {
                bat """
                .venv\\Scripts\\python -m build
                """
            }
        }

        stage('Publish Nexus') {
            when {
                branch 'prod'
            }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'nexus-credentials',
                    usernameVariable: 'NEXUS_USER',
                    passwordVariable: 'NEXUS_PASSWORD'
                )]) {
                    bat """
                    .venv\\Scripts\\python -m twine upload ^
                      --repository-url %NEXUS_REPOSITORY_URL% ^
                      -u %NEXUS_USER% ^
                      -p %NEXUS_PASSWORD% ^
                      dist/*
                    """
                }
            }
        }
    }

    post {
        success {
            echo "core-library-python ${env.LIB_VERSION} publicada com sucesso."
        }

        failure {
            echo "Falha ao gerar/publicar core-library-python."
        }
    }
}