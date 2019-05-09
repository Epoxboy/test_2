# Interview Test 2: Building Microservices API with Python + Flask and Docker

Introduction

This small API demo application is written in Python 2.7 with Flask Microframework, it includes only one endpoint  "/healthcheck" , and gives a JSON format response when hit. It'll return:

   * Applications Version. 
   * Description. ("static variable")
   * Last Commit SHA. 

The Build and Deployment are managed by Travis CI, every commit will trigger a pipeline run:

    1) Build_image:
       It'll build a new docker image
    2) Push_image:
       It'll push new image to Docker hub, my personal repo, with image name epoxboy/interview-test2:$SHORT_HASH

Usage

   To run the app, you need to get Docker installed on your computer, then use following command to pull the image down and run:

   docker run --rm -p 5008:5008 epoxboy/interview-test2:b64ff8e

   It'll pull down the image and start up container with image tag b64ff8e, which you can change to the corresponding commit hash from Github repo commit history. The container will map the servie to your localhost port 5008, you can then verify the service by using:

   curl localhost:5008/healthcheck

   or 
   
   paste http://localhost:5008/healthcheck url in your web browser
   


Moving further

The API test is missing in the pipeline, which can be done with Postman newman integration with Travis CI. Steps:

1, Integrated Newman with Travis CI
https://blog.getpostman.com/2017/08/23/integrate-api-tests-with-postman-newman-and-travis-ci/

2, Add Deployment stage after Push_image, to deploy the app microservice to a Cloud platform (or using Swagger to
   create an REST API, imported to Cloud Native API gateway in front of backend microservices )

3, Add Test stage after Deployment, to run Newman test against microservice directly (or against API gateway if a REST API is imported
   as microservices' front end)












