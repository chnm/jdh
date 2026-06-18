+++
title = "Modelling the Interpretation of Literary Allusion with Machine Learning Techniques"
slug = "modelling-the-interpretation-of-literary-allusion-with-machine-learning-techniques"
type = "article"
date = 2014-03-01
issue = "3-1"
volume = 3
number = 1
season = "Spring"
year = 2014
section = "DH2013 Poster Gallery"
section_url = "/category/3-1/gallery-3-1/"
section_weight = 4
weight = 2
authors = ["Neil Coffee", "James Gawley", "Christopher Forstall", "Walter Scheirer", "David Johnson", "Jason Corso", "Brian Parks"]
author_ids = ["neil-coffee", "james-gawley", "christopher-forstall", "walter-scheirer", "david-johnson", "jason-corso", "brian-parks"]
author = ["neil-coffee", "james-gawley", "christopher-forstall", "walter-scheirer", "david-johnson", "jason-corso", "brian-parks"]
+++

### Poster

<iframe class="gde-frame" scrolling="no" src="https://docs.google.com/viewer?url=http%3A%2F%2Fjournalofdigitalhumanities.org%2Fwp-content%2Fuploads%2F2014%2F01%2Fscheirer_dh_2013-1.pdf&amp;hl=en_US&amp;embedded=true" style="width:100%; height:500px; border: none;"></iframe>

[Download (PDF, 3.5MB)](https://journalofdigitalhumanities.org/wp-content/uploads/2014/01/scheirer_dh_2013-1.pdf)

### Abstract

#### A Computational Perspective on Allusion

Most literary allusion, the deliberate evocation by one text of a passage in another, is based upon text reuse. Yet most instances of textual similarity are not meaningful literary allusions. The goal of the [Tesserae](http://tesserae.caset.buffalo.edu "Tesserae Home") project is to automatically detect allusion in a corpus of literary texts, primarily Classical Latin poetry. We begin with a large set of textual parallels, and then attempt to model which of these instances of text reuse are meaningful literary allusions and which are not, according to a group of human readers. While initial attempts with a few basic textual features have proven surprisingly effective, here we employ a more complex feature set and machine learning techniques drawn from the field of computer vision in an attempt to improve the results. Novel applications of machine learning, beyond the well known but constrained textual classification tasks of attribution and categorization, have the potential to be transformative for complex analysis tasks in the Digital Humanities.

#### Benchmark Data

As an illustration, we consider textual parallels between Book 1 of Lucan’s _Bellum Civile_ and the entirety of Vergil’s _Aeneid_.[^1] Our benchmark dataset comprises a list of 3,400 pairs of sentences that share at least two different words. Each of these pairs has been read and graded for its literary significance by a group of students and faculty working in small teams. These annotator rankings range from 1 (no literary significance) to 5 (pointed literary allusion).

#### Learning Relevant Features

Earlier work showed that high-ranked parallels could be distinguished from the others with modest accuracy using only word frequency, distance between words, and the presence of exact form matching versus differently-inflected forms of the same word.[^2] Nevertheless, others have recommended more sophisticated approaches to this problem.[^3] Here we consider an expanded feature set including bi-gram frequency, frequency of individual words, character-level n-grams and edit distances. Our goal is to learn relevant combinations of features in the presence of often incomplete data.

Recent work by members of our team has developed new methods for tuning machine-learning using support vector machines[^4] and random forests.[^5] Random forest is of particular interest, providing robust feature selection that shows promise for literary analysis.[^6] The problem of missing data is prevalent in all areas of literary study, but is not well addressed by existing algorithms in common use by digital humanists. This is especially true for ancient texts, where we often find a significant gap in the manuscript tradition. Using principled strategies for imputation and marginalization, we reduce the impact on the results.

### Results and Implications

Our ability to learn the difference between high-ranked parallels (ranks 4 & 5) and low-ranked parallels (ranks 1 & 2) for _Bellum Civile_ and the _Aeneid_ is strong: random forest achieves an average AUC score between 82% and 83%, while linear SVMs yield an average score of 81.5%. This suggests that quantifiable patterns do exist across allusions, which can be captured algorithmically. In this ongoing research we seek a more successful model of literary significance that will allow our software to put interesting allusions at the top of the list; at the same time, we hope it will also cast new light on the underlying structures of our experience of literature.

**An interactive demonstration of the Tesserae allusion detection tool accompanied this poster.**

The poster was originally presented at DH2013 on [July 17, 2013](http://dh2013.unl.edu/abstracts/ab-177.html "Abstracts DH2013").

[^1]: N. Coffee, J.P. Koenig, S. Poornima, C.W. Forstall, R. Ossewaarde, and S. Jacobson. “Intertextuality in the Digital Age.” _Transactions of the American Philological Association_, 142(2), 2012.

[^2]: J. Gawley, C.W. Forstall, and N. Coffee. “Evaluating the Literary Significance of Text Re-use in Latin Poetry.” Poster presented at Chicago Colloquium on Digital Humanities and Computer Science, University of Chicago, Chicago, IL. November 17-19, 2012.

[^3]: D. Bamman and G. Crane. “The Logic and Discovery of Textual Allusion.” Language Technology for Cultural Heritage Data Conference, 2008.

[^4]: W.J. Scheirer, A. Rocha, J. Parris, and T.E. Boult. “Learning for Meta-Recognition.” _Institute of Electrical and Electronics Engineers- Transactions on Information Forensics and Security,_ X(Y), March, 2012.

[^5]: C. Xiong, D. Johnson, R. Xu, and J. J. Corso. “Random Forests for Metric Learning with Implicit Pairwise Position Dependence” Association for Computing Machinery Special Interest Group on Knowledge, Discovery and Data Mining Conference, 2012.

[^6]: T. Tabata. “Approaching Dickens’ Style Through Random Forests. _DH2012_, 2012.
