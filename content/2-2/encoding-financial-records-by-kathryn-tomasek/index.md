+++
title = "Encoding Financial Records"
slug = "encoding-financial-records-by-kathryn-tomasek"
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
weight = 3
authors = ["Kathryn Tomasek"]
author_ids = ["ktomasek"]
author = ["ktomasek"]
+++

### Introduction[^1]

“[A]ccount books,” business historian Judith McGaw noted in 1985, “are among the most common but least accessible primary sources for historians….” In the intervening twenty-seven years, historians have made use of these rich sources to produce a range of articles and monographs, but few digitization projects have tackled financial records directly.[^2]

Some standardized electronic data has long been available to social science historians. The [Minnesota Population Center’s Integrated Public Use Microdata Series](https://cps.ipums.org/cps/ "Integrated Public Use Microdata Series Home") provides harmonized data for U.S. and international population studies. The [National Historic Geographic System](https://www.nhgis.org/ "NHGIS Home") provides data for United States historical geography, as does the [Great Britain Historical Geographic Information System](http://www.port.ac.uk/research/gbhgis/ "Great Britain Historical GIS") for Britain. A current initiative of the European Science Foundation, the [European Historical Population Samples Network](http://www.ehps-net.eu/ "European Historical Population Samples Network Home"), seeks “to create a common format for databases containing information on persons, families and households.” And while a strong tradition of monographs and journals in economic history has resulted from investigation of archival financial records, no comparable project exists for their digitization.[^3]

In August 2011, a group of historians, archivists, and technologists met at Wheaton College in Massachusetts to discuss initial steps towards developing standards for markup and metadata for manuscript financial records using [TEI](http://www.tei-c.org/index.xml "TEI Home"). Drawing on the expertise developed by pioneering projects at the [Massachusetts Historical Society](http://www.masshist.org/ "Massachusetts Historical Society Home"), the [University of Virginia](http://www.virginia.edu "University of Virginia"), and [MIT](http://web.mit.edu/ "MIT Home"), this group explored the current state of affairs through discussion of problems and case studies, proposed some paths forward, and identified model projects to test those paths.

The first section of this paper describes the desirability of developing models and standards for markup of financial records. Data modeling will require further investigation, and the second section outlines some of the challenges presented by manuscript financial records. The third demonstrates the potential and limitations of existing TEI elements, especially the <measure> element. Examples are drawn from the Project Director’s work on the [Wheaton College Digital History Project](http://wheatoncollege.edu/digital-history-project/ "Wheaton College Digital History Project").

Discussion of these models points to broad research potential should large numbers of financial records be marked up in standard formats. The examples also sketch out some of the parameters of the problem space for developing a more comprehensive tag-set capable of expressing the complexities of historical financial records, especially if guidelines can be established for expressing the more complex semantic values to be found in many types of historical financial records. One possible method that is currently being explored involves standoff markup using an investigational new tag-set, a so-called “transactionography.” The final section outlines some principles to be followed in considering development of this tag-set.

### Financial Records in Historical Research

A genre of primary sources that includes such materials as bills and receipts, cashbooks, transaction journals and account ledgers, financial records are abundant in traditional archives. Most current digitization projects do not capture some of the more complex semantic values within the records, and if they do, they have yet to develop a common method for fully expressing these semantic values. For example, the [Bethlehem Digital History Project](http://bdhp.moravian.edu/home/home.html "Bethlehem Digital History Project")displays images of a few extracts from business ledgers. The [Railroads in the Making of Modern America](http://railroads.unl.edu/ "Railroads in the Making of Modern America") at the University of Nebraska includes a few transcriptions of payroll records for railroad employees, and this information is stored in a searchable database. In these cases, the financial information is neither comprehensive nor presented in a manner that can be leveraged efficiently by researchers.

In the Project Director’s field alone, the wealth of monographs produced since 1990 speaks to the abundance of archival financial records and their utility for historians of the early United States. Since documentary projects at the Massachusetts Historical Society and the University of Virginia coincide with the Project Director’s chronological field, the activities conducted under this award focused on this rather narrow geographical and chronological area.[^4]

Thus our discussions of such documents only begins to suggest the research opportunities that might eventually be available should large numbers of financial records be digitally accessible in machine processable form. As editors of the [Alcalá Account Book Project](http://archives.forasfeasa.ie/ "Alcalá Account Book Project") have noted with regard to their digital edition of the account books of the Royal Irish College of Saint George the Martyr in Alcalá, such records promise “insight into the day-to-day running of the college with valuable information on diet, discipline, and domestic matters.” Should additional accounts from similar institutions be transcribed and marked up in standard fashion, the value of such insights would be enhanced considerably.[^5]

At the Massachusetts Historical Society, editors have used TEI in the creation of digital editions of the [Adams Family Papers](http://www.masshist.org/digitaladams/aea/index.html "Adams Family Papers"), the previously produced print editions of the Adams Papers, and a collection of Thomas Jefferson documents. In the production of those editions, they have encountered the limits of TEI for markup of financial records found within those collections. Reflecting similar dissatisfaction with the limits of the current system, editors of the [Papers of George Washington](http://gwpapers.virginia.edu/project/index.html "Papers of George Washington") at the University of Virginia are transcribing Washington’s financial papers into a relational database. Their data will be convertible into TEI-conformant XML, but at this time the sheer volume of documents to be transcribed prevents the project’s leaders from using the underdeveloped potentials of the TEI guidelines for this type of manuscript.

### Features and Challenges of Historical Financial Records

Financial records share certain structural characteristics with such other genres of historical records as plague bills, theatre returns, and probate records. Documents from such genres are generally represented as lists or tables, and in many cases they include numerical sums that may or may not extend to totals across pages. This apparent regularity presents perhaps the most significant challenge for those who seek to mark up such records, as it often collapses in use. Thus such tabular records tend to include information that cannot be represented through simple transcription of tabular layout. In fact, they tend to contain significant variations and idiosyncrasies, often within the same document or collection.

In the subgenre of double entry accounts, the impulse to keep regular records produced a set of standards for assigning particular semantic values to financial information. By the eighteenth century, an influential textbook offered ordinary businessmen an opportunity to learn how to keep regular accounts. But the popularity of Scottish economist John Mair’s _Book-keeping Methodiz’d; or, A methodical treatise of Merchant-accompts, according to the Italian form_ did not guarantee perfect adherence to his principles.

Seeming regularity extends beyond double-entry accounts and can appear in numerous forms. For example, one might expect theatre receipts recorded on printed forms to display information quite systematically. Such regularity does indeed characterize the rectos of printed forms used by the _Comédie Française_. The versos however often include such additional types of information as cast lists with marked irregularity. Such lists offer significant information despite their rather haphazard distribution throughout the collection. In other cases, simple prose journals often contain financial information recorded either regularly or intermittently. Authors frequently flipped notebooks, creating texts that operated as prose journals in one direction and financial records in the other.[^6] John Adams recorded financial information more irregularly. Editors at the Massachusetts Historical Society have noted that he interspersed records of expenditures for travel to and from Philadelphia during the Revolutionary War in one of his diaries.

Developing standards for marking up historical financial records thus presents many challenges. In addition to the idiosyncrasies of individual authors, historical and geographical variations in commodities, units of measure, and currencies raise questions with regard to both standardization and normalization.

In the case of commodities, for example, each project could certainly create its own taxonomy for commodities mentioned in its collections. Such a course would however decrease the utility of the data produced for analysis across projects. Ideally, a controlled vocabulary shared across projects would maximize the value of harvestable data. Our survey of the field led us to the [Harmonized System](http://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-online.aspx "Harmonized System Home") established by the World Customs Organization, but this resource does not seem optimal because it is designed to represent contemporary commodities. This Harmonized System includes a code for muslin for instance, but it is unlikely to provide one for saltpeter. In addition, the nomenclature tool for this system is behind a pay wall and is thus inaccessible for most academics. Price tables that historian John J. McCusker created for Great Britain and the United States between the seventeenth and nineteenth centuries offer a starting point. The [Visible Prices](http://www.paigemorgan.net/visibleprices/ "Visible Prices Home") project is developing a database that presents a model for digital representation of such data.[^7]

In the case of currencies as well, standardization would foster processability, and McCusker’s work again represents an exemplar. Certainly determining which standard to use introduces a puzzle for cases in which scholarly resources equivalent to McCusker’s currency tables are unavailable. Thus McCusker’s tables only begin to answer questions that will be raised by efforts to generate a standard applicable across time and space. And the distinction between standardization and normalization presents a particular challenge. Should references to a certain amount of a given currency be merely regularized, be normalized to a standard contemporaneous currency, be normalized to a standard modern currency, or be normalized to a reference currency?[^8]

Finally, the meanings of financial records — their semantic values — might seem quite straightforward, but even apparently simple documents actually hold connotations that might be unpacked to reveal significant information. The sample documents in the next section demonstrate some of those connotations.

### Sample Markup and Complex Expressions

Manuscript financial documents tend to include three levels of data to consider: layout, textual expression, and a third, more abstract level of semantic values that are not as yet easily captured through TEI conformant markup. Attention to layout may or may not be necessary. In cases where page images are included in online publication, for example, some projects may choose to omit digital representation of layout. Similarly, the significance of some elements of textual expressions might vary across projects.

The files excerpted here demonstrate the utility of the TEI <measure> element and some of the challenges presented by complexities of even apparently simple documents. The sample documents are from the Wheaton Family Papers, a collection associated with the family that founded Wheaton Female Seminary in Norton, Massachusetts, in 1834. The documents refer to costs associated with room, board, and laundry for three adults who traveled from the Boston area to London for the international exhibition of 1862. The Wheaton College Digital History Project has focused on imaging, transcribing, and marking up documents from the Wheaton Family Papers since 2005.

A boarding receipt from 1862 records a single transaction in which a boarder paid a boardinghouse keeper for room and board over a specified period:

<div class="wp-caption aligncenter" id="attachment_5509" style="width: 310px"><a href="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Boarding-Receipt-1862.png" target="_blank"><img alt="Boarding Receipt, 1862" aria-describedby="caption-attachment-5509" class="size-medium wp-image-5509" height="176" src="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Boarding-Receipt-1862-300x176.png" title="Boarding Receipt, 1862" width="300"/></a><p class="wp-caption-text" id="caption-attachment-5509">Figure 1: Boarding receipt, May 20, 1862. Wheaton Family Papers, M089, Wheaton College Archives and Special Collections. Wheaton College, Norton, Massachusetts. Used by permission.</p></div>

Transcribed, the text of the receipt is marked up to convey descriptive information about the document. Part of this markup prescribes rendering of superscripts, a layout feature that may or may not be significant for online publication that will include a link to the document image. Including the <handNote> element adds information about textual expression that is significant at the collection level. For local users of the [Wheaton College Archives and Special Collections](http://www2.wheaton.edu/learnres/ARCSC/ "Wheaton College Archives Home"), identifying documents written by members of the Wheaton family and their circle bears some interest. Such information might also be of interest beyond the local level since the fact that the boarder wrote out the receipt and the boardinghouse keeper signed it suggests something about the roles of the two women in the transaction. The boarder in this case eventually became a businesswoman herself, and this receipt might be read to indicate that she had an interest in keeping track of her money and how it was spent even before her occupational change.

The TEI Guidelines already contain the <measure> element, which is meant to record measurements like those contained in documents that refer to monetary transactions. Examples in the P5 Guidelines demonstrate several attributes that may be used with <measure>. This sample follows one of those examples in using “type” to express the currency value attached to the room and board that lay on the other side of the transaction.

Adding the <measure> element to the markup can broaden the audience for the information conveyed by the digital edition of the document beyond that addressed in a simple representation describing layout and textual expression. With the <measure> element included, the markup would identify processable information about both currency and the commodities for which it was exchanged. A digital object of mere local interest could thus be put to broader use.

Using the attribute “commodity” here without its usual accompanying attributes “quantity” and “unit” might however be inadequate. And while the notebooks that record the “provisions” consumed on each day that the boarders stayed do accompany the receipts in this collection, they do not contain clear information about the number of “apartments” the guests occupied. Thus the documents do not provide clear “quantity” or “unit” values for the commodities “room” and “board” indicated on the receipt.

<div class="wp-caption aligncenter" id="attachment_5512" style="width: 310px"><a href="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Boarding-Reciept-XML.png" target="_blank"><img alt="Boarding Reciept XML" aria-describedby="caption-attachment-5512" class="size-medium wp-image-5512" height="170" src="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Boarding-Reciept-XML-300x170.png" title="Boarding Reciept XML" width="300"/></a><p class="wp-caption-text" id="caption-attachment-5512">Figure 2: Boarding Reciept XML</p></div>

This boarding receipt is one of several in the collection for the spring and summer of 1862. These documents are also accompanied in the collection by several laundry lists and by two notebooks that contain detailed daily boarding records for the same period. Thus the collection includes sufficient details about one set of exchanges of cash for services to suggest that transcription and appropriate markup of these documents and others like them could well add to historical knowledge about market values for room and board in one London neighborhood during an international exhibition of the Victorian era. We might expect other collections to hold comparable documents, and in the aggregate digital versions of such documents could provide significant information about an economic phenomenon common to cities in many times and places. If digital versions were to use standard markup, machine processing of the data across collections would become comparatively simple.

While the boarding receipt records a single transaction with two commodities to be measured along with their combined price, a laundry list from the same period records a single transaction involving numerous items and prices for each:

<div class="wp-caption aligncenter" id="attachment_5513" style="width: 148px"><a href="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Laundry-List.png" target="_blank"><img alt="Laundry List" aria-describedby="caption-attachment-5513" class="size-medium wp-image-5513" height="300" src="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Laundry-List-138x300.png" title="Laundry List" width="138"/></a><p class="wp-caption-text" id="caption-attachment-5513">Figure 3: Laundry List, May 19, 1862. Wheaton Family Papers, M089, Wheaton College Archives and Special Collections. Wheaton College, Norton, Massachusetts. Used by permission.</p></div>

Here, the <measure> element conveys information about the currency as well as about the items to be washed. But some might argue that using the <measure> elements here to encode items of clothing implies that the items that are marked up were themselves traded for the sum of money encoded by the immediately following <measure>. But the boarder did not pay the boardinghouse keeper for, say, a skirt; the boarder paid for the service of laundering the skirt.[^9]

One clear approach to thinking about this problem is that the encoding has it right: the <measure> element includes a normalization of what is written on the page, and the fact that the list only itemizes pieces of clothing, leaving for the reader to draw the inference that the service being provided was laundering (because it is a laundry list) is correctly represented. But computers are not nearly as good as humans at making that kind of inference, and in the study of large quantities of historical financial records, it is potentially very powerful to be able to associate goods or services with the prices paid for them in a large scale automated way.

One way around this would be greater specificity in the commodity attribute, for example introducing use values like “service-laundered-skirt.” While we have not thoroughly tested this approach, it is problematic. It seems clumsy and may not scale well; and some would say it misrepresents what was written on the page.

<div class="wp-caption aligncenter" id="attachment_5510" style="width: 310px"><a href="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Laundry-List-XML.png" target="_blank"><img alt="Laundry List XML" aria-describedby="caption-attachment-5510" class="size-medium wp-image-5510" height="173" src="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Laundry-List-XML-300x173.png" title="Laundry List XML" width="300"/></a><p class="wp-caption-text" id="caption-attachment-5510">Figure 4: Laundry List XML</p></div>

If even such apparently simple documents as receipts and laundry lists contain semantic values that cannot be accounted for straightforwardly with existing TEI elements, further data modeling is clearly needed. Topics to be considered include:

- generating lists of typical features of the information contained in account books and other structured records for various places and times,
- determining characteristics specific to particular genres of structured records, and
- differentiating between account books and other sorts of structured records related to exchangesof cash, property, goods, and services.

### Double Entry Accounts

Double entry bookkeeping as developed in Italy as early as the fourteenth century and described by Mair in the eighteenth century represents a specialized vocabulary, a professional jargon that requires data modeling with attention to the special meanings of the terms “debtor” and “creditor” in this language, as well as the relationships between transactions recorded in the daybook and accounts kept in a separate ledger. We are developing a TEI customization for conveying such meanings and their expressions within the journals and ledgers of double entry account books through a “transactionography” that will represent the relationships among such records in abstracted form.

<div class="wp-caption aligncenter" id="attachment_5515" style="width: 244px"><a href="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Double-Entry-Account-Book.png" target="_blank"><img alt="Double Entry Account Book" aria-describedby="caption-attachment-5515" class="size-medium wp-image-5515" height="300" src="https://journalofdigitalhumanities.org/wp-content/uploads/2013/10/Double-Entry-Account-Book-234x300.png" title="Double Entry Account Book" width="234"/></a><p class="wp-caption-text" id="caption-attachment-5515">Figure 5: Laban Morey Wheaton Daybook, pp. 136-137, September 1 – November 14, 1835. Wheaton Family Papers, M089, Wheaton College Archives and Special Collections. Wheaton College, Norton, Massachusetts. Used by permission.</p></div>

The above page spread from a daybook in the Wheaton Family Papers offers an example of some of the complex semantics represented in double entry accounts. The numbers recorded in the first column refer to accounts found in the associated ledger. Dates are written at the top of the page and subsequently centered in the second column. Each transaction may contain multiple items and refers to the individual involved. Notations at the extreme right of the second column indicate whether the transaction is classified as a debit or credit and thus on which side it may be found in the ledger. Amounts in column-pairs three & four and five & six indicate the price per unit (dollars in column 3, cents in column 4) for each item, and a total (dollars in column 5, cents in column 6) for each transaction respectively.

As currently conceived, a “transactionography” follows the principles of double entry accounting to model _transactions_ as a sequence of one or more _transfers_ of anything of value from one _account_ to another. Thus, the simple purchase of a candy bar from a convenience store is represented as two <transfer>s: one of a candy bar from the vendor’s stock account to the buyer, and one of $1.25 from the buyer’s cash account to the vendor’s cash account.

We believe that this model will be sufficient to represent double entry bookkeeping, though we have not yet tested it thoroughly. We have a (working) ODD file for a first cut at such a “transactionography,” and we hope to have a more refined version for presentation at the TEI meeting in fall 2012.

### Conclusion

Participants in the activities funded with this award remain confident that it will be possible to develop guidelines that account for the variations and idiosyncrasies characteristic of manuscript financial records as well as similar tabular records. Documents in all of these genres represent efforts to keep records with some attention to structure, including in many cases to the principles of double entry bookkeeping.

Standardized digitization of this rich yet currently inaccessible genre of manuscript historical records has the potential to produce harvestable data that could open significant new lines of inquiry about economic, social, and cultural history. With extensive application of standardized markup to such records from diverse places and times, researchers could compare information about continuities and changes in use of commodities and in their values over time and space.

Originally published by Kathryn Tomasek in [July 2012](https://securegrants.neh.gov/publicquery/main.aspx?f=1&gn=HD-51224-11 "NEH Grant Details for 'Encoding Financial Records for Historical Research,' National Endowment for the Humanities").

---

### Selected Bibliography

Adams Family Papers: An Electronic Archive. Massachusetts Historical Society. [http://www.masshist.org/digitaladams/aea/.](http://www.masshist.org/digitaladams/aea/. "Adams Family Papers")

Alcalá Account Book Project. [http://archives.forasfeasa.ie/index.shtml](http://archives.forasfeasa.ie/index.shtml "Alcalá Account Book Project").

Bethlehem Digital History Project. [http://bdhp.moravian.edu/community_records/business/busact.html](http://bdhp.moravian.edu/community_records/business/busact.html "Bethlehem Digital History Project").

Burnard, Lou and Syd Bauman, eds. _TEI P5: Guidelines for Electronic Text Encoding and Interchange. 2.0.2._ 2012-02-02T17:24:24Z. [http://www.tei-c.org/P5/](http://www.tei-c.org/P5/ "Burnard and Bauman, 'TEI P5: Guidelines for Electronic Text Encoding and Interchange'").

Comédie Française Register Project. Massachusetts Institute of Technology. [http://web.mit.edu/hyperstudio/cfr/](http://web.mit.edu/hyperstudio/cfr/ "Comédie Française Register Project").

European Historical Population Samples Network (EHPS-Net). [http://www.esf.org/index.php?id=8361](http://www.esf.org/index.php?id=8361 "European Historical Population Samples Network").

Great Britain Historical Geographic Information System (GBHGIS). [http://www.gbhgis.org/](http://www.gbhgis.org/ "Great Britain Historical GIS").

Mair, John._Book-keeping Methodiz’d; or, A methodical treatise of Merchant-accompts, according to the Italian form. Wherein the theory of the art is fully explained,… To which is added, a large appendix. … 8th ed._ Gale ECCO Print Edition reproduced from the National Library of Scotland. Edinburgh: printed by W. Sands, A. Murray, and J. Cochran, for W. Sands, A. Kincaid & J. Bell, and A. Donaldson, 1765.

McCusker, John J. _How Much Is That in Real Money?: A Historical Price Index for Use as a Deflator of Money Values in the Economy of the United States._ Worcester, Mass.: American Antiquarian Society, 2001.

The Minnesota Population Center’s Integrated Public Use Microdata Series (IPUMS). [http://ipums.org/](http://ipums.org/ "Minnesota Population Center").

National Historic Geographic System. [https://www.nhgis.org/](https://www.nhgis.org/ "National Historic GIS").

Railroads in the Making of Modern America. University of Nebraska. [http://railroads.unl.edu/views/item/rrwork](http://railroads.unl.edu/views/item/rrwork "Railroads in the Making of Modern America").

Thomas Jefferson Papers: An Electronic Archive. [http://www.masshist.org/thomasjeffersonpapers/](http://www.masshist.org/thomasjeffersonpapers/ "Thomas Jefferson Papers").

Visible Prices. [http://www.paigemorgan.net/visibleprices/](http://www.paigemorgan.net/visibleprices/ "Visible Prices").

Papers of George Washington. [http://gwpapers.virginia.edu/project/index.html](http://gwpapers.virginia.edu/project/index.html "Papers of George Washington").

_Wheaton Family Papers_, M089, Wheaton College Archives and Special Collections. Wheaton College, Norton, Massachusetts.

World Customs Organization. Harmonized System. [http://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-online.aspx](http://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-online.aspx "World Customs Organization Harmonized System").

Any views, findings, conclusions, or recommendations expressed in this paper do not necessarily reflect those of the National Endowment for the Humanities.

[^1]: Participants in the August 2011 meeting funded by the award included Syd Bauman, Kurt Fendt, Julia Flanders, Scott P. Hamlin, Nancy Heywood, Ondine LeBlanc, Lauren Pfendner, E. Patrick Rashleigh, Jeff Ravel, Mary Beth Sievens, Jennifer Stertzer, Zephorene L. Stickney, Jacqueline Wernimont, Ronald Zboray, and Mary Saracino Zboray. I am grateful to all of them for fruitful discussions and continued interest in the questions raised here. Further, I wish to thank Syd Bauman for invaluable consultations as we engage in preliminary data modeling. Without Syd’s generosity in sharing his knowledge of TEI structures, none of this work would be possible.

[^2]: Judith A. McGaw, “Accounting for Innovation: Technological Change and Business Practice in the Berkshire County Paper Industry,” _Technology and Culture_, 26/4 (October 1985), 703-725.

[^3]: European Historical Populations Samples Network (EHPS-Net), [http://www.esf.org/index.php?id=8361](http://www.esf.org/index.php?id=8361 "European Historical Population Samples Network").

[^4]: For the early United States, a number of such studies have appeared since 1990, see for example: Christopher Clark, _The Roots of Rural Capital: Western Massachusetts, 1780-1860_ (Ithaca, NY: Cornell University Press, 1990); Charles Sellers, _The Market Revolution: Jacksonian America, 1815-1846_ (New York: Oxford, 1991); Ronald J. Zboray, _A Fictive People: Antebellum Economic Development and the American Reading Public_ (New York: Oxford, 1993); Melvyn Stokes and Stephen Conway, eds.,_The Market Revolution in America: Social, Political, and Religious Expressions_ (Charlottesville, Virginia: University of Virginia Press, 1996); Catherine E. Kelly, _In the New England Fashion: Reshaping Women’s Lives in the Nineteenth Century_ (Ithaca, NY: Cornell University Press, 1999); Ronald J. Zboray and Mary Saracino Zboray, _Literary Dollars and Social Sense: A People’s History of the Mass Market Book_ (New York: Routledge, 2005); Scott C. Martin, ed., _Cultural Change and the Market Revolution in America, 1780-1860_ (Lanham, Md: Rowman and Littlefield, 2005); Marla Miller, _The Needle’s Eye: Women and Work in the Age of Revolution_ (Amherst, Mass.: University of Massachusetts Press, 2006); Stephen Mihm, _A Nation of Counterfeiters: Capitalists, Con Men, and the Making of the United States_ (Cambridge, Mass.: Harvard University Press, 2007); Jane Kamensky, _The Exchange Artist: A Tale of High-Flying Speculation and America’s First Banking Collapse_ (New York: Penguin, 2008); Ellen Hartigan-O’Connor, _Ties That Buy: Women and Commerce in Revolutionary America_ (Philadelphia, Penn.: University of Pennsylvania Press, 2009); Seth Rockman, _Scraping By: Wage Labor, Slavery, and Survival in Early Baltimore_ (Baltimore, Md.: The Johns Hopkins University Press, 2009).

[^5]: The Alcalá Account Book Project, [http://archives.forasfeasa.ie/index.shtml](http://archives.forasfeasa.ie/index.shtml "Alcalá Account Book Project").

[^6]: In addition to projects undertaken by professional historians, a family history project has led software developer Ben Brumberg to explore the uses of TEI/XML for marking up financial records. A sample page from the manuscript he is working with can be found here: [http://archive.org/stream/Jeremiah_White_Graves_Diary_V olume_2_Book_01/JWGravesV ol2Book01#p age/n17/mode/1up](http://archive.org/stream/Jeremiah_White_Graves_Diary_V olume_2_Book_01/JWGravesV ol2Book01#p age/n17/mode/1up "Jeremiah White Graves Diary").

[^7]: John J. McCusker, _How Much Is That in Real Money?: A Historical Price Index for Use as a Deflator of Money Values in the Economy of the United States_ (Worcester, Mass.: American Antiquarian Society, 2001).

[^8]: For the significance of questions of standardization and normalization, see Syd Bauman, “Interchange vs. Interoperability,” presented at Balisage: The Markup Conference 2011, Montréal, Canada, August 2 -5, 2011. In _Proceedings of Balisage: The Markup Conference 2011, Balisage Series on Markup Technologies, vol. 7_ (2011), doi:10.4242/BalisageVol7.Bauman01.

[^9]: For discussion of the work of running a boardinghouse, see Wendy Gamber, _The Boardinghouse in Nineteenth-Century America_ (Baltimore, Md.: The Johns Hopkins University Press, 2007).
