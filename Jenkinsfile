pipeline{
    agent { any { image 'python:3.10.7-alpine' } }
    stages{
        
        stage("build"){
            steps{
                sh "mkdir /tmp"
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