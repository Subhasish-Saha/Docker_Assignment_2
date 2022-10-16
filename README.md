# Docker & Docker hub Assignment_2

## Assignment 1: Demonstrate minimum 15 basic docker command with explanation and screenshot.

## Docker commands : 

1. > docker pull hello-world

This command is used to pull images from the docker repository(hub.docker.com) 

![image1](/image/docker_pull.png)

2. > docker images

This command lists all the locally stored docker images

![image2](/image/docker_images.png)

3. > docker run [name]

This command is used to create a container from an image.

![image3](/image/docker_run.png)

4. > docker ps

This command is used to list the running containers.

![image4](/image/docker_ps.png)

5. > docker stop [container ID]

This command stops a running container.

![image5](/image/docker_stop.png)

6. > docker pause [container ID]

This command is used to pause a running container.

![image6](/image/docker_pause.png)

7. > docker unpause [container ID]

This command is used to unpause a running container.

![image7](/image/docker_unpause.png)

8. > docker rmi -f [name/ID]

This command is used to delete an image from the local storage.

![image8](/image/docker_rmi.png)

9. > docker build -t [path]

This command is used to build an image from a specified docker file.

![image9](/image/docker_build.png)

10. > docker push [username/image_name]

This command is used to push an image to the docker hub repository.

![image10](/image/docker_push.png)

11. > docker port [container ID]

This command is used to view the port mapping of a specific container.

![image11](/image/docker_port.png)

12. > docker top [container ID]

This command is used to view the running process in a specific container.

![image12](/image/docker_top.png)

13. > docker logs [container ID]

This command is used to view the logs from the running container.

![image13](/image/docker_logs.png)

14. docker stats [container ID]

This command is used to view the usage statistics a container.

![image14](/image/docker_stats.png)

15. docker diff [container ID]

This command is shows the changes to the directories on a filesystem.

![image15](/image/docker_diff.png)



## Assignment 2: Hello World Docker Image Run Hello World Docker Image Locally.

![image16](/image/docker_task_2.png)

## Assignment 3: Create a hello world fastapi application. Create a Dockerfile for your fastapi hello world application. Build Docker image using Docker file. Run docker image build in previous step. Push your Docker image to Docker Hub.

![image](/image/build_fast_api_docker.png)
![image](/image/run_fastapi.png)
![image](/image/fastapi_docker.png)
[Here is a link to my docker_hub/fastapi-hello-world](https://hub.docker.com/r/subhasish30/fastapi-hello-world)

## Assignment 4: Automate Assignment below task using github action.
## 1. Build Docker Image
## 2. Push Docker Image to Docker hub.

