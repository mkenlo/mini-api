pipeline{
    agent { docker { image 'python:3.10.7-alpine' } }
    stages{
        
        stage("build"){
            steps{
                sh "python --version"
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