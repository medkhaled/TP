pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt'
                echo 'Dependencies installed'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. .venv/bin/activate && pytest --junit-xml test-reports/results.xml test_stats_calcul.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
