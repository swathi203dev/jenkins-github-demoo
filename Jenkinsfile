pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting source code from GitHub'
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Automated Tests') {
            steps {
                echo 'Running website tests'
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
    }
}
