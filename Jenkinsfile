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
        sh 'python .k8s-flask/jenkinsFlask.py &'
      }
    }

    stage('Test App') {
      steps {
        sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt && python .k8s-flask/jenkinsUnittest.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      } 
    }
    
    stage('Build Docker Container') {
      steps{
        script {
          dockerImage = docker.build(registry + ":$BUILD_NUMBER")
        }
      }
    }

    /*stage('Upload Container to Registry') {
      steps{
        script {
          docker.withRegistry('', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }*/

    stage('Run image locally'){
      steps{
        sh "kubectl set image deployment k8sflaskdeployment k8sflask=$registry:$BUILD_NUMBER"
      }
    }

    /*stage('Remove docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }*/
  }
}