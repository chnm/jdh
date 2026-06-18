+++
title = "Programming with Arduino for Digital Humanities"
slug = "programming-with-arduino-for-digital-humanities"
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
weight = 3
authors = ["Kazushi Ohya"]
author_ids = ["kohya"]
author = ["kohya"]
+++

### Poster

<iframe class="gde-frame" scrolling="no" src="https://docs.google.com/viewer?url=http%3A%2F%2Fjournalofdigitalhumanities.org%2Fwp-content%2Fuploads%2F2013%2F11%2FProgramming-with-Arduino.pdf&amp;hl=en_US&amp;embedded=true" style="width:100%; height:500px; border: none;"></iframe>

[Download (PDF, 92KB)](https://journalofdigitalhumanities.org/wp-content/uploads/2013/11/Programming-with-Arduino.pdf)

### Background

The department of library, archive, and information studies at Tsurumi University provides courses on computer science for humanities students. The courses include one introductory and two intermediate programming courses. There are project-based courses on Digital Humanities instead of an advanced programming course. In the introductory course, [Scratch](http://scratch.mit.edu/ "'Scratch' Programming Tool") was used and in the intermediate courses, Java has been adopted.

Difficulties in teaching programming in an introductory course to humanities students have been to let students find interest or enjoyment in (1) symbol manipulation and (2) grouping tasks with functions or other similar units.

Humanities students tend to expect big results in programming. They are disappointed at small results from source codes in exercises. It is usually difficult to expect them to find interest in a small result from symbol manipulation in introductory programming.

As far as our experience goes, humanities students seem to struggle to envision the existence of a computational world in their minds. The formats and abstract behaviors of typical programming patterns appearing in structured programming such as assignment, iteration, condition, and flow control themselves are not difficult for humanities students to understand. The grammar is easy to comprehend. The problem they face is to understand the ways to use them as substantial components making up the whole code in actual programming.[^1]

### Embedded System: Arduino

In order to respond to the aforementioned difficulties or problems, we set two requirements for the programming environment:

1. letting students be interested in something moving, and
2. letting students be satisfied with small results.

Then, we decided to introduce embedded systems to an introductory programming course. We expected embedded systems to bring the real world into a scene of learning programming.

Current students have been immersed in digital or virtual environments from an early age. They are not easily satisfied with computational results on screens. On the other hand, interestingly, they show interest in physical phenomena even if it is slight.[^2] They are very sensitive to physical stimuli. Embedded systems can be expected to let students be interested in something moving that may be small. And, it can contribute to helping students envision a computational world in their minds.

As an embedded system, we adopted [Arduino](http://www.arduino.cc/ "Arduino Home Page"), which provides a good developing environment:

1. there is no need to prepare a device to install native codes to ICs,
2. there is an easy IDE based on [Processing](http://processing.org/ "Processing programming language home page") , and
3. the price of Arduino is affordable.

A concern we noticed about introducing Arduino was that students have to learn about electricity to some extent. It is an unfamiliar subject to humanities students.

The IDE for Arduino on Processing provides simple descriptive rules reminiscent of BASIC, and easy to view and write grouping tasks in methods. We expected this feature would make it easy for students to concentrate on finding categories of processes and making groups with functions.

### Course Design

One semester consists of 15 classes, which are lectures on and practices of programming. The practices consist of four themes: LED handling, variable registor, sound handling, and binary display.

In all practices, we used only three circuit patterns based on a voltage divider. The typical four programming patterns in procedural languages were learned with eight source codes using one circuit pattern of an LED. We used a variable resistor as an input device and a game controller in learning structural programming. An array is not a difficult topic in programming, but it is not easy for students to understand the usefulness of the array. Arrays working as music scores to handle sound seemed to be a good example. We think that even though the topic of a binary digit may not be useful in Digital Humanities, students should learn it to feel the philosophy behind symbol manipulation. We used bit operation to control LEDs of a binary digit display, and provided a chance to learn binary digit.

### Observation and Future

Fortunately, many students seemed to find enjoyment from a small result in physical programming and grouping tasks. However, as we expected before this experiment, learning electricity seemed to be difficult for students. For example, Ohm’s law was difficult for students who had learned it in junior high school. It might be possible to teach electronic circuit like LEGO block without any explanation of theory or background knowledge. However, learning scientific theories is inevitable in science education. We are planning to devise course materials to reduce the offset of learning electricity for next year.

Originally presented by Kazushi Ohya at DH2013 on [July 17, 2013](http://dh2013.unl.edu/abstracts/ab-117.html "Abstracts DH2013").

### References

Banzi, M. 2011. _Getting Started with Arduino._ 2nd ed. O’Reilly Media.

Gibbs, N. E. and A. B. Tucker. 1986. “A Model Curriculum for A Liberal Arts Degree in Computer Science.” _Communications of the ACM_ 29(3), ACM.

Ishii, H. 2006. “Tangible User Interfaces.” _CHI 2006 Workshop Proceedings._

Kobayashi, S. 2010. _Prototyping Lab in Japanese._ Japan: O’Reilly.

Liberal Arts Computer Science Consortium (LACS). 2007. “A 2007 Model Curriculum for a Liberal Arts Degree in Computer Science.” _ACM Journal on Educational Resources in Computing_ 7(2). ACM.

Marshall, P. 2007. “Do tangible interfaces enhance learning?” _TEI’07._ ACM.

Monk, S. 2012. _Programming Arduino._ New York: McGraw-Hill Companies.

Schmidt, M. 2011. _Arduino._ The Pragmatic Programmers.

Winslow, L. E. 1996. “Programming Pedagogy — A Psychological Overview.” _SIGCSE Bulletin_ 28(3). ACM.

Arduino. [http://www.arduino.cc/](http://www.arduino.cc/ "Arduino project home")

Processing. [http://processing.org/](http://processing.org "Processing programming language home")

Scratch. [http://scratch.mit.edu](http://scratch.mit.edu "'Scratch' tool home page")

[^1]: Winslow, L. E. (1996). “Programming Pedagogy — A Psychological Overview.” _SIGCSE Bulletin_ 28(3). ACM.

[^2]: Ishii, H. (2006). “Tangible User Interfaces.” _CHI 2006 Workshop Proceedings_.
