pipeline {
    agent any

    parameters {
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
        booleanParam(name: 'destroy', defaultValue: false, description: 'Destroy Terraform build?')
    }

    environment {
        dockerhub=credentials('dockerhub')
        AWS_ACCESS_KEY_ID=credentials('aws_access_key_id')
        AWS_SECRET_ACCESS_KEY=credentials('aws_secret_access_key')
    }

    stages {

        stage("verify tooling") {
            
            steps {
                sh '''
                    docker version
                    docker info
                '''
            }
        }

        stage("build docker image") {

            steps {
                sh '''
                    docker build -t jpmontoya19/cisco_demo:flask-app .
                '''
            }
        }

        stage("push docker image to docker-hub") {

            steps {
                sh '''
                    echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin
                    docker push jpmontoya19/cisco_demo:flask-app
                '''
            }
        }

        stage("plan infrastructure with terraform") {

            when {
                not {
                    equals expected: true, actual: params.destroy
                }
            }

            steps {
                sh '''
                    pwd
                    terraform init
                    terraform plan
                '''
            }
        }
    }
}