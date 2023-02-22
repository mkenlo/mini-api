pipeline{
    agent { any { image 'python:3.10.7-alpine' } }
    stages{
        
        stage("build"){
            steps{
                sh "python3 --version"
                sh 'pip3 install -r requirements.txt --user'
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