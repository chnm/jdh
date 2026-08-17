+++
title = "Review of Bookworm, produced by Benjamin Schmidt, Martin Camacho, et al."
slug = "bookworm"
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
weight = 2
authors = ["Boone B. Gorges"]
author_ids = ["bgorges"]
author = ["bgorges"]
+++

[Bookworm](http://bookworm.culturomics.org "Bookworm") is a tool that allows users to create visualizations charting the use of words or phrases in selected large corpora over specified periods of time. The software was developed by a group of researchers at the [Harvard University Cultural Observatory](http://www.culturomics.org/cultural-observatory-at-harvard "Culturomics, the Cultural Observatory at Harvard") [^1] as a follow-up to the 2010 project that resulted in [a cover story in _Science_](http://www.sciencemag.org/content/early/2010/12/15/science.1199644 "Michel Jean-Baptiste, et al. 'Quantitative Analysis of Culture Using Millions of Digitized Books'"), the [Google Books Ngram Viewer](http://books.google.com/ngrams "GoogleBooks, Ngram Viewer"), and the coining of the term [‘culturomics’](https://en.wikipedia.org/wiki/Culturomics "Wikipedia entry, 'Culturomics'"). Bookworm development is still in its alpha phase, but already the software shows great promise as a tool for scholarly exploration of historical trends in large collections of books.

The purpose of Bookworm is to track the frequency with which a phrase is used over a certain time span, within user-defined subsets of Bookworm’s total book collection. Users can carve out subcollections in a number of different ways: by geography (where the book was published), language, Library of Congress classification, and date (publication date, date of authorship, birthdate of author). These criteria can be combined, and compared against each other, to nice effect. For example, we can compare the frequency of the name ‘Simon Cameron’ as it appears in all books, versus all books published in Pennsylvania, versus Pennsylvanian books under the subject heading “History of the Americas”:

<div class="wp-caption aligncenter" id="attachment_253" style="width: 1411px"><a href="/wp-content/uploads/2012/03/ss1.jpg" target="_blank" title='Frequency of "Simon Cameron" in books with “History of the Americas” subject heading.'><img alt='Frequency of "Simon Cameron" in books with “History of the Americas” subject heading.' aria-describedby="caption-attachment-253" class="wp-image-253" height="594" src="/wp-content/uploads/2012/03/ss1.jpg" title='Frequency of "Simon Cameron" in books with “History of the Americas” subject heading.' width="1401"/></a><p class="wp-caption-text" id="caption-attachment-253">Frequency of “Simon Cameron” in books with “History of the Americas” subject heading.</p></div>

The results are, in this case, predictable: Cameron’s name appears more frequently in publications from his home state, with peaks in the decade or so after the Civil War. But this rather mundane example gestures toward the potential for richer exploratory searches across custom-defined subcollections of Bookworm’s index.

Similarly, we can compare the frequency of different phrases across a single corpus. For instance, the phrase ‘Simon Cameron’ is (again, unsurprisingly) more frequent in Pennsylvania books than ‘Gideon Welles’:

<div class="wp-caption aligncenter" id="attachment_250" style="width: 1324px"><a href="/wp-content/uploads/2012/03/ss2.jpg" target="_blank" title='Frequency of "Simon Cameron" and "Gideon Welles" in books published in Pennsylvania with "History of the Americas" subject heading'><img alt='Frequency of "Simon Cameron" and "Gideon Welles" in books published in Pennsylvania with "History of the Americas" subject heading' aria-describedby="caption-attachment-250" class="wp-image-250" height="601" src="/wp-content/uploads/2012/03/ss2.jpg" title='Frequency of "Simon Cameron" and "Gideon Welles" in books published in Pennsylvania with "History of the Americas" subject heading' width="1314"/></a><p class="wp-caption-text" id="caption-attachment-250">Frequency of “Simon Cameron” and “Gideon Welles” in books published in Pennsylvania with “History of the Americas” subject heading</p></div>

The power of a tool designed for the exploration of a specific corpus is, in large part, dependent on the size and quality of that corpus. Bookworm’s index is based on the public domain works available through [Open Library](http://openlibrary.org/ "Home page of Open Library"), which numbers nearly one million books. The public domain limitation is notable for a few reasons. For one thing, it means that Bookworm’s corpus is more limited than that of the Google Books project, both in terms of sheer size (the original _Science_ paper cites a corpus of over five million books) and in terms of usable date ranges (most US public domain works come from before 1922, the horizon for most works under current US copyright law). At the same time, limiting the collection to public domain works means that Bookworm can link to the full text of query results:

<div class="wp-caption aligncenter" id="attachment_251" style="width: 714px"><a href="/wp-content/uploads/2012/03/ss3.jpg" target="_blank" title="Books for series Simon Cameron matching constraints in 1883"><img alt="Books for series Simon Cameron matching constraints in 1883" aria-describedby="caption-attachment-251" class="wp-image-251" height="243" src="/wp-content/uploads/2012/03/ss3.jpg" title="Books for series Simon Cameron matching constraints in 1883" width="704"/></a><p class="wp-caption-text" id="caption-attachment-251">Books for series Simon Cameron matching constraints in 1883</p></div>

In this way, Bookworm provides a link (both figurative and literal) between the very distant reading of macro-level quantitative analysis, and the close reading of specific texts that is crucial to contextualizing the qualitative results.

Setting aside limitations imposed by what copyright law _excludes_ from the corpus, some of Bookworm’s notable limitations come from the weaknesses of the texts that _are_ in the collection. The OCR (optical character recognition) process used to scan the books is imperfect. As a simple example, the frequency of a non-word like ‘hiftory’ (for ‘history’) shows that the software has a hard time distinguishing characters like the medial ‘s’. And the metadata used by Open Library (and thus by Bookworm) to categorize and filter collections is, in places, incomplete or incorrect. Scholars should take heart, however, that Open Library’s metadata is publicly modifiable: users can add or edit a book’s info, which Bookworm – and any other tool using Open Library data – will recognize the next time it refreshes its index.

The team behind Bookworm is at work on numerous improvements. Publicly available installations of Bookworm are being developed to track other large corpora; [Bookworm arXiv](http://arxiv.culturomics.org/ "Culturomics, 'Bookworm arXiv'"), just announced, draws from the scientific papers of [arXiv.org](http://arxiv.org/ "arXiv, an e-print service in the fields of physics, mathematics, non-linear science, computer science, quantitative biology, quantitative finance and statistics"). The development team is [particularly interested](http://blogs.law.harvard.edu/dplaalpha/2011/10/14/interview-with-ben-schmidt-and-martin-camacho-of-bookworm/ "Kenny Whitebloom, 'Interview with Ben Schmidt and Martin Camacho of Bookworm'") in conceptualizing Bookworm as an interface for browsing library catalogs. And perhaps most exciting is the prospect of an eventual general release of the software – including the visualization interface as well as the server-side tools necessary for indexing arbitrary collections of text – under a free software license.[^2] Such a release would allow individual scholars or other organizations to host their own Bookworm instances, connected to whatever arcana they see fit. This would be a most welcome addition to the existing library of tools for macro text analysis.

Even in this early incarnation, Bookworm is an easy-to-use and powerful way for interested parties to get started with quantitative analysis of a large and important corpus of works in the public domain.

[^1]: Ben Schmidt, Martin Camacho, Neva Cherniavsky, Erez Lieberman Aiden, and Jean-Baptiste Michel.

[^2]: This possibility was conveyed to me by developer Ben Schmidt in an email exchange.
