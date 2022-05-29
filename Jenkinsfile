properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/Ronen02/DevOps1004.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
