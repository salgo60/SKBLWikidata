Task [T219700](https://phabricator.wikimedia.org/T219700) "*ISNI i SKBL <-> Wikidata*"
## KARP - Wikidata

 

KARP is a database that contains profiles from SKBL ( [The Biographical Dictionary of Swedish](https://skbl.se/en/about-skbl) ). Wikidata is already connected to all records in SKBL using the [property 4963](https://www.wikidata.org/wiki/Property_talk:P4963) ( [see blog](http://minancestry.blogspot.com/2018/03/svenskt-kvinnobiografiskt-lexikon.html) )

This [task](https://phabricator.wikimedia.org/T219700) is for checking consistency between data in SKBL and WD regarding ISNI (compare [WD <-> Nobelprize using Federated search](https://www.wikidata.org/wiki/User:Salgo60/ListeriaNobelData3) )

### KARP
* [Nättjänst](https://spraakbanken.gu.se/swe/Forskning/Infrastruktur/Karp/N%C3%A4ttj%C3%A4nst/n%C3%A4ttj%C3%A4nst)
* Github [skbl-portal](https://github.com/spraakbanken/skbl-portal)
* Access data in KARP
 * Get all records 
   * [ws.spraakbanken.gu.se/ws/karp/v4/minientry?mode=skbl&q=extended||and|namn.search|exists&resource=skbl&show=name,lifespan&size=10000&start=0](https://ws.spraakbanken.gu.se/ws/karp/v4/minientry?mode=skbl&q=extended%7C%7Cand%7Cnamn.search%7Cexists&resource=skbl&show=name,lifespan&size=10000&start=0)
 * KARP url = "AlmaAbrahamsson" 
   * id =  [AV-6FkE-WxymAE2pjnq5](https://skbl.se/sv/artikel/AV-6FkE-WxymAE2pjnq5.json) 

   * --> Wikidata P4963 --> [haswbstatement:P4963=AlmaAbrahamsson](https://www.wikidata.org/w/index.php?search=haswbstatement%3AP4963%3DAlmaAbrahamsson&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns120=1) --> Wikidata [Q50806808](https://www.wikidata.org/wiki/Q50806808)
### The program
To use add Wikidata login to user-config.py

The program

1. Gets all records from Karp SKBL
    1. try to decode ISNI
1. Gets Wikidata record and ISNI in Wikidata
1. Logs potential mismatches in the /log file
1. Writes a csv file skbl.csv

### Wikidata actions
1. Updated wrong ISNI added missing
1. Oddities found in SKBL
    1. [AVmr017w7hONWjeN9oCA](https://skbl.se/sv/artikel/AVmr017w7hONWjeN9oCA.json) ISNI number containes also ISNI
    1. [LydiaWahlstrom](https://www.skbl.se/sv/artikel/LydiaWahlstrom) miss [ISNI 0000 0001 0966 715X](https://tools.wmflabs.org/wikidata-externalid-url/?p=213&url_prefix=http://isni.org/&id=0000+0001+0966+715X)
    
## Lesson learned
1. Writing software that should parse JSON and take care of odd implementations like KARP ISNI were **00000000** is no ISNI found. Take much more time than having a SPARQL endpoint and use Federated search see [Task T200668](https://phabricator.wikimedia.org/T200668) and [Nobelprize.org](https://www.wikidata.org/wiki/User:Salgo60/ListeriaNobelData3)
1. Start comparing and sharing data will make the quality better for everyone and make life easier for the next person that should use this data
1. Starting using linked data for people, places instead strings will be a game changer [Europeana Linked Open Data - What is it?](https://vimeo.com/36752317) se [Task T218782](https://phabricator.wikimedia.org/T218782)

## Next step
1. Compare more data between SKBL and Wikidata
1. Start a dialogue what is good implementation of LOD or not
1. Find better patterns I feel SPARQL endpoint is easy and in Wikidata we have out of the box support for Listera lists see [video in Swedish](https://youtu.be/jOtrlb1KRP8)
1. Also get tighter collaborations between different projects 
    1. SKBL writes about [Lilli Zickerman](https://www.skbl.se/sv/artikel/LilliZickerman) and Nordiska has [new material](https://twitter.com/sveren/status/1106851525375287301) - help each other to be more visible and dont be scare linking see [tweet](https://twitter.com/salgo60/status/1107959251505479681)
    1. We document signs of litterature in Stockholm [link](https://sv.wikipedia.org/wiki/Anv%C3%A4ndare:Salgo60/Listeria/Det_litter%C3%A4ra_Stockholm) - maybe plan togehter what authors SKBL writes about and new planned signs look how they relates to SKBL/Litteraturbanken
    
## Action SKBL see also task [T219706](https://phabricator.wikimedia.org/T219706)
1. Mismatches that maybe needs action at SKBL Task; xxxxx
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
    1. http://www.wikidata.org/wiki/Q4979129 
        1. SKBL: https://skbl.se/sv/artikel/AWED1FSwWxymAE2pjnyw.json		  
        1. WD ISNI: 0000 0001 0915 0425 SKBL ISNI: 
    1. http://www.wikidata.org/wiki/Q4990100 
        1. SKBL: https://skbl.se/sv/artikel/AV3p525ZDqWJ2eBq92mK.json		  
        1. WD ISNI: 0000 0001 0966 715X SKBL ISNI: 
