pipeline {
    agent any

    environment {
        NEXUS_REPOSITORY_URL = 'https://nexus.house-software.com.br/repository/python-house-libs/'
        PYTHON_IMAGE = 'python:3.10-slim'
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

        stage('Build Package') {
            steps {
                sh '''
                docker run --rm \
                  -v "$PWD":/app \
                  -w /app \
                  $PYTHON_IMAGE \
                  sh -c "pip install --upgrade pip && pip install -r requirements.txt && pip install build twine && rm -rf dist build src/*.egg-info && python -m build"
                '''
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
                    sh '''
                    docker run --rm \
                      -v "$PWD":/app \
                      -w /app \
                      -e NEXUS_REPOSITORY_URL="$NEXUS_REPOSITORY_URL" \
                      -e NEXUS_USER="$NEXUS_USER" \
                      -e NEXUS_PASSWORD="$NEXUS_PASSWORD" \
                      $PYTHON_IMAGE \
                      sh -c "pip install twine && python -m twine upload --repository-url $NEXUS_REPOSITORY_URL -u $NEXUS_USER -p $NEXUS_PASSWORD dist/*"
                    '''
                }
            }
        }
    }
}