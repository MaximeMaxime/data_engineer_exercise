# Data Engineering Exercises

Below are some data engineering exercices. Note that we will use them to evaluate : 
1. Your knowledge and ability to use / learn multiple scripting languages and technologies;
2. Your data engineering designing skills, and;
3. Your creativity.

## To Do 
1. Follow the instructions below while maintaining a presentable (clean) project. 
2. Over the next interview, we will ask that you present a demo of your work (environment set up, tools used, architecture, pipelines developped, scripts, etc...).
Use any presentation form you deem necessary (ppt, pdf, schema, drawings, code snippets, etc.) in addition to the live demo.

## Remember 
1. Ensure you apply best scripting/development practices.
2. Make assumptions where necessary - We are interested in your approach primarily.
3. The best of works goes unnoticed if not well explained - You only have 30-40min to present your work, focus on the important pieces.
4. Be creative.

**Good Luck!**
<br></br>
<br></br>


# Exercise 1 : Data Ingestion / Scraping
1. Design and implement a pipeline to ingest the RSS feed from https://www.cbc.ca/cmlink/rss-topstories and retrieve the following info about the ingested articles
    * Timestamp
    * Author
    * Title
    * Descriptive text
2. Push the ingested data to the service in Exercise 2

**Extra points** : What would you do if there was no RSS feed available? Implement an engine that would retrieve the same information directly from https://www.cbc.ca/news periodically (ex : every hour) 

# Exercise 2 : Data Engineering & Storing
As data is received from the service in Exercise 1, it should be curated then stored. 
1. Clean up the data to facilitate its retrieval as described in *Exercise 3*
2. Store the data in the engine of your choice, keep in mind the following requirements : 
    * There will be many services like the one in Exercise 1 pushing data from different sources
    * Later use of the stored data will be to be retrieved as described in *Exercise 3*

# Exercise 3 : Retrieve API
Create a service allowing GET requests to search the stored data by timestamp, author and/or keywords, returning the stories.

# Exercise 4 : Monitoring
1. Monitor the health status of your pipelines & services from previous exercises
2. Create an alerting system based on this health status check

# Extra points : ML Serving
The *rocket_science.py* file contains a state-of-the-art machine learning algorithm to identify if the ingested article is of interest or not. Implement it the architecture you have constructed so far and store it's output in the engine chosen in *Exercise 2*
```
Input : article_text (string) : The text of the article
Output : interest_level (float) : Interest level on the article, ranges from 0 to 1.
```

  * Can you ensure scalability of the engine?
  * Can you monitor the health of the engine?

