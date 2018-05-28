# Data Engineering Exercises

Below are some data engineering exercices. Note that we will use them to evaluate : 
1. Your knowledge and ability to use / learn multiple scripting languages and technologies;
2. Your data engineering designing skills, and;
3. Your creativity.

## To Do : 
1. Follow the instructions below while maintaining a presentable (clean) project. 
2. Over the next interview, we will ask that you present a demo of your work (environment set up, tools used, architecture, pipelines developped, scripts, etc...).
Use any presentation form you deem necessary (ppt, pdf, schema, drawings, code snippets, etc.) in addition to the live demo.

## Remember : 
1. Ensure you apply best scripting/development practices.
2. Make assumptions where necessary - We are interested in your approach primarily.
3. The best of works goes unnoticed if not well explained - You only have 30-40min to present your work, focus on the important pieces.
4. Be creative.

# Exercise 1 : Webscraping Pipelines & Messaging

Design and develop a pipeline to keep track of top articles on https://www.kdnuggets.com/ using the "Top Stories Past 30 Days" section of the page. 
1. Every hour, gather the following info about the top 10 most popular stories from that list
  1. timestamp
  2. author
  3. title
2. Create a pipeline to push this info to a messaging system (Pipeline A)
3. Design a schema for storing this information in a database
4. Create a pipeline to consume from the messaging system and store in the database (Pipeline B)

# Exercise 2 : 
Create another pipeline (Pipeline C) to consume the message queue above, compute article count by author and store the results into the database.

# Exercise #3 : 
Develop a web service which takes an author's name as input and returns the last three articles stored in your database for that author.

# Extra Points : 
- Can you monitor the health status of your pipelines & APIs?
- Can you implement this using Google Cloud Platform's tools & technologies? (Note : you have 300$ worth of free credits the first time you sign in to GCP)

*IMPORTANT* : Here are some *examples* of technologies that we would like to see in action :
1. An OOP Language : Python or Scala
2. A pipelining framework : Airflow, Luigi or Pinball
3. A messaging broker : Rabbitmq or Kafka,
4. A real time processing framework : Spark or Storm
5. A permanent storage : postgres or cassandra
