<<<<<<< HEAD
pipeline{
    agent any
    parameters {
	string(name: 'TAG',defaultValue: 'last',description: 'the docker tag you want to release')
    }
    environment {
	TAG = "${params.TAG}"
	USER = "root"
	HOST = "10.10.0.212"
    }
    stages {
        stage('k8s部署服务') {
            steps {
                sh "ssh ${USER}@${HOST}  ls /data/docker"
=======
pipeline {
    agent any
    parameters {
	string(name: 'BRANCH',defaultValue: 'master',description: 'you want to release the branch')
	string(name: 'TAG',defaultValue: 'last',description: 'the tag of the docker images')
    }
    environment {
        BRANCH = "${params.BRANCH}"
        PROJECT = "cmdb"
	TAG = "${params.TAG}"
    }
    stages {
        stage('本地代码更新') {
            steps {
                sh " cd /data/git-app/$PROJECT && git pull && git checkout $BRANCH "
		}		
            }
        stage('代码打包') {
            steps {
                sh "cd /data/git-app/$PROJECT && tar -czvf  ${PROJECT}.tar.gz ./guokr-cmdb && mv  ${PROJECT}.tar.gz /data/docker-app/$PROJECT "
            }
        }
        stage('生成docker镜像') {
            steps {
                sh "  cd /data/docker-app/$PROJECT  && docker  build -t 180.76.244.5/quxiaotong/${PROJECT}:$TAG . "
            }
        }
        stage('推送docker镜像') {
            steps {
                sh " docker push 180.76.244.5/quxiaotong/${PROJECT}:$TAG "
>>>>>>> dev
            }
        }
    }
}
