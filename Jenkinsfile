pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the latest code from your GitHub repository
                git branch: 'main', url: 'https://github.com/mohammednyc22/python-qa-framework.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                // Creates a clean Python virtual environment inside the workspace
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installs all required packages from requirements.txt inside the venv
                sh '''
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run BDD Tests') {
            steps {
                // Runs your Behave BDD test features
                sh '''
                    . venv/bin/activate
                    behave
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}