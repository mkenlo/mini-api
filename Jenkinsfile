pipeline{
    //agent { any { image 'python:3.10.7-alpine' } }
    agent any
    stages{
        
        stage("build and test"){
            agent{
                any {
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
                        app = docker.build('mkenlo/mini-api', ' -f ./prod/Dockerfile .')
                        withDockerRegistry([ credentialsId: "edd2d278-66f7-4779-8f9c-e37c1b9465dd", url: "" ]) {
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