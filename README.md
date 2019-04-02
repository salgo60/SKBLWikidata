Task [T219700](https://phabricator.wikimedia.org/T219700) "*ISNI i SKBL <-> Wikidata*"
## KARP - Wikidata

 

KARP is a database that contains profiles from SKBL ( [The Biographical Dictionary of Swedish Women](https://skbl.se/en/about-skbl) ). Wikidata is already connected to all records in SKBL using the [property 4963](https://www.wikidata.org/wiki/Property_talk:P4963) ( [see blog](http://minancestry.blogspot.com/2018/03/svenskt-kvinnobiografiskt-lexikon.html) )

This [task](https://phabricator.wikimedia.org/T219700) is for checking consistency between data in SKBL and Wikidata (WD) regarding ISNI (compare how simple the same solution is with [SPARQL Federated search](https://phabricator.wikimedia.org/T200668) see [WD <-> Nobelprize using Federated search](https://www.wikidata.org/wiki/User:Salgo60/ListeriaNobelData3) )

### KARP
* [Nättjänst](https://spraakbanken.gu.se/swe/Forskning/Infrastruktur/Karp/N%C3%A4ttj%C3%A4nst/n%C3%A4ttj%C3%A4nst)
* Github [skbl-portal](https://github.com/spraakbanken/skbl-portal)
* Access data in KARP
 * Get all records 
   * [ws.spraakbanken.gu.se/ws/karp/v4/minientry?mode=skbl&q=extended||and|namn.search|exists&resource=skbl&show=name,lifespan&size=10000&start=0](https://ws.spraakbanken.gu.se/ws/karp/v4/minientry?mode=skbl&q=extended%7C%7Cand%7Cnamn.search%7Cexists&resource=skbl&show=name,lifespan&size=10000&start=0)
 * KARP 
   * KARP.url = "GertrudAdelborg" 
   * KARP.id =  [AVUB3uB9oXI9ppygjor0](https://skbl.se/sv/artikel/AVUB3uB9oXI9ppygjor0.json) 
#### KARP <-> Wikidata 
   * Wikidata [P4963](https://www.wikidata.org/wiki/Property_talk:P4963) contains the value of KARP.url
     * --> [haswbstatement:P4963=GertrudAdelborg](https://www.wikidata.org/w/index.php?search=haswbstatement%3AP4963%3DGertrudAdelborg&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns120=1) --> Wikidata [Q4933813](https://www.wikidata.org/wiki/Q4933813) --> sv:Wikipedia [Gertrud Adelborg](https://sv.wikipedia.org/wiki/Gertrud_Adelborg)
     * or use the [hub tool](https://tools.wmflabs.org/hub) with P4963 and the value in KARP.url [tools.wmflabs.org/hub/P4963:GertrudAdelborg?lang=sv](https://tools.wmflabs.org/hub/P4963:GertrudAdelborg?lang=sv)
        * same with the Q number [tools.wmflabs.org/hub/Q4933813?lang=sv](https://tools.wmflabs.org/hub/Q4933813?lang=sv)
        * same with [ISNI P213](https://www.wikidata.org/wiki/Property_talk:P213) = [tools.wmflabs.org/hub/P213:0000 0000 4761 5839?lang=sv](http://tools.wmflabs.org/hub/P213:0000%200000%204761%205839?lang=sv)
        * same with [LIBRIS P906](https://www.wikidata.org/wiki/Property_talk:P906) = 404084 -> SKBL P4963 [tools.wmflabs.org/hub/P906:404084?property=P4963](http://tools.wmflabs.org/hub/P906:404084?property=P4963)
        * same with [SBL P3217](https://www.wikidata.org/wiki/Property_talk:P3217) = 5517 -> SKBL P4963 [tools.wmflabs.org/hub/P3217:5517?property=P4963](http://tools.wmflabs.org/hub/P3217:5517?property=P496)
           * SKBL P4963 = GertrudAdelborg --> SBL P3217 [tools.wmflabs.org/hub/P4963:GertrudAdelborg?property=P3217](http://tools.wmflabs.org/hub/P4963:GertrudAdelborg?property=P3217)
      * [List of Wikidata](http://tinyurl.com/y33z9466) / KARP.url / LIBRIS / ISSNI / SBL - [link query](https://goo.gl/2ffJwf)
      * [List of external identifiers in WIkidata](http://tinyurl.com/yybaazal) for profiles linked to SKBL see also [blog](http://minancestry.blogspot.com/2018/03/svenskt-kvinnobiografiskt-lexikon.html)

![](https://github.com/salgo60/SKBLWikidata/blob/master/External.png?raw=true "[External identifiers](http://tinyurl.com/yybaazal))") 
##### KARP <-> Wikidata sources e.g. Riksarkivet
* next step is to also define sources with Unique identifiers so they can be machinereadable and compared
  * a small test with +300 SKBL profiles whith sources in Riksarkivet Wikidata as Wikidata reference for facts
      * [list with links](http://tinyurl.com/y2hpdscg) Riksarkivet ( [the query](https://goo.gl/SupVkQ))
## Using what WIkidata knows about 
Wikidata is connected to +3000 external sources see [list of SKBL profiles](http://tinyurl.com/y2nfoswl) below some examples how that can be used to find candidates fr new profiles
### KARP <-> Wikidata <-> Digital Museums
As we move in the direction of more digital also some museums starts add collections avalaible on the net as sites like [Digitalmuseum.org](https://digitaltmuseum.org/). In Wikidata we store an identifier called Kulturnav and if the museums that upload data to Digitalmuseum is doing it in the "correct" way we could easy find collections for a person
* Example
  * SKBL [LeaAhlborn](https://www.skal.png?raw=truebl.se/sv/artikel/LeaAhlborn) = [kulturnav Ahlborn, Lea (1826 - 1897)](http://kulturnav.org/569ae578-d8d8-4260-a6d3-e67f8ffb7bda) = Digital museum [ahlborn-lea-1826-1897](https://digitaltmuseum.se/021036372385/ahlborn-lea-1826-1897)
  * [List](http://tinyurl.com/y4qtlfms) ordered after how many articles Wikipedia have about the person in different languages
My feeling is that its a small chaos if museums links or not links a person. I guess its some education needed, better userinterfaces and also better understanding of the possibilities of the Digital landscape
### KARP <-> Wikidata <-> Signaturer.se [P5316](https://www.wikidata.org/wiki/Property_talk:P5316)
* Example
  * SKBL [AnnaBoberg](https://www.skbl.se/sv/artikel/AnnaBoberg) = Signaturer.se [AnnaBoberg](http://www.signaturer.se/Sverige/AnnaBoberg.htm)
  * [List](http://tinyurl.com/y2m8twb9) 
### KARP <-> Wikidata <-> Nationalmuseum [P2538](https://www.wikidata.org/wiki/Property_talk:P2538)
* Example 
  * SKBL [HilmaafKlint](https://www.skbl.se/sv/artikel/HilmaafKlint) = Nationalmuseum [18466](http://emp-web-84.zetcom.ch/eMP/eMuseumPlus?service=ExternalInterface&module=artist&objectId=18466)
  * [List](http://tinyurl.com/yxcpg6yl)
     * [List](http://tinyurl.com/y6kqe9gm) female, swedish women who has passed away and is NOT in SKBL ordered by articles in Wikipedia
     * [Same query but sorted by death date](http://tinyurl.com/y4uhg5gp)
### KARP <-> Wikidata <-> Spotify [P1902](https://www.wikidata.org/wiki/Property_talk:P1902)
* Example 
  * SKBL [ZarahLeander](https://www.skbl.se/sv/artikel/ZarahLeander) = Spotify [5R15K0QUPe4AhP1vaPoaX3](https://open.spotify.com/artist/5R15K0QUPe4AhP1vaPoaX3)
  * [List](http://tinyurl.com/y68adnky)
     * [List](http://tinyurl.com/y3yamvth) female, swedish women who has passed away and is NOT in SKBL ordered by number of articles in Wikipedia
     * [Same query but sorted by death date](http://tinyurl.com/yyto3pal)
### KARP <-> Wikidata <-> Svenskt Översättarlexikon [P5147](https://www.wikidata.org/wiki/Property_talk:P5147)
* Example 
  * SKBL [HedvigCharlottaNordenflycht](https://www.skbl.se/sv/artikel/HedvigCharlottaNordenflychtÖversättar) = Svenskt Översättarlexikon [Hedvig_Charlotta_Nordenflycht](https://litteraturbanken.se/%C3%B6vers%C3%A4ttarlexikon/artiklar/Hedvig_Charlotta_Nordenflycht)
  * [List](http://tinyurl.com/y4n99gjy)
     * [List](http://tinyurl.com/y4leqwks) female, past away but NOT in SKBL ordered by number of articles in Wikipedia
### KARP <-> Wikidata <-> SOK [P2323](https://www.wikidata.org/wiki/Property_talk:P2323)
* Example 
  * SKBL [GretaJohansson](https://www.skbl.se/sv/artikel/GretaJohansson) = SOK [greta-johanson](https://sok.se/idrottare/idrottare/g/greta-johanson.html)
  * [List](http://tinyurl.com/y325kqst)
     * [List](http://tinyurl.com/y3qgu62u) female, past away part in SOK but NOT in SKBL ordered by number of articles in Wikipedia
     * [Same query but sorted by death date](http://tinyurl.com/yyde2sxn)

### KARP <-> Wikidata <-> Litteraturbanken [P5101](https://www.wikidata.org/wiki/Property_talk:P5101)
Status in Wikidata is that Litteraturbanken [P5101](https://www.wikidata.org/wiki/Property_talk:P5101) needs some cleaning....
* Example 
  * SKBL [SelmaLagerlof](https://www.skbl.se/sv/artikel/SelmaLagerlof) = Litteraturbanken [LagerlofS](https://litteraturbanken.se/forfattare/LagerlofS)
  * [List](http://tinyurl.com/y5djjq4r)
     * [List](http://tinyurl.com/y2p659r7) female, past away part in Litteraturbanken but NOT in SKBL ordered by number of articles in Wikipedia
     
### KARP <-> Wikidata <-> Nobel Prize Nomination [P3360](https://www.wikidata.org/wiki/Property_talk:P3360)
* Example 
  * SKBL [SelmaLagerlof](https://www.skbl.se/sv/artikel/SelmaLagerlof) = Nobel Prize Nomination [5152](https://www.nobelprize.org/nomination/redirector/?redir=archive/show_people.php&id=5152)
  * [List](http://tinyurl.com/yxq64zj8)
     * [List](http://tinyurl.com/y2rd6ojm) female, past away with Nobel Prize Nomination in Wikidata but NOT in SKBL ordered by number of articles in Wikipedia

# The program
To use add Wikidata login to [user-config.py](https://github.com/salgo60/SKBLWikidata/blob/master/user-config.py)

The program

1. Gets [all records from Karp SKBL](https://ws.spraakbanken.gu.se/ws/karp/v4/minientry?mode=skbl&q=extended%7C%7Cand%7Cnamn.search%7Cexists&resource=skbl&show=name,lifespan&size=10000&start=0)
    1. try to decode ISNI ([get_isni](https://github.com/salgo60/SKBLWikidata/blob/master/get_SKBL.py))
1. Gets Wikidata record and ISNI in Wikidata ([get_wikidata](https://github.com/salgo60/SKBLWikidata/blob/master/get_Wikidata.py))
1. Logs potential mismatches to the [/log file](https://github.com/salgo60/SKBLWikidata/tree/master/log)
1. Writes a csv file [skbl.csv](https://github.com/salgo60/SKBLWikidata/blob/master/skbl.csv) with the following columns
    1. Karp.url = Wikidata [P4963](https://www.wikidata.org/wiki/Property_talk:P4963) e.g. MargitAbenius
    1. Karp.id
    1. SKBL ISNI (format 9999 9999 9999 9999 )
    1. Wikidata Q number e.g. [Q4933592](https://www.wikidata.org/wiki/Q4933592)
    1. Wikidata ISNI

# Wikidata actions
1. Updated wrong ISNI added missing
1. Oddities found in SKBL
    1. [AVmr017w7hONWjeN9oCA](https://skbl.se/sv/artikel/AVmr017w7hONWjeN9oCA.json) ISNI number containes also text ISNI
    1. See section below Action SKBL see also task [T219706](https://phabricator.wikimedia.org/T219706)
    
# Lesson learned
1. Writing software that should parse JSON and take care of odd implementations like KARP ISNI were **00000000** is no ISNI found. Take much more time than having a SPARQL endpoint and use Federated search see [Task T200668](https://phabricator.wikimedia.org/T200668) and [Nobelprize.org](https://www.wikidata.org/wiki/User:Salgo60/ListeriaNobelData3)
1. Start comparing and sharing data will make the quality better for everyone and make life easier for the next person that should use this data
1. Starting using linked data for people, places instead strings will be a game changer [Europeana Linked Open Data - What is it?](https://vimeo.com/36752317) se [Task T218782](https://phabricator.wikimedia.org/T218782)

## Next step
1. Compare more data between SKBL and Wikidata
1. Start a dialogue what is good implementation of LOD or not
1. Find better patterns I feel SPARQL endpoint is easy and in Wikidata we have out of the box support for Listera lists see [video in Swedish](https://youtu.be/jOtrlb1KRP8) and how [we every night compare Wikidata and the Nobelprize.org](https://www.wikidata.org/wiki/User:Salgo60/ListeriaNobelData3) - Task [T200668](https://phabricator.wikimedia.org/T200668)
1. Also get tighter collaborations between different projects 
    1. SKBL writes about [Lilli Zickerman](https://www.skbl.se/sv/artikel/LilliZickerman) and Nordiska has [new material](https://twitter.com/sveren/status/1106851525375287301) - help each other to be more visible and dont be scare linking is my feeling see [tweet](https://twitter.com/salgo60/status/1107959251505479681) and also start thinking what can attract Wikipedia as they have a lot of visitors (2019 profiles related to SKBL had 13 481 viewers per day)
    1. In Wikidata we document signs of litterature in Stockholm see [link](https://sv.wikipedia.org/wiki/Anv%C3%A4ndare:Salgo60/Listeria/Det_litter%C3%A4ra_Stockholm) - maybe this could be an input to SKBL what people should be documented next time and when planning signs also look how they relates to SKBL/Litteraturbanken
    1. See also [blogpost](http://minancestry.blogspot.com/2019/03/wikipediawikidata-digitaltmuseum.html) how Wikidata can be used to get some interesting statistics
       1. example [search in Wikidata for female Swedish persons who has died and have most articles and are not part of SKB](https://goo.gl/2qnzxo) - in Swedish a [Video](https://www.youtube.com/watch?v=SCk39XvzvNs)
    
## Action SKBL see also task [T219706](https://phabricator.wikimedia.org/T219706)
1. Mismatches that maybe needs action at SKBL Task [T219706](https://phabricator.wikimedia.org/T219706)
    1. http://www.wikidata.org/wiki/Q4954113 
        1. SKBL: https://skbl.se/sv/artikel/AV44Ec_tDqWJ2eBq92nx.json		  
        1. WD ISNI: 0000 0000 5186 9858 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q16595323 
        1. SKBL: https://skbl.se/sv/artikel/AWBPP4z-WxymAE2pjnvP.json		  
        1. WD ISNI: 0000 0000 1701 7221 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q4956130 
        1. SKBL: https://skbl.se/sv/artikel/AVvxOGQx6HF5HgpJZ2w9.json		  
        1. WD ISNI: 0000 0003 6825 4210 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q50804907 
        1. SKBL: https://skbl.se/sv/artikel/AV_9nDubjP4rR07fm2xo.json		  
        1. WD ISNI: 0000 0003 8182 3780 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q50803502 
        1. SKBL: https://skbl.se/sv/artikel/AVuf7Lxgi-B3PHNCX9VD.json		  
        1. WD ISNI: 0000 0000 3262 2657 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q4970779 
        1. SKBL: https://skbl.se/sv/artikel/AWEDRVoDWxymAE2pjnyo.json		  
        1. WD ISNI: 0000 0001 0463 2783 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q50846445 
        1. SKBL: https://skbl.se/sv/artikel/AVyMLsea6HF5HgpJZ2y9.json		  
        1. WD ISNI: 0000 0003 7794 8716 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q16596123 
        1. SKBL: https://skbl.se/sv/artikel/AWFv7UtfWxymAE2pjn2w.json		  
        1. WD ISNI: 0000 0004 3982 9828 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q4974163 
        1. SKBL: https://skbl.se/sv/artikel/AVmr017w7hONWjeN9oCA.json		  
        1. WD ISNI: 0000 0000 5303 1792 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q13563726 
        1. SKBL: https://skbl.se/sv/artikel/AWFrNzKKWxymAE2pjn2Q.json		  
        1. WD ISNI: 0000 0000 5184 7851 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q4976815 
        1. SKBL: https://skbl.se/sv/artikel/AWEDkKK1jP4rR07fm24c.json		  
        1. WD ISNI: 0000 0000 1218 5656 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q4976841 
        1. SKBL: https://skbl.se/sv/artikel/AV9sGgqZWxymAE2pjnoD.json		  
        1. WD ISNI: 0000 0000 5196 8258 SKBL ISNI: 0000000137251661
        1. Looks like she has 2 ISNI
    1. http://www.wikidata.org/wiki/Q4979129 
        1. SKBL: https://skbl.se/sv/artikel/AWED1FSwWxymAE2pjnyw.json		  
        1. WD ISNI: 0000 0001 0915 0425 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q4990100 
        1. SKBL: https://skbl.se/sv/artikel/AV3p525ZDqWJ2eBq92mK.json		  
        1. WD ISNI: 0000 0001 0966 715X SKBL ISNI: 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/salgo60/SKBLWikidata/master)
