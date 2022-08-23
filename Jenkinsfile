pipeline {
  environment {
    registry = "jodennis/jenkins-docker"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
        sh 'python k8s-flask/k8sflask.py &'
      }
    }

    stage('Test App') {
      steps {
        sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt && python k8s-flask/k8sflaskunittest.py'
      }
    }
    
    stage('Build Docker Container') {
      steps{
        script {
          dockerImage = docker.build(registry + ":$BUILD_NUMBER")
        }
      }
    }

    stage('Upload Container to Registry') {
      steps{
        script {
          docker.withRegistry('', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }


    /*stage('Remove docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }*/
  }
}
