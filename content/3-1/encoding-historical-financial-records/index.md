+++
title = "Encoding Historical Financial Records"
slug = "encoding-historical-financial-records"
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
weight = 7
authors = ["Kathryn Tomasek", "Syd Bauman"]
author_ids = ["ktomasek", "syd-bauman"]
author = ["ktomasek", "syd-bauman"]
+++

### Poster

<iframe class="gde-frame" scrolling="no" src="https://docs.google.com/viewer?url=http%3A%2F%2Fjournalofdigitalhumanities.org%2Fwp-content%2Fuploads%2F2014%2F01%2Ftomasek.pdf&amp;hl=en_US&amp;embedded=true" style="width:100%; height:500px; border: none;"></iframe>

[Download (PDF, 817KB)](/wp-content/uploads/2014/01/tomasek.pdf)

### Abstract

A significant number of scholars in Europe and North America are now involved in projects utilizing or encoding historical financial and tabular records. Many of them hope that it will be possible to develop guidelines that account for both the idiosyncrasies of such manuscripts and the semantic information embedded in them.

Historical financial records (HFRs), a genre of primary sources that includes such materials as bills, receipts, cashbooks, journals, and account ledgers, are abundant in traditional archives. Most current digitization projects do not capture the full range of financial information, and if they do, they have yet to develop a common method for fully expressing this range.

HFRs share certain structural characteristics with such other genres of historical records as plague bills, theatre returns, and probate records. Documents from such genres are generally represented as lists or tables, and in many cases they include numerical sums. The apparent regularity of these documents presents perhaps the most significant challenge for those who seek to encode them, as it often collapses in use. Thus such tabular records tend to include information that cannot be represented through simple transcription of tabular layout. In fact, they tend to contain significant variations and idiosyncrasies, often within the same document or collection.

In the subgenre of double entry accounts, the impulse to keep regular records produced a set of standards for recording financial information. Through the centuries, various influential texts offered ordinary businessmen opportunities to learn how to keep regular accounts. But the popularity of these texts did not guarantee perfect adherence to their principles.

HFRs tend to include three levels of data to consider: layout, textual expression, and a third, more abstract level of financial semantics that are not as yet easily captured through TEI conformant markup. Attention to layout and textual expression may or may not be necessary. In cases where page images are included in online publication, for example, some projects may choose to omit digital representations of layout. Similarly, different projects place emphasis on particular textual features.

At the more abstract level, double entry bookkeeping uses a specialized vocabulary, a professional jargon that requires data modeling with attention to the special meanings of the terms “debtor” and “creditor,” as well as the relationships between transactions recorded in the journal and accounts kept in a separate ledger. We are developing a TEI customization for conveying such meanings and their expressions within double entry account books through a “transactionography” that will represent the relationships among such records in abstracted form.

As currently conceived a “transactionography,” like a “personography,” provides information about the financial information within each transaction separately from the transcribed text. “Transactionographies” follow the principles of double entry accounting to model transactions as a sequence of one or more transfers of anything of value from one account to another. Thus, the simple purchase of a candy bar from a convenience store is represented as two transfers: one of a candy bar from the vendor’s stock account to the buyer, and one of $1.25 from the buyer’s cash account to the vendor’s cash account.

We believe that this model will be sufficient to represent double entry bookkeeping, though we have not yet tested it thoroughly. We presented a (working) ODD file for a first cut at such a “transactionography” at the TEI meeting in fall 2012, and we had a more refined version for presentation at DH2013. (Customization files are available at [http://www.customization.encodinghfrs.org/](http://www.customization.encodinghfrs.org/).)

This abstract only begins to suggest the research opportunities that might eventually be available should large numbers of HFRs be digitally accessible in machine processable form. As editors of the Alcalá Account Book Project have noted with regard to their digital edition of the account books of the Royal Irish College of Saint George the Martyr in Alcalá, such records promise “insight into the day-to-day running of the college with valuable information on diet, discipline, and domestic matters.” Standardized digitization of HFRs, a rich yet currently inaccessible genre of texts, has the potential to produce harvestable data that could open significant new lines of inquiry about economic, social, and cultural history.

This poster was originally presented at DH2013 on [July 17, 2013](http://dh2013.unl.edu/abstracts/ab-445.html "Abstracts DH2013").

### Selected Bibliography

The Alcalá Account Book Project. [http://archives.forasfeasa.ie/index.shtml](http://archives.forasfeasa.ie/index.shtml "Alcala Account Book Project").

Burnard, Lou and Syd Bauman, eds. _TEI P5: Guidelines for Electronic Text Encoding and Interchange_. Release 2.0.2. 2012-02-02 T17:24:24Z. [http://www.tei-c.org/P5/](http://www.tei-c.org/P5/ "TEI P5").

Gleeson-White, Jane. _Double Entry: How the Merchants of Venice Created Modern Finance._ (New York: Norton, 2011).

Mair, John. _Book-keeping Methodiz’d; or, A Methodical Treatise of Merchant-accompts, According to the Italian Form. Wherein the Theory of the Art is Fully Explained,… To Which is Added, a Large Appendix._ … 8th ed. Gale ECCO. Print Edition reproduced from the National Library of Scotland. (Edinburgh: printed by W. Sands, A. Murray, and J. Cochran, for W. Sands, A. Kincaid & J. Bell, and A. Donaldson, 1765).

McCusker, John J. _How Much Is That in Real Money?: A Historical Price Index for Use as a Deflator of Money Values in the Economy of the United States._ (Worcester, Mass.: American Antiquarian Society, 2001).

Pacioli, Luca. _The Rules of Double-Entry Bookkeeping: Particularis de computis et scripturis._ Michael Schemmann, ed. (Orig. pub. 1494. International Institute of Certified Public Accountants, 2012).

Poovey, Mary. _Genres of the Credit Economy: Mediating Value in Eighteenth- and Nineteenth- Century Britain_. (Chicago, Ill.: University of Chicago Press, 2008).

Visible Prices: A Collection of Literary and Historical Economic Information. [http://staff.washington.edu/paigecm/vp](http://staff.washington.edu/paigecm/vp "Genres of the Credit Economy").
