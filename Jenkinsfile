pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *') // Vérifie les changements toutes les 2 minutes
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/medkhaled/TP'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest --junit-xml test-reports/results.xml test_stats_calcul.py
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Build and Deploy Docker Image') {
            steps {
                sh '''
                    docker build -t webserver .
                    docker stop webserver || true
                    docker rm webserver || true
                    docker run -d -p 8081:80 --name webserver webserver
                '''
            }
        }
    }
}
