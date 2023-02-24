pipeline{
    agent any
    stages{
        
        stage("build and test"){
            agent{
                docker {
                    image 'python:3.10.7-alpine'
                }
            }
            steps{
                sh "python3 --version"
                sh 'pip install -r requirements.txt --user'
                sh 'python3 -m pytest'
            }
        }
        stage('build  and push image'){
            steps{
                    script{
                        app = docker.build('mkenlo/mini-api', './prod/')
                        withDockerRegistry([ credentialsId: "DockerHub Credentials", url: "" ]) {
                            app.push()
                        }
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