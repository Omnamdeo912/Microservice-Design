### System Design 


#### Installations 
- Docker 
- kubectl - allows users to interact with Kubernetes clusters
- minikube - local kubernetes clusters on our local machine , no deployement required on the production
- K9s - to manage the kubernetes clusetrs
- Python3
- mysql
---
> Everything is on the local for now , how to deploy?

- Why venv is used ? -> to manage dependancey conflict , to isolate projects .

- So in the Microservice design folder , all the the subfolders you see is the a microservice i.e they are itself a independent flask application.
- @server.routes - In simple terms, a decorator(@server.route) is a function that wraps another function to add some functionality to it. ... login is another function

- 


---
- you have to do `docker login` before pushing docker image to docer repo `docker push <username>/<reponame>:latest`

----
- you define the infa code into the deploy.yaml,configuremap.yaml,secreats.yaml,service.yaml file which defines the deployment of kubernets .
- So in the menifest folder we have wrote the infra code for out auth deployement.
- in deployment.yaml , we are pulling docker image form docker repo and deploying it on the kubernets .

---
- Kubernets heps us to manage contanierised applications . eg - so lets say we configure a service to have 4 pods so kube will keep the tarck of those pods and if any pods go down kube will scale the deployemt so the number of pods matches the configured(in deploy.yaml) amount , so there is no need to deploy pods manually in case of fliure.

- Also the crachloopback concept - the kube tries to restart the instance after giving it some backoff time where it tries to solve underlying issue.
- automatic scaling - w/o kube we need to go to loadbalacer and regier the new pods , but with kube just write `kubectl scale deployment --replicas=6 service` and it scale ups the service and auto configure the loadbalcer by adding new pods.
- deploy.yaml se deploy object banega , service yaml se service object ,and kube cluster is comprised of bunch of these objects and kube keep on comparing these objects to origianl on ean dtries to match ..... and to create or modify these objects is done by the kube api , and via kubectl we access these apis.
- in realword the kube cluster will be deployed on some remote server.
- Now looking at fileds of yaml ... watch later

 
---
### GAteway microservice

- gridfs - we are storing mp4,mo4 in the mongodb but mongodb has 16MB limitation on BSON(binary JSON data). So to store larger file it shards the file (gridfs ckunks the file into) hence aboid perforance degradations.
- gridfs maintains 2 ccolletions(table) ,one is actual location of file chunks and second one contain metadata about chuks and how to put them toagther.
- Pika is used for connnecting to rabbitmq.
- How rabbbit mq comes into picture - video [1.42 hr to 1.47hr]