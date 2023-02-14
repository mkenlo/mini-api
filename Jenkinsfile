pipeline{
    agent any
    stages{
        
        stage("build"){
            steps{
                echo "buiding project"
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