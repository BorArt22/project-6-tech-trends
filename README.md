# TechTrends

TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

The web application is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database to store the submitted articles.

Below you can examine the main components of the firsts prototype of the application:
<figure>
  <img
  src="https://video.udacity-data.com/topher/2021/January/5ff782da_screenshot-2021-01-07-at-21.53.16/screenshot-2021-01-07-at-21.53.16.png"
  alt="TechTrends web application components">
  <figcaption>TechTrends web application components</figcaption>
</figure>

Additionally, the initial sitemap of the website can be found below:
<figure>
  <img
  src="https://video.udacity-data.com/topher/2021/January/5ff78576_screenshot-2021-01-07-at-22.04.29/screenshot-2021-01-07-at-22.04.29.png"
  alt="Diagram with the sitemap of the web applciation">
  <figcaption>TechTreds sitemap</figcaption>
</figure>

Where:
 - **About** page - presents a quick overview of the TechTrends site 
 - **Index** page - contains the content of the main page, with a list of all available posts within TechTrends 
 - **New Post** page - provides a form to submit a new post 
 - **404** page - is rendered when an article ID does not exist is accessed

And lastly, the first prototype of the application is storing and accessing posts from the "POSTS" SQL table. A post entry contains the post ID (primary key), creation timestamp, title, and content. The "POSTS" table schema can be examined below:
<figure>
  <img
  src="https://video.udacity-data.com/topher/2021/January/5ff81ebb_screenshot-2021-01-07-at-22.16.30/screenshot-2021-01-07-at-22.16.30.png"
  alt="Table with the SQL schema for the posts table">
  <figcaption>The schema for the "posts" table</figcaption>
</figure>

# Test workflow
