pipeline {
    agent any
    stages {
        stage('Clonar Repositório') {
            steps {
                echo 'Repositório clonado automaticamente pelo Jenkins.'
            }
        }
        stage('Build dos Serviços') {
            steps {
                echo 'Construindo imagens Docker...'
                sh 'docker-compose build auth_service orders_service'

            }
        }
        stage('Deploy dos Serviços') {
            steps {
                echo 'Realizando deploy dos microserviços com docker-compose up...'
                sh 'docker-compose up -d auth_service orders_service'
            }
        }
        stage('Verificar Serviços') {
            steps {
                echo 'Listando containers ativos...'
                sh 'docker ps'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finalizado!'
        }
    }
}
