pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root'
        }
    }

    environment {
        NEXUS_REPOSITORY_URL = 'https://nexus.house-software.com.br/repository/python-house-libs/'
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

        stage('Install Dependencies') {
            steps {
                sh '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                pip install build twine
                '''
            }
        }

        stage('Clean Build') {
            steps {
                sh '''
                rm -rf dist build src/*.egg-info
                '''
            }
        }

        stage('Build Package') {
            steps {
                sh '''
                python -m build
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
                    python -m twine upload \
                      --repository-url $NEXUS_REPOSITORY_URL \
                      -u $NEXUS_USER \
                      -p $NEXUS_PASSWORD \
                      dist/*
                    '''
                }
            }
        }
    }
}