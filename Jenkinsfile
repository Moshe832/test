pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh 'python3 -m pytest test.py' 
            }
        }
    }
}
