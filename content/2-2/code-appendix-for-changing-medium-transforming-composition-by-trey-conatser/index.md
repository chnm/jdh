+++
title = "Code Appendix for “Changing Medium, Transforming Composition”"
slug = "code-appendix-for-changing-medium-transforming-composition-by-trey-conatser"
type = "article"
date = 2013-03-01
issue = "2-2"
volume = 2
number = 2
season = "Spring"
year = 2013
section = "Explorations"
section_url = "/category/2-2/explorations-2-2/"
section_weight = 2
weight = 2
authors = ["Trey Conatser"]
author_ids = ["tconatser"]
author = ["tconatser"]
+++

### Appendix A: Selections from Major Assignment Markup Schemes

#### _Primary Source Analysis_

- In at least one paragraph match evidence (details) from the primary source with the interpretations you draw from them:

> `<seg type="ev_interp">`

> `<seg type="evidence">evidence (details) from the primary source</seg>`

> `<seg type="interpretation">interpretation based on corresponding evidence</seg>`

> `</seg>`

- Tag all research questions at the end of the PSA with unique  xml:id  identifiers:

> `<seg type="research_question" xml:id="surname_rq_#">research question</seg>`

- Tag a moment of the PSA when you complicate the seemingly obvious:

> `<seg type="complication">text here</seg>`

- Tag at least one exact repetition that you find in the primary source:

> `<seg type="pattern">text here</seg>`

- Tag a moment of the PSA when you identify a strand: a pattern of approximate (not exact) repetition:

> `<seg type="strand">text here</seg>`

- Define one binary—an  organizing contrast —that you are identifying in or from the primary source:

> `<seg type="binary_a">text here</seg>
> `

> `<seg type="binary_b">text here</seg>`

- Tag an anomaly in the primary source as well as your explanation of the significance of that anomaly:

> `<seg type="anomaly">text here</seg>`

> `<seg type="anomaly_sig">text here</seg>`

#### _Annotated Bibliography_

- Markup structure for each annotated bibliography entry; possible type attributes are “book” for a consistently authored book, “chapter” for a separately authored chapter in a collection or anthology of separately authored chapters in a book, “pr_article” for a scholarly, peer reviewed article from an academic journal, “np_article” for a newspaper article, “m_article” for a magazine article, “o_article” for other article types:

> `<bibl type="type_here" xml:id="id_here" n="alphabetical_organizer"> MLA Works Cited Entry `

> `<note type="ab_annotation" corresp="xml:id_of_corresponding_research_question"> Annotation here.</note>`

> `</bibl>`

- Professional status of author or authors for each entry:

> `<seg type="author">text here</seg>`

- Main argument for each entry:

> `<seg type="main_argument">text here</seg>`

- Relevance of each entry to your primary source, primary source analysis, and/or research questions:

> `<seg type="relevance">text here</seg>`

#### _Secondary Source Integration_

- Tag in your introduction and/or conclusion your preliminary thesis, however vague it may be. Tag each part of the thesis within the overall thesis tag; see the _Writing Analytically_ sections on incorporating tension and complexity into your thesis:

> `<seg type="thesis">`

> `<seg type="thesis_part">text here</seg>`

> `<seg type="thesis_part">text here</seg>`

> `</seg>`

- Tag the sequence or line of thought when you cite a secondary source to extend your line of thought:

> `<seg type="integrating_sources">`

> `<seg type="me">your initial insight about the primary source</seg>`

> `<seg type="source">citation/integration of related insight(s) from a secondary source</seg>`

> `<seg type="synthesis">your new, clarified, qualified, or modified insight(s)</seg>`

> `</seg>`

#### _Analytical Research Paper_

- Tag your thesis whenever it occurs in your ARP, as many times as it evolves. Tag each part of the thesis within the overall thesis tag; see the _Writing Analytically_ sections on incorporating tension and complexity into your thesis:

> `<seg type="thesis">`

> `<seg type="thesis_part">text here</seg>`

> `<seg type="thesis_part">text here</seg>`

> `</seg>`

- Tag whenever you explore the significance of the primary source’s audience:

> `<seg type="audience">text here</seg>`

- Tag whenever you explore the significance of the primary source’s medium:

> `<seg type="medium">text here</seg>`

- Tag whenever you explore the significance of the primary source’s author(s), creator(s), host(s), sponsor(s), etc.:

> `<seg type="author">text here</seg>`

- At least twice tag an insight that you then explore in terms of its significance—in other words, following the  _so what?_  question—repeat the <seg type=”so_what”> as many times as necessary, assigning the same value for the  corresp  attribute linking all  so what?  explorations back to the same original insight:

> `<seg type="insight" xml:id="lastname_insight_#">text here</seg>`

> `<seg type="so_what" corresp="lastname_insight_#">text here</seg>`

### Appendix B: Example Primary Source Analysis with Markup[^1]

```
<div type="primary_source_analysis" n="1" xml:id="psa_example_1">
<head type="student_name" n="1">J. Q. Student</head>
<head type="instructor_name" n="2">Trey Conatser</head>
<head type="class" n="3">English 1110.01</head>
<head type="date" n="4">04 February 2012</head>
<head type="paper_title" n="5">Primary Source Analysis</head>
<p>
<seg type="introduction">
Robert and Shana ParkeHarrison’s <title level="a">Summer Arm</title>, a mixed media (though mostly photographic)
piece in their <title level="m">Counterpoint</title> series, presents us with a mechanical apparatus holding the
outstretched arm of a man whose body for the most part lies beyond the frame.
<seg type="pattern">
Atop the arm grow three clusters of plants, including Black-eyed Susans, a Tiger Lily, and small fern stalks.
</seg>
<seg type="pattern">
Four butterflies of varying colors and an insect of an uncertain type fly around the flowers in front of the flat, off-white background.
</seg>
<seg type="thesis">
<seg type="thesis_part">
<title level="a">Summer Arm</title> therefore consists both compositionally and conceptually of
three major parts: the mechanical, the human, and the natural, a triad that the ParkeHarrisons have
made the focus of most, if not all of their work.
</seg>
<seg type="thesis_part">
In addition to raising questions about the nature of each of these parts, <title level="a">Summer
Arm</title> leads us to reconsider how much they feed into or push back against each other.
</seg>
</seg>
</seg>
</p>
<p>
The apparatus occupies roughly the bottom fourth of the image.
<seg type="ev_interp">
<seg type="evidence">
Hard right angles and sickle-like curves convey a harshness and coldness matched by the silver and
black of the skeletal pieces. Though obviously mechanical, the device also appears to have been assembled
idiosyncratically;
<seg type="pattern">
the irregular knobs, connectors, and sections
</seg>
may very well have been scrounged from a scrap pile.
</seg>
<seg type="interpretation">
At best, therefore, the apparatus suggests a moral ambivalence; while it unavoidably points to the impersonal,
mass fabrication of modern industry, it also represents a creative recycling of available resources, the
castoff detritus from the engines of consumption and waste.
</seg>
</seg>
<seg type="ev_interp">
<seg type="interpretation">
Moreover, the device both threatens and supports the man’s arm.
</seg>
<seg type="evidence">
Rods taper to needle-like points uncomfortably close to the man’s flesh, and a circular component just above
the elbow seems to function as a clamp holding the arm in place: a buttress, or, conversely, a restraint.
</seg>
</seg>
</p>
<p>
Thus, we question whether the man himself constructed the apparatus or if he simply was placed in it. His upturned
arm appears hyperextended, and his shirtsleeve has been rolled back; overall, the body’s position recalls the act
of giving blood or having a blood sample taken, in both cases the loss of vivifying, essential fluid. Furthermore,
the man’s head bolsters the appearance of exhaustion.
<seg type="anomaly">
Though we see only the very top of his head, it clearly tilts deeply in the direction of the extended arm
</seg>,
<seg type="anomaly_sig">
perhaps compensating for the awkward hyperextension, or perhaps resting out of sheer exhaustion. Indeed, we
don’t know how long the man has been in the apparatus; if the plants actually have grown on his arm, he may
very well have been in this position for quite a while.
</seg>
</p>
<p>
Returning to the question of purpose, the <hi rend="italics">why</hi> of the image’s representation, we look
to the plants themselves.
<seg type="binary_a">
Utility
</seg>
does not underwrite their cultivation; rather, the
<seg type="binary_b">
whimsy
</seg>
of their variety indicates that they function more as a sign of the color and bounty of summer’s flora.
Put simply, the man doesn’t seem to be accomplishing anything substantial in the world. Growing the plants,
then, evinces less of
<seg type="binary_a">
a material goal
</seg>
—human use or natural restoration—and more of
<seg type="binary_b">
a ceremonial devotion
</seg>.
Because we have no context for the ritual, because instead of on lush scenery the image foregrounds the
situation atop a depthless, ascetic, white matte, the tone strikes the viewer not as celebratory but as elegiac.
</p>
<p>
Again, the ParkeHarrisons imply narrative through the questions that we’re led to ask: what is the purpose
of the ritual, if it is a ritual in the first place? what does the ritual elegize, and if it does elegize
something, what led to that loss? At this point a narrative of ecological decline or even disaster isn’t
beyond the pale, and we wouldn’t be out of line in postulating for the man the role of a minister of a
forgotten religion.
<seg type="complication">
Despite the clear differences between the mechanical, the human, and the natural, complicating similarities
slyly lie behind the organizing contrasts.
<seg type="strand">
The vertical lines of the mechanical apparatus continue in the more organic form of the plants’ stems
and leaves beyond the perpendicular horizon of the man’s arm.
</seg>
Compositionally speaking, then, the human either divides the natural from the mechanical, or it represents a
blend of the two. We often invoke technology and industry as antithetical to nature, but in
<title level="a">Summer Arm</title> their purpose is specifically to support natural growth, which then attracts
the additional life of the butterflies and bee-like insect. Of course, this use of mechanical technology results
not from large-scale efforts but from an individual’s ritualistic bricolage.
</seg>
</p>
<p>
<seg type="conclusion">
<title level="a">Summer Arm</title> leads us to several larger questions about the ParkeHarrisons’ work.
<seg type="research_question" xml:id="student_rq_1">
Despite the implication that industry and technology destroy the natural world, to what degree do the
ParkeHarrisons present (and endorse) the possibility that they can be harnessed as ecological adjuncts?
</seg>
<seg type="research_question" xml:id="student_rq_2">
Like the man in <title level="a">Summer Arm</title>, do the ParkeHarrisons make their artworks as elegies
or as the kind of patched-together scaffolds on which the human may foster growth?
</seg>
<seg type="research_question" xml:id="student_rq_3">
Just what sort of sacrifice or support does nature require from us?
</seg>
<seg type="research_question" xml:id="student_rq_4">
Ultimately, how can we negotiate Summer Arm’s various <q>selves</q>—aesthetic object, abstract
symbolism, programmatic allegory, call to action, and, finally, material object whose very composition
involves the mechanical-human-natural triad that it represents?</seg>
</seg>
</p>
</div>
```

[^1]: Robert and Shana ParkeHarrison, _Summer Arm_, mixed media, [http://static.icompendium.com/artistInfo/parkehar/big/284.jpg?0](http://static.icompendium.com/artistInfo/parkehar/big/284.jpg?0 "ParkeHarrison, 'Summer Arm'").
