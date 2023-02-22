pipeline{
    agent { any { image 'python:3.10.7-alpine' } }
    stages{
        
        stage("build"){
            steps{
                sh "python3 --version"
                sh 'python3 -m venv testing-venv'
                sh 'source testing-venv/bin/activate'
                sh 'pip install -r requirements.txt --user'
                sh 'coverage run'
            }
        }
        stage("test"){
            steps{
                
                echo "running tests"
                sh 'pytest'
            }
        }
        stage("deploy"){
            steps{
                echo "deploying"
            }
        }
    }
}