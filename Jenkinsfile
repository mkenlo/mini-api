pipeline{
    agent { any { image 'python:3.10.7-alpine' } }
    stages{
        
        stage("build"){
            steps{
                sh "python3 --version"
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage("test"){
            steps{
                
                echo "running tests"
                sh 'python3 -m pytest'
            }
        }
        stage('build  and push image'){
            steps{
                 app = docker.build('mkenlo/mini-api', './prod/')
                withDockerRegistry([ credentialsId: "DockerHub Credentials", url: "" ]) {
                    app.push()
                }
                }
           
        }

        stage("deploy"){
            steps{
                echo "deploying"
                
            }
        }
    }
}