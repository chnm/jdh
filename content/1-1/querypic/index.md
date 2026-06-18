+++
title = "Review of QueryPic, produced by Tim Sherratt"
slug = "querypic"
type = "article"
date = 2011-12-01
issue = "1-1"
volume = 1
number = 1
season = "Winter"
year = 2011
section = "Reviews"
section_url = "/category/1-1/reviews-1-1/"
section_weight = 4
weight = 3
authors = ["Jeremy Boggs", "David McClure", "Eric Rochester", "Wayne Graham"]
author_ids = ["jboggs", "clured", "erochester", "wgraham"]
author = ["jboggs", "clured", "erochester", "wgraham"]
+++

[QueryPic](http://discontents.com.au/shed/hacks/querypic "QueryPic") is a graphical search summarizer that mines content in the [Trove](http://trove.nla.gov.au/ "Trove, the National Library of Australia Digitised Newspaper Collection") newspaper archive from the [National Library of Australia](http://www.nla.gov.au/ "National Library of Australia"). The program is part of Tim Sherratt’s larger [TroveNewspaper software project](http://wraggelabs.com/emporium/trove-tools/ "Tools for Trove"), which allows researchers to obtain parsable data from the Trove collection. QueryPic searches the Trove newspaper archive, scrapes the returns, and graphs the results of the search. QueryPic uses the Python programming language, and is [available on GitHub](https://github.com/wragge/Trove-newspapers "Tools for Trove on GitHub") under a GPL v3 license.

Using QueryPic requires some comfort entering commands on the console or terminal. To start, users first must download the TroveNewspaper package (or clone the Git repository) to their computer. Then, users must open a terminal and change into the TroveNewspaper package directory, and type commands in order to submit a query to the Trove archive:

```python
python do_totals.py "http://trove.nla.gov.au/newspaper/result?q=drought" -g "drought_flood"
```

For the example above, QueryPic generates a chart called “drought_flood” in a ‘graphs’ directory that plots the number of articles found by year for a query on “drought.” The chart provides a great way to explore the results of any given query on the Trove newspaper archive. Clicking on each point on the graph reveals a list of articles returned by the query, with links to view each article in the Trove archive. Sherratt includes several options for generating the graphs. Users can generate a single graph for multiple queries to compare the results of each, by making sure the value for the graph name ‘-g’ is the same. Users also can plot changes in the query results by month instead of year.

<div class="wp-caption aligncenter" id="attachment_574" style="width: 963px"><a href="https://journalofdigitalhumanities.org/wp-content/uploads/2012/03/querypic.jpg" target="_blank" title="A screenshot of a chart generated with QueryPic."><img alt="A screenshot of a chart generated with QueryPic." aria-describedby="caption-attachment-574" class="wp-image-574" height="603" src="https://journalofdigitalhumanities.org/wp-content/uploads/2012/03/querypic.jpg" title="A screenshot of a chart generated with QueryPic." width="953"/></a><p class="wp-caption-text" id="caption-attachment-574">A screenshot of a chart generated with QueryPic.</p></div>

The graphs are generated on a well-formatted HTML file, using [HTML5 Boilerplate](http://html5boilerplate.com "HTML 5 Boilerplate") for page markup and the [960 Grid System](http://960.gs "960 Grid System") for styling and layout. QueryPic also uses the [HighCharts](http://www.highcharts.com/ "HighCharts Java Script Library") JavaScript library to create the line graph. Transferring these graphs to a public web page would be relatively easy, as long as the accompanying CSS and JavaScript files are also transferred.

A few areas for improvement for the scripts themselves: The way the TroveNewspaper package is currently written sends a high volume of requests to the Trove archive, so the Australian National Archives could potentially throttle requests if increased use of the script occurs. Perhaps the TroveNewspaper package should limit the rate at which it issues requests to avoid overtaxing the National Archives system. The project might also benefit from having some continuous testing that will parse the data from the Trove archive, which could provide regular alerts if the Trove site changes its markup and consequently breaks any scripts in the TroveNewspaper package. Also, the way that the software is currently constructed makes it difficult for developers to use this in a larger application. However, adding a setup file to the package would allow the software to be easily used in other Python applications.

Of course, any script that relies on screenscraping will eventually break. Even slight changes to the HTML you are scraping can break the script, as was the case for the review team. Fortunately the fix was easy, and the team member who discovered the issue (Rochester) [submitted a fix](https://github.com/wragge/Trove-newspapers/commit/f659fc7ab49b1eed74bda3e1523c47d3c9fa8393 "Pull Request for Trove on GitHub"), which Sherratt quickly added to the TroveNewspaper package. This quick response, combined with Sherratt’s own commit history to the project and [exploration of its use](http://discontents.com.au/tag/trove "Tim Sherratt, Explorations Using Trove") on his blog, indicates that development on the project is active and attentive.

QueryPic, and the TroveNewspaper package of which it is part, are a great example of how digital humanists are exploring and implementing new functionality for existing resources. QueryPic is of particular use to anyone using the Trove archive to research Australian history and culture. Sherratt’s broader software projects also serve as a model for anyone with moderate programming knowledge (or access to someone who does) who wants to create tools for use with other archives.
