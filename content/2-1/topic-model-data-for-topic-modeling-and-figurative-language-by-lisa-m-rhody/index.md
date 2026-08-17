+++
title = "Topic Model Data for Topic Modeling and Figurative Language"
slug = "topic-model-data-for-topic-modeling-and-figurative-language-by-lisa-m-rhody"
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
weight = 2
authors = ["Lisa M. Rhody"]
author_ids = ["lrhody"]
author = ["lrhody"]
aliases = ["/2-1/topic-model-data-for-topic-modeling-and-figurative-language-by-lisa-m-rhody.html", "/2-1/topic-model-data-for-topic-modeling-and-figurative-language-by-lisa-m-rhody/"]
+++

The topic model discussed in “Topic Modeling and Figurative Language” was created with MALLET. Drawing from 4,500 English-language poems from the “Revising Ekphrasis” corpus, the model was generated using the following parameters:

```
mallet train-topics --input poems-seq.mallet --num-threads 2 --num-topics 60 --optimize-interval 10 --output-model poems08072012test1.model --output-doc-topics poems08072012_test1.txt --output-topic-keys poems08072012-test1keys.txt
```

The following table contains the number of the topic (0-59); hyper-parameter estimation; and top 20 key words most likely to be found in each topic.

<table border="1" cellpadding="3" cellspacing="0">
<tbody>
<tr>
<td nowrap="nowrap" style="text-align: center;" valign="top" width="50"><b>Topic</b></td>
<td nowrap="nowrap" style="text-align: center;" valign="top" width="100"><b>Proportion</b></td>
<td nowrap="nowrap" style="text-align: center;" valign="top" width="150"><b>Topic Key Words</b></td>
</tr>
<tr>
<td>0</td>
<td>0.07467</td>
<td>city streets country middle year park town times thousand paris state york jews jew henry rich houses empire broken central</td>
</tr>
<tr>
<td>1</td>
<td>0.01304</td>
<td>ball father field casey trouble boy baseball ebbets brooklyn play game thousand pitcher satchel bat day luis mickey diamond los</td>
</tr>
<tr>
<td>2</td>
<td>0.42746</td>
<td>death life heart dead long world blood earth man soul men face day pain die days eyes years hand tears</td>
</tr>
<tr>
<td>3</td>
<td>0.28246</td>
<td>world life mind time space human body things future earth thought sense place called end moment air order choose form</td>
</tr>
<tr>
<td>4</td>
<td>0.00659</td>
<td>de la el en green verde con los mi se del poem ni lo os poema yo oo ya sobre</td>
</tr>
<tr>
<td>5</td>
<td>0.02437</td>
<td>horse deer shoe horses european forward loves james species nose st sweeping rider pray worm story seconds mane survive assassin</td>
</tr>
<tr>
<td>6</td>
<td>0.12499</td>
<td>blue red white bird color green yellow black wings birds feathers hawk girl box pink round brown nest orange flying</td>
</tr>
<tr>
<td>7</td>
<td>0.02036</td>
<td>portrait duke parrot grace starlings bronze woman lord heron guilt figures phyllis daphne helmet roman smiling brush painted painting gri</td>
</tr>
<tr>
<td>8</td>
<td>0.04481</td>
<td>sweet golden fair winds dew flowers wine tender dying fresh venus lovely brings sheep nature flow shepherd silver make crystal</td>
</tr>
<tr>
<td>9</td>
<td>0.03802</td>
<td>thy thou thee art thine st doth heaven hast hath dost er shalt mine leave bid rest seek thyself joy</td>
</tr>
<tr>
<td>10</td>
<td>0.09271</td>
<td>god lord man hell heaven soul holy ye angel good earth christ sin spirit em mercy prayer give blessed truth</td>
</tr>
<tr>
<td>11</td>
<td>0.01756</td>
<td>praise whack give spiral penny matter heaven alabanza violet lightning colour hanging ave hush shell chimera effects percent fat sew</td>
</tr>
<tr>
<td>12</td>
<td>0.10439</td>
<td>poetry line sense person poet poem language words feeling point lines meaning subject real witness physical story art problem beauty</td>
</tr>
<tr>
<td>13</td>
<td>0.04146</td>
<td>text words screen disaster beat tail word motion hunted speed door open gestures keys material logic failing notebook noun ladder</td>
</tr>
<tr>
<td>14</td>
<td>0.01923</td>
<td>coat famous matter hat layer coats fold theory weave folds completed squirrel code hole lip giving mower suddenly hats watched</td>
</tr>
<tr>
<td>15</td>
<td>0.01781</td>
<td>monkeys human pressure machine cave boat luminous image animal tubes dot myth patient fork bison cowboy ra solar set tuc</td>
</tr>
<tr>
<td>16</td>
<td>0.23363</td>
<td>house room door window street glass black wall table morning walls windows small past rooms floor books hair dark bed</td>
</tr>
<tr>
<td>17</td>
<td>0.01374</td>
<td>mr bo bonghy yonghy hand uh yeah um stall moonlight riding pony gonna gentlemen jack tom lady tlot jug alright</td>
</tr>
<tr>
<td>18</td>
<td>0.1251</td>
<td>sea water ocean waves ship sand boat fish shore tide beach land green white great shark island waters sail rock</td>
</tr>
<tr>
<td>19</td>
<td>0.03033</td>
<td>room drunk eng wine chang hotel private rome true john forbidden cards tiger answer rambling carl jazz roast poetry rendezvous</td>
</tr>
<tr>
<td>20</td>
<td>0.0611</td>
<td>poem write poems letter writing page book read poet words word wrote letters great johnny pages head poets written language</td>
</tr>
<tr>
<td>21</td>
<td>0.13955</td>
<td>man eyes hair black drink head sees death takes face house waits dance hand falls close beautiful air calls turns</td>
</tr>
<tr>
<td>22</td>
<td>0.07743</td>
<td>boy girl school boys girls train street war summer walking woman village age class bus past goodbye station line car</td>
</tr>
<tr>
<td>23</td>
<td>0.00262</td>
<td>wi night auld syne gat lang fere ye owre ha till goodly fu grendel nae lasses luve weary ane sae</td>
</tr>
<tr>
<td>24</td>
<td>0.01807</td>
<td>york times public september bush president deborah prince press office oil helicopter citizens st national mr museum american landing charles</td>
</tr>
<tr>
<td>25</td>
<td>0.00633</td>
<td>spam occupation conturbat mortis timor animal guam lips sharon made loneliness lynn west part east miner equation sir beef beds</td>
</tr>
<tr>
<td>26</td>
<td>0.0808</td>
<td>water fish surface air light back lake bridge pond fear carrying tin bodies swimming lights day bottom bright current wing</td>
</tr>
<tr>
<td>27</td>
<td>0.26726</td>
<td>made time great feet side hand round god eyes place stood set lay left till sun ground back turned stand</td>
</tr>
<tr>
<td>28</td>
<td>0.0326</td>
<td>love stood mind heaven fear dame proud rest maid fair place feast hell fatal hounds care day prey pursue pursued</td>
</tr>
<tr>
<td>29</td>
<td>0.04181</td>
<td>idea part ideas system tragic stage fucking mattress works brain prometheus places rock runs series friend points knowledge general positions</td>
</tr>
<tr>
<td>30</td>
<td>0.00652</td>
<td>de miss ain jump dat ah dey ter yo slim scarlett hunh git back tu stan fu huh barbie den</td>
</tr>
<tr>
<td>31</td>
<td>0.16209</td>
<td>soul beauty earth thoughts sweet ah er deep spirit wild heaven sad year calm rest air youth soft form dim</td>
</tr>
<tr>
<td>32</td>
<td>0.38369</td>
<td>night light moon stars day dark sun sleep sky wind time eyes star darkness bright dream morning bed hear blue</td>
</tr>
<tr>
<td>33</td>
<td>0.0423</td>
<td>war men achilles land gods great troy victory soldiers son goddess words fought battle soldier army greek left hector truth</td>
</tr>
<tr>
<td>34</td>
<td>0.15537</td>
<td>song voice music sound words sing singing songs long hear heard notes sweet ear voices listen bird lady wind sings</td>
</tr>
<tr>
<td>35</td>
<td>0.66719</td>
<td>don time ll ve make day things back people good thing feel work life find long love won remember left</td>
</tr>
<tr>
<td>36</td>
<td>0.0222</td>
<td>bells ii iii iv vi vii ho ice miracle thunder ix viii king peace swords wide banks miniver romeo blackbird</td>
</tr>
<tr>
<td>37</td>
<td>0.20618</td>
<td>head looked back thought man turned didn white fell knew stood sat heard hair red watched walked men called felt</td>
</tr>
<tr>
<td>38</td>
<td>0.03754</td>
<td>america soul land great part freedom rivers waters announce flow slave blood past indian passage free vast parts pass women</td>
</tr>
<tr>
<td>39</td>
<td>0.03265</td>
<td>art din hide beauty fear light painting artist kingdom matisse shadow stone dread gunga painter objects model gallery master peak</td>
</tr>
<tr>
<td>40</td>
<td>0.53625</td>
<td>wind river sky water trees snow light rain leaves white green air cold sun road field fields winter grass long</td>
</tr>
<tr>
<td>41</td>
<td>0.1053</td>
<td>day round till ye good er eye men hath fair high lie fast wide tis strange twas merry gentle blow</td>
</tr>
<tr>
<td>42</td>
<td>0.20498</td>
<td>skin stone bone bones blood mouth eye flesh black tongue steel water turn rock teeth inside hole cut bodies wet</td>
</tr>
<tr>
<td>43</td>
<td>0.09104</td>
<td>big money people american richard street white english york modern america phone buy chicago talking movie home war bill bag</td>
</tr>
<tr>
<td>44</td>
<td>0.01553</td>
<td>goat mr fly horowitz mrs tenure goats elephant buzz sheep milk trunk carlyle apricots stack nice cleft devil rushes nervous</td>
</tr>
<tr>
<td>45</td>
<td>0.09358</td>
<td>time question thing reason makes law light shows speech choice change perfect interest present kind measure shown account wrong great</td>
</tr>
<tr>
<td>46</td>
<td>0.15667</td>
<td>black red car back fire radio inside smoke road dirt bus cars dust lights train iron shirt dog gray windows</td>
</tr>
<tr>
<td>47</td>
<td>0.00166</td>
<td>ye ne doe ring sing woods theyr al eccho ben love answer thi shal erthe herte lyke long fayre god</td>
</tr>
<tr>
<td>48</td>
<td>0.0932</td>
<td>eat table bread kitchen plate salt cup food coffee orange ice eating meat milk chicken good butter fat tea cream</td>
</tr>
<tr>
<td>49</td>
<td>0.23713</td>
<td>love heart loved live loves sweet life world true kiss eyes lips make lover mind die dear lost give man</td>
</tr>
<tr>
<td>50</td>
<td>0.09267</td>
<td>vain ring er man state fate fame tis nature power great good heaven glorious strong happy race strength rise heav</td>
</tr>
<tr>
<td>51</td>
<td>0.06024</td>
<td>man woman men dead women young time house lies weeping world age patrizia sex unfolded married board foundry watch shows</td>
</tr>
<tr>
<td>52</td>
<td>0.01615</td>
<td>ll buy laura lizzie goblin forest dear marsh eat fruits sir tender gun freud blades grow beat rapture minnehaha brookdog cat fox dogs children states poor street cats church rich ball tail kitten yard hare paul aged drowning village</td>
</tr>
<tr>
<td>53</td>
<td>0.01909</td>
<td>flags thread names learning kong rocks yr hem string cloth elizabeth mexico magic fabric united july numbers stitch needle mirrors</td>
</tr>
<tr>
<td>54</td>
<td>0.23906</td>
<td>tree green summer flowers grass trees flower spring leaves sun fruit garden winter leaf apple yellow rose year morning gold</td>
</tr>
<tr>
<td>55</td>
<td>0.50195</td>
<td>body back hands face hand eyes inside head open white arms woman mouth small sleep hair light legs dark turn</td>
</tr>
<tr>
<td>56</td>
<td>0.20162</td>
<td>mother father child children years dead son home brother daughter family wife bed sister baby day made parents boy born</td>
</tr>
<tr>
<td>57</td>
<td>0.00688</td>
<td>de moloch le la les cf des rats mayor piper pas je di bridge du river clock charbon mon est</td>
</tr>
<tr>
<td>58</td>
<td>0.01597</td>
<td>gertrude guitar inside blue stein beginning sieve cloud type end tiny lee live bad world wrist picasso feel small pussy</td>
</tr>
<tr>
<td>59</td>
<td>0.04035</td>
<td>dog cat fox dogs children states poor street cats church rich ball tail kitten yard hare paul aged drowning village</td>
</tr>
</tbody>
</table>
