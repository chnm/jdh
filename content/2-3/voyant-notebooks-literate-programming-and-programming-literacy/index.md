+++
title = "Voyant Notebooks: Literate Programming and Programming Literacy"
slug = "voyant-notebooks-literate-programming-and-programming-literacy"
type = "article"
date = 2013-06-01
issue = "2-3"
volume = 2
number = 3
season = "Summer"
year = 2013
section = "DH 2013 Poster Gallery"
section_url = "/category/2-3/gallery-2-3/"
section_weight = 3
weight = 5
authors = ["Stéfan Sinclair", "Geoffrey Rockwell"]
author_ids = ["ssinclair", "grockwell"]
author = ["ssinclair", "grockwell"]
+++

### Poster

<iframe class="gde-frame" scrolling="no" src="https://docs.google.com/viewer?url=http%3A%2F%2Fjournalofdigitalhumanities.org%2Fwp-content%2Fuploads%2F2013%2F11%2FVoyant-Notebooks-Sinclair-and-Rockwell.pdf&amp;hl=en_US&amp;embedded=true" style="width:100%; height:500px; border: none;"></iframe>

[Download (PDF, 676KB)](https://journalofdigitalhumanities.org/wp-content/uploads/2013/11/Voyant-Notebooks-Sinclair-and-Rockwell.pdf)

### Abstract

Some thirty years ago Donald Knuth, a computer scientist, proposed literate programming as a better way of organizing narrative and code (1984). Knuth argued that more emphasis should be placed on explaining to humans what computers are meant to do, rather than simply instructing computers what to do. Knuth was especially interested in weaving together macrostyle code snippets with prose that provided a larger narrative context, not merely functional comments of specific lines of code that are the distilled remnants of an intellectual process.

Literate programming has been more influential in theory than in practice (Nørmark), despite several utilities and environments including Mathematica, Knuth’s (C)WEB, Sweave for R, and Marginalia for Clojure. Perhaps the exigencies of programming in the real world correspond poorly with the vision of Knuth of the programmer as author: “the practitioner of literate programming can be regarded as an essayist, whose main concern is with exposition and excellence of style” (1992, 1). However, that balance of essayist and coder strikes us as perfectly appropriate for the digital humanities, a natural blend of the expression of intellectual process with the exposition of technical methodologies. The prose can gloss the code, or vice versa, in a symbiotic relationship that serves to strengthen an argument and demonstrate its own workings.

One of the most significant potential benefits of the literate programming paradigm is pedagogical: these works can both explain an interpretive insight and present the methodology for reproducing the data or results that were part of the process. Many widely-read digital humanities blogs already present these characteristics of exploration, explanation, interpretation, and step-by-step instructions (see for example blogs by [Ted Underwood](http://tedunderwood.com/ "Ted Underwood, The Stone and the Shell"), [Benjamin Schmidt](http://sappingattention.blogspot.com/ "Ben Schmidt, Sapping Attention"), [Lisa Rhody](http://www.lisarhody.com/ "Lisa Rhody, Lisa@Work") and [Scott Weingart](http://www.scottbot.net/HIAL/ "Scott Weingart, scottbot.net")). Literate programming can be more self-contained and more useful for those learning new methodologies and new programming techniques. This is about the principles of literate programming, but also about the potential for increasing programming literacy.

This poster will introduce Voyant Notebooks, a web-based literate programming environment designed for the digital humanities (see Appendix A). There is already a working prototype, and we anticipate having a more feature-rich version available by July 2013. Voyant Notebooks inherits many of the characteristics of the Voyant Tools environment, including a concern for usability and flexibility (researchers and students should be able to use it with minimal or no training and with their own texts of interest). Voyant Notebooks also addresses one of the main weaknesses of Voyant Tools: the fact that most tools are constrained by assumptions about how they would be most commonly used. For instance, the Wordle-like (word cloud) Cirrus tool is designed to show the top frequency terms from a corpus or document; but what if the user instead wants to visualize the top frequency nouns, or people, or repeating phrases? All of that functionality could be built into the tool, but possibly at the cost of usability (endless menus and options), and it could still never address all of the possible use cases. Voyant Notebooks, by contrast, empowers the user to customize some of the functionality by leveraging the analytic capabilities of the Voyant back-end and the visualization interfaces in the front-end (like Cirrus). Our poster will have two parts, a) a usable demonstration on one or more laptops and b) a poster that illustrates how Voyant Notebooks implements Knuth’s concept of literate programming. In addition to these conceptual aspects, the poster will outline technical details about the Voyant Notebooks prototype for those interested, including the technologies used for both client-side (browser) and server-side components. Some of the technical challenges that will be described include:

- managing the flow of code execution in an asynchronous architecture
- using web workers to avoid browser freezes during longer executions
- mitigating the security risks of user-defined and persistent Javascript code
- code variable scoping across editor instances and window components
- embedding of Voyant tool panels (visualizations) and other services
- developing a flexible API for different programming levels and styles
- developing an API that includes both client-side and server-side operations
- ensuring efficiency of repeated code snippets during writing and viewing

And of course, visitors to the poster session will be warmly encouraged to play with Voyant Notebooks.

### Appendix A: Mockup of Voyant Notebooks (previously called Voyeur Notebooks).

<div class="wp-caption aligncenter" id="attachment_5984" style="width: 310px"><a href="https://journalofdigitalhumanities.org/wp-content/uploads/2013/11/Voyant-Notebooks-Appendix-A.png" target="_blank"><img alt="Voyant Notebooks-Appendix A" aria-describedby="caption-attachment-5984" class="size-medium wp-image-5984" height="292" src="https://journalofdigitalhumanities.org/wp-content/uploads/2013/11/Voyant-Notebooks-Appendix-A-300x292.png" title="Sinclair and Rockwell, Voyant Notebooks Appendix A" width="300"/></a><p class="wp-caption-text" id="caption-attachment-5984">Figure 1: Mockup of Voyant Notebooks</p></div>

Originally presented by Stéfan Sinclair and Geoffrey Rockwell at DH2013 on [July 17, 2013](http://dh2013.unl.edu/abstracts/ab-295.html "Abstracts DH2013").

### References

Knuth, D. (1984). Literate Programming. _The Computer Journal_ 27(2): 97-111, 1.

Knuth, D. (1992). Literate Programming. Stanford University Center for the Study of Language and Information.

Nørmark, K. (1998). Literate Programming: Issues and Problems. [http://www.cs.aau.dk/~normark/litpro/issues-and-problems.html](http://www.cs.aau.dk/~normark/litpro/issues-and-problems.html "Nørmark, K. 'Literate Programming: Issues and Problems.'").

Sinclair, S. and G. Rockwell (2012). Teaching Computer-Assisted Text Analysis: Approaches to Learning New Methodologies. in _Digital Humanities Pedagogy_. Open Book Publishers.
