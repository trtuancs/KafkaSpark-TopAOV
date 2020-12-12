<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://springflee.files.wordpress.com/2020/03/new-project.png" alt="Logo" width="500" height="250">
  </a>

  <h1 align="center">Process Data Streaming With Kafka, Spark and Postgres</h1>
---  
## Run project  
1.  Clone the repo :  
    ```sh
    git clone git@github.com:trtuancs/KafkaSpark-TopAOV.git
    ```
2.  Run docker-compose :  
    ```sh
    docker-compose up -d
    ```
3.  Install python3 lib for project :  
    ```sh
    pip3 install -r requirements.txt
    ```
4.  Open 2 terminal.  

    4.1  First terminal, you type following :  

    ```sh
    python3 /src/consumer.py
    ```
    This scrip start consumer of kafka and begin process data from producer.  
4.2  Second for product, you type following:

    ```sh
    python3 /src/producer.py -id 100002 -total 500000 -cus_id 5123
    ```

    With:  
    *  id: id of invoice (invoice_no)  
    *  total: grand total of invoice
    *  cus_id: id of customer  

    When you will create event to  kafka as producer with topic default is 'users'.  

    Result will show top 10 customer has avg grand total > 5000 on first terminal.  
    You can also open Spark UI to see custer and information of Spark cluster at : local:8080, or see postgres data base how connect to : admin:adminpass@127.0.0.1:32773/postgres.  
