pipeline {
    agent any

    stages {
        
        stage('Install Dependencies') {
            steps {
                sh 'sudo apt install python3.12-venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt'
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
