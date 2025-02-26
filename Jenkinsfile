pipeline {
    agent any

    stages {
        
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv .venv && . .venv/bin/activate && python -m pip install -r requirements.txt'
                echo 'build'
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
