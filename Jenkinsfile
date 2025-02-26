pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/medkhaled/TP'
                echo 'Checkout'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv .venv && . .venv/bin/activate && python -m pip install -r requirements.txt'
                echo 'build'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s . -p "test_stats_calcul.py"'
                echo 'Tests'
            }
        }
    }
}
