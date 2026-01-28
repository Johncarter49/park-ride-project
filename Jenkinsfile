pipeline {
    agent any

    environment {
        SCHOOL = "datascientest"
        NAME = "Anthony"
        APP_DIR = "theme-park-ride-gradle"
    }

    stages {
        stage("Env Variables") {
            environment {
                NAME = "lewis" // replaces the NAME variable defined at the pipeline level
                BUILD_ID = "2" // replaces the default BUILD_ID variable
            }

            steps {
                echo "SCHOOL = ${env.SCHOOL}"
                echo "NAME = ${env.NAME}"
                echo "BUILD_ID = ${env.BUILD_ID}"

                script {
                    env.SOMETHING = "1"
                }
            }
        }

        stage("Override Variables") {
            steps {
                script {
                    env.SCHOOL = "I LOVE DATASCIENTEST!" // cannot replace SCHOOL defined at the pipeline or stage level
                    env.SOMETHING = "2" // can replace a variable created imperatively
                }

                echo "SCHOOL = ${env.SCHOOL}"
                echo "SOMETHING = ${env.SOMETHING}"

                withEnv(["SCHOOL=DEV UNIVERSITY"]) { // can replace any variable
                    echo "SCHOOL = ${env.SCHOOL}"
                }

                withEnv(["BUILD_ID=1"]) {
                    echo "BUILD_ID = ${env.BUILD_ID}"
                }
            }
        }

        stage("Build") {
            steps {
                dir("${env.APP_DIR}") {
                    sh "chmod +x ./gradlew"
                    sh "./gradlew clean build"
                }
            }
        }

        stage("Unit Tests") {
            steps {
                dir("${env.APP_DIR}") {
                    sh "./gradlew test"
                }
            }
        }

        stage("Docker Build") {
            steps {
                dir("${env.APP_DIR}") {
                    sh "docker build -t theme-park-ride-gradle:jenkins ."
                }
            }
        }

        stage("Deploy Dev (auto)") {
            steps {
                dir("${env.APP_DIR}") {
                    sh "docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d"
                }
            }
        }

        stage("Deploy Prod (manual)") {
            steps {
                input message: "Approve production deployment?"
                dir("${env.APP_DIR}") {
                    sh "docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d"
                }
            }
        }

        stage("Kubeconfig (optional)") {
            steps {
                script {
                    if (!env.KUBECONFIG_CMD || env.KUBECONFIG_CMD.trim().isEmpty()) {
                        error "KUBECONFIG_CMD is not set. Provide the exact command to generate kubeconfig."
                    }
                }
                sh "${env.KUBECONFIG_CMD}"
            }
        }
    }
}
