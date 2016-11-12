# ping-o-bot

A bot that uses the ping-o-matic web tool to ping search engine crawlers

Ping-o-Bot is a website which helps bloggers in pinging the search engine crawlers every time they publish new content. In there website, one has to fill out a form regarding the details of the blog/website. Then the crawllers are pinged. To avoid filling out the form again and again, they a provid a link which needs to be bookmarked. And everytime the link is opened, the crawlers are pinged.

I don't know if the tool really works. This script is built assuming that it does. But I have actually noticed a significant increase in the organic traffic of my blog.

So, in this script, I am just calling that bookmark link every 30mins. If you try to ping within the 30mins, the website says "Slow down cowboy!". 

Go through the code and feel free to play around with it. 

To run the script, install the required dependencies, replace the URL with your bookmark link URL and execute "python Ping-o-matic.py"

[Read more](http://teckguide.blogspot.com/2016/03/ping-o-matic-python.html)