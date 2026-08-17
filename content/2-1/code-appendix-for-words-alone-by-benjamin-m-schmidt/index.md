+++
title = "Code Appendix for “Words Alone: Dismantling Topic Models in the Humanities”"
slug = "code-appendix-for-words-alone-by-benjamin-m-schmidt"
type = "article"
date = 2012-12-01
issue = "2-1"
volume = 2
number = 1
season = "Winter"
year = 2012
section = "Applications and Critiques"
section_url = "/category/2-1/applications-2-1/"
section_weight = 3
weight = 5
authors = ["Benjamin M. Schmidt"]
author_ids = ["bschmidt"]
author = ["bschmidt"]
+++

### Topic Modeling Ships

Begin by getting the data in order. (This data is available on request.)

```
# Oceans2
rm(list = ls())
require(ggplot2)
require(plyr)
require(lubridate)
source("ICOADS parsing.R")
source("../Map Functions.R")
```

This step pulls in the Maury data and splits it. This is not fully documented as part of this article, since the purpose is to show general geodata parsing.

```
data = loadInData("~/shipping/ICOADS/maury.txt")
data = splitDataByVoyage(data)
```

Next, save the R data.frame into a directory that MALLET will be able to interpret as a text, and run a topic model on it. The rounding gives the resolution at which the topic will be run.

```
MALLEABLE = data.frame(text = data$voyageid, word = paste(round(data$lat, 1),
    round(data$long, 1), sep = "X"))
MALLEABLEpointRes = data.frame(text = data$voyageid, word = paste(round(data$lat),
    round(data$long), sep = "X"))
# I'm p system('mkdir /tmp/MALLET') system('mkdir /tmp/MALLETpointres')
# system('rm /tmp/MALLET/*')

# Write one text file for each voyage with all the points it passed
# through.
ddply(MALLEABLE, .(text), function(text) {
    write.table(text$word, paste("/tmp/MALLET/", text$text[1], ".txt", sep = ""),
        row.names = F, col.names = F, quote = F)
}, .progress = "text")

silent = ddply(MALLEABLEpointRes, .(text), function(text) {
    write.table(text$word, paste("/tmp/MALLETpointres/", text$text[1], ".txt",
        sep = ""), row.names = F, col.names = F, quote = F)
    return(data.frame())
}, .progress = "text")

# To get it to take number-and-comma formatted data, I need to change the
# token-regex; that was the only major hiccup I found here.
system("cd ~/mallet-2.0.7/; bin/mallet import-dir --input /tmp/MALLET --output ships.mallet --keep-sequence --token-regex \"\\S+\";")

system("cd ~/mallet-2.0.7/; bin/mallet import-dir --input /tmp/MALLETpointres --output shipsPointRes.mallet --keep-sequence --token-regex \"\\S+\";")

# I ran this several times with topic topic sizes; only including in the
# post 9 and 25
system("cd ~/mallet-2.0.7/; bin/mallet train-topics --input ships.mallet --output-topic-keys shipKeys.txt --num-topics 9 --output-doc-topics shipTopics.txt --output-state state.txt.gz;",
    ignore.stdout = T, ignore.stderr = T)

system("cd ~/mallet-2.0.7/; bin/mallet train-topics --input shipsPointRes.mallet --output-topic-keys shipKeys.txt --num-topics 9 --output-doc-topics shipTopics.txt --output-state 9pointres.txt.gz;",
    ignore.stdout = T, ignore.stderr = T)

system("cd ~/mallet-2.0.7/; gunzip -c -f 9pointres.txt.gz &gt; 9pointres.txt")

system("cd ~/mallet-2.0.7/; bin/mallet train-topics --input ships.mallet --output-topic-keys shipKeys.txt --num-topics 25 --output-doc-topics shipTopics.txt --output-state state.txt.gz;")

# This is the data I want to plot.
system("cd ~/mallet-2.0.7/; gunzip -c -f state.txt.gz &gt; 25topics.txt")

system("cd ~/mallet-2.0.7/; bin/mallet train-topics --input ships.mallet --output-topic-keys shipKeys.txt --num-topics 9 --output-doc-topics shipTopics.txt --output-state state.txt.gz;",
    ignore.stdout = T, ignore.stderr = T)

system("cd ~/mallet-2.0.7/; gunzip -c -f state.txt.gz &gt; 9topics.txt")
```

Read in those MALLET results and clean them up for analysis.

```
#Set the individual file to be plotted here. This should be wrapped into a function.
file = "25topics.txt"

malletresults = read.table(paste0('~/mallet-2.0.7/',file),sep=" ",col.names=c("?","file","loc","total","point","topic"),colClasses=c("NULL","character","NULL","NULL","character","integer"))
message("Working on a file that has ",length(unique(malletresults$topic))," topics")

tabbed = table(malletresults$point,malletresults$topic)

summarized = data.frame(tabbed)
summarized = summarized[summarized$Freq&gt;0,]

words =strsplit(as.character(summarized[,1]),'x')
f = t(sapply(words,as.numeric))

summarized$lat = f[,1]
summarized$long = f[,2]
summarized = summarized[,-1]
names(summarized)[1]="topic"

summarized$long[summarized$long&gt;180] = summarized$long[summarized$long&gt;180]-360

top = ddply(summarized,.(topic),function(locframe){
  returning = locframe[order(-locframe$Freq),][1:10,]
  returning$rank = 1:10
  returning
},.progress='text')

head(summarized)

baseplot = ggplot(summarized[as.numeric(summarized$topic)&gt;=0,],aes(x=long,y=lat)) +
  geom_tile(aes(alpha=Freq),width=1,height=1) +
  facet_wrap(~topic,ncol=round(sqrt(length(unique(summarized$topic))))) +
  annotation_map(map=world,fill='#F3E0BD') +
  theme_nothing+
  labs(title=paste0("Distribution of points across a ",length(unique(summarized$topic)),"-topic model\nTop ten points in each topic in red")) +
  scale_alpha_continuous("Number of ship-days\nassigned to topic\nwithin 1 degree",
    range=c(0,1),na.value=1,limits=c(0,50),breaks=c(0,10,20,30,40,50),labels=c(0,10,20,30,40,"50 or more")) +
  theme(legend.position="right")

baseplot  + labs(title=paste0("Distribution of points in the US Maury dataset across a ",length(unique(summarized$topic)),"-topic model")) + scale_x_continuous(expand=c(0,0))

baseplot + geom_point(data=top,color='red',size=5,alpha=.33)+ scale_x_continuous(expand=c(0,0))

baseplot %+% summarized[summarized$topic==4,]+ geom_point(data=top[top$topic==4,],color='red',size=5,alpha=.33)+ scale_x_continuous(expand=c(0,0)) + labs(title="Topic 4 in the 9-topic model")

}
```

Make some plots:

```
ggplot(plottable, aes(x = as.numeric(long), y = as.numeric(lat))) + geom_point(alpha = 0.1,
    size = 0.3) + facet_wrap(~topic, scales = "free", ncol = 4) + annotation_map(map = world,
    fill = "#F3E0BD") + theme_nothing + labs(title = "Distribution of points across a 25-topic model")
```

Try K-means clustering on the voyages in topic space (note: this did not work -– most ended up in a single k-means cluster –- so I did not include it in the blog post). This approach might work better with a higher number of topics, perhaps a couple hundred, but that would take better priors.

```
topicdists = table(malletresults$file, malletresults$topic)
head(topicdists)
topicdists = apply(topicdists, 2, function(z) {
    z/sum(z, na.rm = T)
})
class(topicdists) = "matrix"
f = kmeans(topicdists, centers = 9)
data$cluster = f$cluster[match(data$voyageid, names(f$cluster))]

offset = 220
plotWorld = Recenter(world, offset, idfield = "group")
plotData = Recenter(data, offset, shapeType = "segment", idfield = "voyageid")
head(plotData)
ggplot(plotData[!is.na(plotData$cluster), ], aes(x = as.numeric(long), y = as.numeric(lat))) +
    geom_path(aes(group = group), alpha = 0.02) + annotation_map(map = plotWorld,
    fill = "beige") + facet_wrap(~cluster, ncol = 3) + theme_nothing
```

### Topic Model evaluation with JSTOR and MALLET in R

This is Ben Schmidt’s R diagnostics for long-term historical topic modeling. It works off a MALLET state file.

Most of the work is done in custom functions: these are stored in the separate file “TopicModelVisualization.R” (which is printed at the end of this appendix).

```
opts_chunk$set(warning = FALSE, error = FALSE, message = FALSE, results = "show",
    cache = TRUE, eval = FALSE)
require(plyr)

## Loading required package: plyr
require(ggplot2)
## Loading required package: ggplot2
require(reshape2)
## Loading required package: reshape2
source("TopicModelVisualization.R")
```

The first step is to load the MALLET file with a function to do so.

```
loadMalletFile
topics = loadMalletFile(fileLocation = "../topic-state")
```

This is code I borrowed from Andrew Goldstone to match the metadata from JSTOR against the topics. If you are not using JSTOR, you would just need to

1. create a ‘year’ column in the topics frame
2. (optionally) create a files frame with other metadata (title, author, and so forth), indexed so that files$numid maps to topics$doc.

```
# An id can be a string('numid') or a character('id'); I'm just trying to
# get them aligned
ids = readInIDs(readOrderFile = "../readOrder.txt")

# refactor the topics with the filenames: not doing this because factors
# are slooooooow. topics$doc =
# factor(topics$doc,levels=ids$numid,labels=ids$id)

files = readInMetadata("../citations_all.csv")
files$numid = ids$numid[match(files$id, ids$id)]
# match is fast than merge, and will only work once.
topics$year = files$year[match(topics$doc, files$numid)]
topics = topics[!is.na(topics$year), ]  #eliminates duplicates, among other things.
dim(topics)
```

And finally, topics conventionally have names, not numbers. Here we derive those as the top seven words in each topic.

```
topics = labelTopics(topics)
```

OK, now to look for weirdness.  
 Plow through all the topics and run that function to extract out various data about them. The exact metrics I use are documented inside the code for the previous function

```
topics = idata.frame(topics)
diagnostics = dlply(topics, .(topic), topicBeforeAndAfterSplit, .progress = "none")

unimeasures = ldply(diagnostics, function(list) {
    data.frame(topCor = list$topCor, tenCor = list$tenCor, unlikelihood = list$unlikelihood,
        perToken = list$unlikelihoodPerToken)
})
```

Plot some of the worst ones. This will not work with other models, perhaps. The whole block can be skipped, though.

```
allTopics = unimeasures$topic[order(unimeasures$tenCor)]

# Dropping ones that start with fewer than four letter words clears out
# language topics, which are overwhelming. It probably clears out a few
# other ones, too, though.

source("TopicModelVisualization.R")
EnglishTopics = allTopics[grep("^\\w\\w\\w\\w", allTopics)]
goodTopics = rev(EnglishTopics)[1:12]
badTopics = EnglishTopics[1:12]
twain = EnglishTopics[grep("twain", EnglishTopics)]
set.seed(80)  #So the random topics will always be the same ones
randomTopics = sample(EnglishTopics, 12)

diagnosticPlot(badTopics)
diagnosticPlot(randomTopics) + labs(title = "A random set of 12 topics is better, but still shows some change")
diagnosticPlot(twain) + labs(title = "The 'Grant State Twain' topic breaks in two\nwhen bisected across time")
```

Here’s a function to plot the usage of a word across its top five topics.

```
wordDist = function(word) {
    # This requires topics to exist as a frame word can be a vector of any
    # length
    wordframe = as.data.frame(topics[topics$word %in% word, ])
    wordframe = wordframe[wordframe$topic %in% names(head(sort(-table(wordframe$topic)),
        5)), ]
    wordframe$topic = factor(wordframe$topic)
    tabbed = table(round(as.numeric(as.character(wordframe$year)), -1), wordframe$topic)
    yearvalues = melt(tabbed)
    names(yearvalues) = c("year", "topic", "count")
    yearvalues$year = as.numeric(as.character(yearvalues$year))
    require(ggplot2)
    ggplot(yearvalues) + geom_line(aes(x = year, y = count, color = topic)) +
        labs(title = paste0("Usage of ", paste(word, collapse = "/"), " across different topics")) +
        theme(legend.position = "bottom")
}
```

For example:

```
wordDist(c("represent", "represents", "represented", "representing"))
wordDist(c("mimesis", "mimetic"))
```

### Code to parse MALLET/JSTOR results in R

This is the block of functions used to parse mallet/JSTOR results.

```
loadMalletFile = function(fileLocation = "../topic-state") {
  #Loads a mallet file, keeping only the doc, word, and topic variables
  read.table(
    file=fileLocation,
    colClasses=c("integer","NULL","NULL","NULL","character","integer"),
    comment.char="#",col.names=c("doc","NA","NA2","NA3","word","topic"))
  #You might want
}

readInIDs = function(readOrderFile = "../readOrder.txt") {
  #I previously created a script with the order files were read in using "readOrder.txt"
  ids = read.table("../readOrder.txt",col.names="filename")
  ids$numid = 0:(nrow(ids)-1) #This is the id that
  ids$id = gsub("_","/",gsub("\\.[[:alpha:]]*$","",gsub("^.*wordcounts_","",ids$filename))) #Just some particularities to make filenames match up with JSTOR identifiers. I believe Goldstone must have written at least some of this, based on the regex style.
  ids
}

readInMetadata = function(citationsFile) {
  #These are scripts of Andrew Goldstone's to parse JSTOR metadata.
  #Andrew Goldstone's script to parse jstor metadata
  source("metadata.R")
  files = read.citations("../citations_all.csv")
  files$year = as.numeric(substr(files$pubdate,1,4))
  files$filename
  files
}

labelTopics = function(topics) {
  message("Labelling topics: this may take a while")
  smallerFrame = idata.frame(topics[,c("topic","word")])
  topicNames = dlply(
    smallerFrame,
    .(topic),
    function(locframe) {
      paste(names(sort(-table(locframe$word)))[1:7],collapse=' ')
    },
    .progress='text')

  message("")
  if (sum(duplicated(topicNames))&gt;0) {
    warning("Two topics have the same top 7 words. Yikes! Time to rethink the labeling scheme, just leaving it as integers for now.")} else {
      topics$topic = factor(topics$topic,levels = as.numeric(names(topicNames)),labels=unlist(topicNames))
    }
  topics
}

topicBeforeAndAfterSplit = function(thisTopic=topics[topics$topic ==sample(levels(topics$topic),1),]) {
  #allowing multiple bin sizes, just in case.
  bins=2
  thisTopic$era = cut(thisTopic$year,breaks=quantile(thisTopic$year,na.rm=T,probs=seq(0,1,length.out=bins+1)),include.lowest=T,labels=paste("From",quantile(thisTopic$year,na.rm=T,probs=seq(0,1,length.out=bins+1))[-(bins+1)],'to',quantile(thisTopic$year,na.rm=T,probs=seq(0,1,length.out=bins+1))[-1]))
  tabbed = table(thisTopic$word,thisTopic$era)
  tabbed = tabbed[order(-rowSums(tabbed)),]
  class(tabbed)='matrix'

  #For log-likelihood purposes, consider any non-appearances to be half-appearances.
  tabbed[tabbed==0] = .5

  #An implementation of Dunning Log-Likelihood
  llr = function(k) { 2 * (llr.H(k) - llr.H(rowSums(k)) - llr.H(colSums(k)) ) }
  llr.H = function(k) { total = sum(k) ; sum( k * log(k / total)) }

  tabbed = cbind(tabbed,round(apply(tabbed, 1, function(row) {
    k = rbind(row, colSums(tabbed))
    2 * (llr.H(k) - llr.H(rowSums(k)) - llr.H(colSums(k))) * (as.numeric(row[1]&gt;row[2])*2-1)
  }),3))

  #A grabbag of outputs to look at. Most of these were not used: some might be worth using.
  output = list(
    #all words with their frequencies in each of the year bins
    allWords = tabbed,
    #the name of the topic
    topic = as.character(thisTopic$topic[1]),
    #the number of words in the topic
    size = nrow(thisTopic),
    #the mean Dunning-log-likelihood across all words in the set: higher
    #means more unlikely
    unlikelihood = mean(abs(tabbed[,3])),
    #A per-token normalizetion of the Dunning score.
    unlikelihoodPerToken = mean(abs(tabbed[,3]))/nrow(thisTopic),
    #correlation of word counts from group 1 to group 2, log distribution
    overallCorrelation = cor(log(tabbed[,1]),log(tabbed[,2])),
    #the 100 words with the worst Dunning score in either direction
    worstWords =tabbed[order(-abs(tabbed[,3])),][1:100,],
    #the 100 commonest words
    commonestWords = tabbed[1:100,],
    #the 100 commonest words in time group A and B
    topA = rownames(tabbed)[order(-tabbed[,1])][1:100],
    topB = rownames(tabbed)[order(-tabbed[,2])][1:100],
    #just the words with no data
    topOverall = rownames(tabbed)[order(-rowSums(tabbed[,1:2]))][1:100]
    )
  #The intergroup correlation for the most common words, log distribution
  output$topCor = cor(log(output$commonestWords[1:100,1]),log(output$commonestWords[1:100,2]))
  #The intergroup correlation for the very most common words.
  output$tenCor = cor(log(output$commonestWords[1:10,1]),log(output$commonestWords[1:10,2]))
  return(output)
}

#### Visualization Functions

#From stackOverflow
reverselog_trans 0] = "rising"
  plottable$trend[plottable$change==0] = "steady"
  plottable$trend[plottable$change&lt;0] = "falling"
  plottable
}

diagnosticPlot = function(topicSet) {
  plottable = makePlottable(topicSet)

  ggplot(plottable,aes(x=Period,y=count,label=paste0(count,'. ',word))) +
    geom_text(size=3.5) +
    geom_path(aes(size=abs(change),color=trend,group=word),alpha=.33) +
    facet_wrap(~topic,scales='free',nrow=3) +
    labs(title =
    "Splitting in half by year shows two very different vocabularies\n(showing the top 20 words overall in the 12 worst English language topics)") +
    scale_y_continuous("Rank of word among corpus's top 100 words",trans='reverselog',breaks=outer(c(1,2,5),c(1,10,100,1000))) +
    scale_color_discrete("Direction of change") +
    scale_size_continuous("Fall\n(or Increase)\nin rank\nwithin topic",labels=exp,breaks=log(c(.0001,1,10,100,1000)))
  }

alternativeTrack = function(words) {

  wordlist = unlist(strsplit(sample(levels(topics$topic),1),' '))
  wordlist = c("shelley","keats","wordsworth","romantic","romanticisms","ballade")
  justTheseWords = data.frame(topics[topics$word %in% wordlist,])
  justTheseWords$year = floor(justTheseWords$year/5)*5
  plottable = ddply(justTheseWords,.(word),function(wordframe) {
    ddply(wordframe,.(year),function(yearframe){
      data.frame(index=(nrow(yearframe)/nrow(wordframe))*length(unique(wordframe$year))
    )})
  })
  ggplot(plottable,aes(x=floor(year/5)*5,y=index)) + stat_summary(fun.y=median,geom='point',size=4) + geom_line(aes(color=word))
}
```
