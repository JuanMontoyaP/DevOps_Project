pipeline {
    agent any

    parameters {
        booleanParam(name: 'buildImage', defaultValue: false, description: 'Build docker image?')
        booleanParam(name: 'destroy', defaultValue: false, description: 'Destroy Terraform build?')
    }

    environment {
        dockerhub=credentials('dockerhub')
        AWS_ACCESS_KEY_ID=credentials('aws_access_key_id')
        AWS_SECRET_ACCESS_KEY=credentials('aws_secret_access_key')
        us-west-key=credentials('us-west-key') 
    }

    stages {

        stage("verify tooling") {
            
            steps {
                sh '''
                    docker version
                    docker info
                    terraform -help
                    ansible --version
                '''
            }
        }

        stage("build docker image") {

            when {
                equals expected: true, actual: params.buildImage
            }

            steps {
                sh '''
                    docker build -t jpmontoya19/cisco_demo:flask-app .
                '''
            }
        }

        stage("push image to docker-hub") {

            when {
                equals expected: true, actual: params.buildImage
            }

            steps {
                sh '''
                    echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin
                    docker push jpmontoya19/cisco_demo:flask-app
                '''
            }
        }

        stage("initialize terraform") {
            
            steps {
                dir('terraform') {
                    sh "terraform init"
                }
            }
        }

        stage("plan infrastructure") {

            when {
                not {
                    equals expected: true, actual: params.destroy
                }
            }

            steps {
                dir('terraform') {
                    sh '''
                        terraform plan
                    '''
                }
            }
        }

        stage("build infrastructure") {

            when {
                not {
                    equals expected: true, actual: params.destroy
                }
            }

            steps {
                dir('terraform') {
                    sh "terraform apply --auto-approve"
                }
            }
        }

        stage("Use ansible") {
            when {
                not {
                    equals expected: true, actual: params.destroy
                }
            }

            steps {
                dir('ansible') {
                    sh "ansible-playbook -i dev.inv playbook.yml --key-file us-west-key"
                }
            }
        }

        stage("destroy infrastructure") {
            when {
                equals expected: true, actual: params.destroy
            }

            steps {
                dir('terraform') {
                    sh "terraform destroy --auto-approve"
                }
            }
        }
    }
}