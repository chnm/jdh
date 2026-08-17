+++
title = "Code Appendix for “Digital Ethnography”"
slug = "code-appendix-for-digital-ethnography"
type = "article"
date = 2014-03-01
issue = "3-1"
volume = 3
number = 1
season = "Spring"
year = 2014
section = "Features"
section_url = "/category/3-1/features-3-1/"
section_weight = 3
weight = 4
authors = ["Wendy F. Hsu"]
author_ids = ["whsu"]
author = ["whsu"]
+++

`require 'rubygems'
require 'mechanize'
require 'geokit'
include Geokit::Geocoders`

`# intitialize agent and open page
agent = Mechanize.new`

# create a .txt file to save the results of the program in  
 filename = 'MyspaceFriendListnew.txt'  
 File.open filename, 'w' do |f|

f.puts "lat\\tlon\\ttitle\\tdescription\\ticonSize\\ticonOffset\\ticon"

friend_pagenumber = 1  
 # Fill in the starting page number of friend result pages  
 BandName = 'thekominas'  
 # Fill in the friendId of the band  
 band_url = 'http://myspace.com/' + BandName + '/friends/all/page/' + friend_pagenumber.to_s  
 page = agent.get(band_url)

count = 1

# loop through all the pages by clicking the 'next page' button as long as one exists  
 begin

next_flag = FALSE  
 count += 1

# find each friend  
 page.search('div[@class = "details"]').each do |friend|  
 geodone = FALSE

# print each friend's name  
 # make sure that each friend has an actual name  
 if friend.search('a[@class = "msProfileTextLink"]').first  
 friend_name = friend.search('a[@class = "msProfileTextLink"]').first.text  
 else  
 friend_name = ""  
 end

# print each friend's profile id  
 friend_url = friend.search('a[@class = "msProfileTextLink"]/@href').first

puts friend_name

begin # begin find friend page and geolocate

friend_page = agent.get(friend_url)

if friend_page.search('//p[@class="even Location"]//text()').text

friend_page.search('//p[@class="even Location"]//text()').each do |item|

unless(item.content.include?('Profile Views') || item.content.include?('Last Login') ||  
 item.content.include?('years old') || item.content.include?('Male') ||  
 item.content.include?('Female') || item.content.include?('jello') ||  
 item.content.include?('coming soon') || item.content.include?('BANG BANG!') ||  
 item.content.include?('MyHot') || item.content.include?('View My') ||  
 item.content.include?('One Foot On') || item.content.include?('new beginning') ||  
 item.content.include?('padia') || item.content.include?('recording') ||  
 item.content.include?('grave') || item.content.include?('http://') ||  
 item.content.include?('RIP') || item.content.include?('Haad?') ||  
 item.content.include?('Hello.') || item.content.include?('OPA!') ||  
 item.content.include?('Here and Now') || item.content.include?('i, am') ||  
 item.content.include?('Kveldubach') || item.content.include?('Tiger baby') ||  
 item.content.include?('Misanthrope') || item.content.include?('D.I.Y.') ||  
 item.content.include?('Thrashing') || item.content.include?('Fire mares') ||  
 item.content.include?('studioAKT') || item.content.include?('Aloha!') ||  
 item.content.include?('Lost') || item.content.include?('3rd world') ||  
 item.content.include?('ane amma') || item.content.include?('deux') ||  
 item.content.include?('Millennium') || item.content.include?('realest') ||  
 item.content.include?('........°L°......') || item.content.include?('original') ||  
 item.content.include?('760') || item.content.include?('dead') ||  
 item.content.include?('~~~') || item.content.include?('One people!') ||  
 item.content.include?('Yeah!') ||  
 item.content.gsub(/[\\s,\\n]/,'').eql?('') || geodone)  
 loc_info = item.content.strip  
 loc=GoogleGeocoder.geocode(loc_info)

if loc.success?  
 f.puts loc.lat.to_s + "\\t" + loc.lng.to_s + "\\t" + friend_name + "\\t" + loc_info + " " + friend_url + "\\t21,25\\t-10,-25\\thttp://www.openlayers.org/dev/img/marker.png"  
 geodone = TRUE  
 end # end if loc...

end # end unless

end # end if friend_page...

else  
 begin  
 loc_info = friend_page.search('//li[@class="adr"]').first.content.strip  
 rescue  
 puts "*** Failed page search for geoinfo on alt page ***"  
 end  
 loc=GoogleGeocoder.geocode(loc_info)

if loc.success?  
 f.puts loc.lat.to_s + "\\t" + loc.lng.to_s + "\\t" + friend_name + "\\t" + loc_info + " " + friend_url + "\\t21,25\\t-10,-25\\thttp://www.openlayers.org/dev/img/marker.png"  
 geodone = TRUE  
 end

end

rescue  
 puts '***  Error!!!  ***'  
 end  # end find friend page and geolocate

end  
 puts '*** This concludes friend result on page ' + friend_pagenumber.to_s + ' ***'

# Retrieve next page if one exists  
 if page.search('a[class = "pageBtn nextBtn"]')  
 next_flag = TRUE  
 friend_pagenumber = friend_pagenumber.to_i + 1  
 band_url = 'http://myspace.com/' + BandName + '/friends/all/page/' + friend_pagenumber.to_s  
 page = agent.get(band_url)  
 end

# keep looping if there's a next page and we haven't surpassed the max number of hits  
 end while next_flag

end
