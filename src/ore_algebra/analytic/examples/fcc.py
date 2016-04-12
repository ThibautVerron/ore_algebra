r"""
Face-centered cubic lattices

The following examples are adapted from Koutschan's study of the face-centered
cubic lattice (Ch. Koutschan, Lattice Green's Functions of the
Higher-Dimensional Face-Centered Cubic Lattices, J. Phys. A: Math. Theor. 46
(2013) 125005, arXiv:1108.2164). ::

    sage: from ore_algebra import *
    sage: from ore_algebra.analytic.ui import *
    sage: Dops, z, Dz = Diffops("z")

Koutschan shows that the lattice Green's function (LGF) of the four-dimensional
face-centered cubic is annihilated be the following operator::

    sage: dop4 = ((-1 + z)*z^3*(2 + z)*(3 + z)*(6 + z)*(8 + z)*(4 + 3*z)^2*Dz^4
    ....:   + 2*z^2*(4 + 3*z)*(-3456 - 2304*z + 3676*z^2 + 4920*z^3 + 2079*z^4
    ....:   + 356*z^5 + 21*z^6)*Dz^3
    ....:   + 6*z*(-5376 - 5248*z + 11080*z^2 + 25286*z^3 + 19898*z^4 + 7432*z^5
    ....:   + 1286*z^6 + 81*z^7)*Dz^2
    ....:   + 12*(-384 + 224*z + 3716*z^2 + 7633*z^3 + 6734*z^4 + 2939*z^5
    ....:   + 604*z^6 + 45*z^7)*Dz
    ....:   + 12*z*(256 + 632*z + 702*z^2 + 382*z^3 + 98*z^4 + 9*z^5))

Using this differential equation, he computes the value of the LGF at z=1 (and
from there the return probability of the lattice)::

    sage: eval_diffeq(dop4, [0, 0, 0, 1], [0, 1], 1e-60) # long time (4.5 s)
    [1.10584379792120476018299547088585107443954623663875285836499...]
    + [+/- ...]*I

(The result is complex even though that particular solution is real-valued
because some local solutions involve logarithms.)

Similarly, in dimension five, Koutschan obtains::

    sage: dop5 = (
    ....:   16*(-5 + z)*(-1 + z)*z^4*(5 + z)^2*(10 + z)*(15 + z)*(5 + 3*z)*
    ....:   (-675000 + 3465000*z - 1053375*z^2 + 933650*z^3 + 449735*z^4 +
    ....:   144776*z^5 + 15678*z^6)*Dz^6
    ....: + 8*z^3*(5 + z)*(-354375000000 + 1774828125000*z - 503550000000*z^2 -
    ....:   1289447109375*z^3 + 254876515625*z^4 - 266627903125*z^5 -
    ....:   304623830625*z^6 - 87265479875*z^7 - 4878146975*z^8 + 3939663705*z^9
    ....:   + 1048560285*z^10 + 97471734*z^11 + 3057210*z^12)*Dz^5
    ....: + 10*z^2*(-5568750000000 + 23905125000000*z + 3393646875000*z^2 -
    ....:   39702348750000*z^3 - 7716298734375*z^4 - 3779011321875*z^5 -
    ....:   7801785421250*z^6 - 3351125770500*z^7 - 382134335775*z^8 +
    ....:   148313757125*z^9 + 68439921540*z^10 + 11725276842*z^11 +
    ....:   923795772*z^12 + 27279720*z^13)*Dz^4
    ....: + 5*z*(-13162500000000 + 45343125000000*z + 40530375000000*z^2 -
    ....:   190176960000000*z^3 - 77498059625000*z^4 - 3649915059375*z^5 -
    ....:   26918293320000*z^6 - 13545524756500*z^7 - 465440555100*z^8 +
    ....:   1350059072325*z^9 + 524857986060*z^10 + 92744995638*z^11 +
    ....:   7892060544*z^12 + 255864960*z^13)*Dz^3
    ....: + 5*(-3240000000000 + 5055750000000*z + 44457862500000*z^2 -
    ....:   133825053750000*z^3 - 110925736437500*z^4 + 13367806743750*z^5 -
    ....:   6199228765625*z^6 - 8282515456375*z^7 + 1646226060075*z^8 +
    ....:   2287368823475*z^9 + 810956145330*z^10 + 149186684934*z^11 +
    ....:   13819981248*z^12 + 496679040*z^13)* Dz^2
    ....: + 10*(-189000000000 + 4816462500000*z - 7268326875000*z^2 -
    ....:   21210430812500*z^3 + 2664478321875*z^4 + 3711617481250*z^5 -
    ....:   135661728250*z^6 + 689643286650*z^7 + 607021304825*z^8 +
    ....:   209673119160*z^9
    ....:   + 40678130502*z^10 + 4143853440*z^11 + 167064768*z^12)*Dz
    ....: + 30*(27000000000 + 84037500000*z - 346865625000*z^2 - 55567000000*z^3
    ....:   + 187923165625*z^4 + 36477006875*z^5 + 21336230625*z^6 +
    ....:   19123388575*z^7 + 6925739310*z^8 + 1443544710*z^9 + 163913184*z^10
    ....:   + 7525440*z^11))

In this case, the segment [0, 1] contains a singularity of the operator::

    sage: eval_diffeq(dop5, [0, 0, 0, 0, 1, 0], [0, 1])
    Traceback (most recent call last):
    ...
    ValueError: Step 0 --> 1 passes through or too close to singular point
    0.2050... (to compute the connection to a singular point, make it a vertex
    of the path)

We can nevertheless evaluate the solution of interest using an integration path
that passes above the singular point::

    sage: eval_diffeq(dop5, [0, 0, 0, 0, 1, 0], [0, 1/5+i/2, 1], 1e-60) # long time (56 s)
    [1.04885235135491485162956376369999275945402550465206640313845...] + [+/-...]*I

In the six-dimensional case, Koutschan gives the following operator::

    sage: dop6 = (
    ....:
    ....: 90*(-26986562465909833728000000000000000 -
    ....: 578659365675271609712640000000000000*z -
    ....: 3932207868973120630810214400000000000*z^2 -
    ....: 12270310453108287668341923840000000000*z^3 -
    ....: 9698100095942063765846249472000000000*z^4 +
    ....: 52113850317609070332668882227200000000*z^5 +
    ....: 165979815868291791006070607462400000000*z^6 +
    ....: 252029928377053385449407192172320000000*z^7 +
    ....: 234855990648514674287291744222356800000*z^8 +
    ....: 98749247882439137822044179686396640000*z^9 -
    ....: 83930464288781215080378386513083200000*z^10 -
    ....: 204430925935804223158200138096719244000*z^11 -
    ....: 217051701285403806039787021788244210200*z^12 -
    ....: 158672230290697625052364901820833352540*z^13 -
    ....: 88492994651041978105789511893808827410*z^14 -
    ....: 39203789245543299948038211301310631735*z^15 -
    ....: 14017460872371123201967056591950292270*z^16 -
    ....: 4044657270312306250764976742472089595*z^17 -
    ....: 924626001493256833520380233115382826*z^18 -
    ....: 158195048236903725948800257698582066*z^19 -
    ....: 16377415461160421103082005421146444*z^20 +
    ....: 574602465936356660227512513519630*z^21 +
    ....: 717575244018720111969771948822450* z^22 +
    ....: 190773160991774404319508940400373*z^23 +
    ....: 34047746401934351907977621763618*z^24 +
    ....: 4663284432121091702260620852777* z^25 +
    ....: 510811439434664402615401586970*z^26 +
    ....: 45371384308945745114138623620*z^27 + 3269391489631666671425989920*z^28
    ....: + 189382045823502675349219920*z^29 + 8653460076869413651316640*z^30 +
    ....: 302276251598295683586240*z^31 + 7675748903189765748480*z^32 +
    ....: 130185473751277349888*z^33 + 1254502960824572928*z^34 +
    ....: 4556502187948032*z^35)
    ....:
    ....: + 45*(186207281014777852723200000000000000 -
    ....: 8434528659189021937434624000000000000*z -
    ....: 122588504883178716188285337600000000000*z^2 -
    ....: 655267817084534423521940643840000000000*z^3 -
    ....: 1863534767021891922131179987968000000000*z^4 -
    ....: 2226964464248713386006518356377600000000*z^5 +
    ....: 401336331886317774107713318790400000000*z^6 +
    ....: 5165781565021067274342996673450656000000*z^7 +
    ....: 8691043975963666049447299379144001600000*z^8 +
    ....: 7349743557503879010410921836212410400000*z^9 +
    ....: 698114077775776671885153675463762080000*z^10 -
    ....: 6955035214429661410040236974622315476000*z^11 -
    ....: 10758301750323045400708026810527005985400*z^12 -
    ....: 9808779912515181085311292716635118617340*z^13 -
    ....: 6500636144955681369542005264067707999470*z^14 -
    ....: 3351334353377309619203633178809010250269*z^15 -
    ....: 1382954753973214192431623770039149437562*z^16 -
    ....: 461005100390610028275047960932687009761*z^17 -
    ....: 123304322017356000844884963447213004302*z^18 -
    ....: 25665990995028381347757284132973790086*z^19 -
    ....: 3776626287411277314694612568191478460*z^20 -
    ....: 232966958115695319966898071487115550*z^21 +
    ....: 65404062287190045292473501882376446*z^22 +
    ....: 27828342208285269645811267613975751*z^23 +
    ....: 6203408988166712509967367951961350*z^24 +
    ....: 1010115611151696866102360444043867*z^25 +
    ....: 129674818596578381841709352363310*z^26 +
    ....: 13478285221767374237433813894156* z^27 +
    ....: 1143508859378085891069139805496*z^28 +
    ....: 79010991647695967734365641136*z^29 + 4398883914180352580752205664*z^30
    ....: + 193479386194110772817766720*z^31 + 6513463004865397861819008*z^32 +
    ....: 159628611480988435906560*z^33 + 2619357527554007840768*z^34 +
    ....: 24549299776964745216*z^35 + 88092375633661952*z^36)*Dz
    ....:
    ....: + 45*(1619193747954590023680000000000000000 +
    ....: 14860150621853249942323200000000000000*z -
    ....: 83241123892330166885744640000000000000*z^2 -
    ....: 1428583143864269960769790771200000000000*z^3 -
    ....: 7784392307839726168650555924480000000000*z^4 -
    ....: 20932834089033885270730650301440000000000*z^5 -
    ....: 29659078571699608256375734426214400000000*z^6 -
    ....: 20656761408545661580810751146327680000000*z^7 +
    ....: 6746831082562798982378495636957952000000*z^8 +
    ....: 34764119013156176353837403619970113600000*z^9 +
    ....: 37297341452565155702787810516361533600000*z^10 +
    ....: 9719645940829530820988532518598953424000*z^11 -
    ....: 24193553263042351259117425539502701518400*z^12 -
    ....: 40652966100310576219422839345851085154840*z^13 -
    ....: 36747814326347114270377987158311612338260*z^14 -
    ....: 23667524905718087319814208022941410083354*z^15 -
    ....: 11757721460891217253150507437222976590963*z^16 -
    ....: 4646227686063347368140269721102656923194*z^17 -
    ....: 1472149779764303912910700825119513125745*z^18 -
    ....: 369692934875862692678770756612360457070*z^19 -
    ....: 70294647356901524101024740972933056916*z^20 -
    ....: 8583686545551708471758291210460691032*z^21 -
    ....: 3744645921582101044070547736300950*z^22 +
    ....: 322041161855435062814533420723282482*z^23 +
    ....: 99771357205875220145109466450106517*z^24 +
    ....: 19908118207277143280846917552738638*z^25 +
    ....: 3028085987873439981041316741040299*z^26 +
    ....: 369055333918742878506923895821094*z^27 +
    ....: 36707414555219468440447241903970* z^28 +
    ....: 2993264774540100816050708154540*z^29 +
    ....: 199288291693600445167066471488*z^30 +
    ....: 10707051961496414217407305536*z^31 + 454875015831485400909097248*z^32
    ....: + 14802080405483677823943104*z^33 + 351010067005351488224256*z^34 +
    ....: 5584340634105826525184*z^35 + 50980706267636984832*z^36 +
    ....: 180741253455271936*z^37)*Dz^2
    ....:
    ....:  + 90*z*(11486155649552872980480000000000000000 +
    ....: 114230678131481922666823680000000000000*z +
    ....: 284911453840859719602001920000000000000*z^2 -
    ....: 1112041174659253407521806233600000000000*z^3 -
    ....: 9932878926912153370258947363840000000000*z^4 -
    ....: 27649387021455520276766166546048000000000*z^5 -
    ....: 41909264304440185602876764536603200000000*z^6 -
    ....: 34653454861369485847062964251845520000000*z^7 +
    ....: 757729323937951939044642929351040000000*z^8 +
    ....: 41970729402708473923386620935623814800000*z^9 +
    ....: 54660627321107405540934107870983869840000*z^10 +
    ....: 32573268392371003654841290966684606314000*z^11 +
    ....: 340763873540255131808343067503063454800*z^12 -
    ....: 18559051142634901231618230067011245261730*z^13 -
    ....: 20395042168164862736248341991799243143275*z^14 -
    ....: 13791392258782895819955453998955102517548*z^15 -
    ....: 6879647707640439013900747488611335523490*z^16 -
    ....: 2671193766306193321259081077503739718922*z^17 -
    ....: 818596118205128605985330478856111679058*z^18 -
    ....: 195183178990057349643272275435126736340*z^19 -
    ....: 33929658665256259408812784354866385557*z^20 -
    ....: 3212526847572548623801062566839102968*z^21 +
    ....: 335162333006577190998078624832466745*z^22 +
    ....: 232117491219054750436300759063832796*z^23 +
    ....: 61070425289478623056319494081223364*z^24 +
    ....: 11283714208962998257330503635013918*z^25 +
    ....: 1627987793820686707319681442965532*z^26 +
    ....: 190122674553786922619563973540916*z^27 +
    ....: 18213230428133179674440523308931* z^28 +
    ....: 1434485821162175237888091472086*z^29 +
    ....: 92390999114814905907317974392*z^30 + 4805890762274729535435673296*z^31
    ....: + 197763282456363307438541552*z^32 + 6235802763945868063424352*z^33 +
    ....: 143387361084360543557376*z^34 + 2215666629279250997248*z^35 +
    ....: 19728125958978028032*z^36 + 69106949850545152*z^37)*Dz^3
    ....:
    ....: + 15*z^2*(161818175186211840491520000000000000000 +
    ....: 1776029394112720931570319360000000000000*z +
    ....: 7522568512298824734532104192000000000000*z^2 +
    ....: 7747728379627393494726545203200000000000*z^3 -
    ....: 36772706828360958944274523883520000000000*z^4 -
    ....: 140261247415772885691546407435520000000000*z^5 -
    ....: 242455701875928553517844332493302400000000*z^6 -
    ....: 214965129809120690827282902731468640000000*z^7 +
    ....: 6337926159808918213308690816700464000000*z^8 +
    ....: 276342679146887322412220759883497997600000*z^9 +
    ....: 379975092805467869163550626412993759200000*z^10 +
    ....: 279266241080334469793315941614102969564000*z^11 +
    ....: 107413528041921729529347960434391761302800*z^12 -
    ....: 10222760436927155616364669208395729054260*z^13 -
    ....: 47185211186009106848535876331178061122490*z^14 -
    ....: 38476335393060119379820741759126402451166*z^15 -
    ....: 20284887219829242010855806602752336703097*z^16 -
    ....: 7949778754688875639594299226888542864672*z^17 -
    ....: 2396582727922965009354571656000074347578*z^18 -
    ....: 548617946604162829617617348998523187024*z^19 -
    ....: 87288636539051237531541938169181610997*z^20 -
    ....: 5626714951506760337684784884293147302*z^21 +
    ....: 1820210924970374403477059898368292414*z^22 +
    ....: 815865984997630892337526061797547730*z^23 +
    ....: 194225784819376433418854177036400765*z^24 +
    ....: 33925520928056707379949042245154948*z^25 +
    ....: 4693678127508685757329704793118274*z^26 +
    ....: 528960737538220962199232165726700*z^27 +
    ....: 49056517288448701934966949399201* z^28 +
    ....: 3746772515516029997311378363446*z^29 +
    ....: 234205994182438943769949245108*z^30 +
    ....: 11827310475440684698801079376*z^31 + 472534466386674980533072704*z^32
    ....: + 14467601136584109707654400*z^33 + 323165791319702484035520*z^34 +
    ....: 4857665734098963690240*z^35 + 42232680898487251200*z^36 +
    ....: 146187778529999360*z^37)*Dz^4
    ....:
    ....: + 3*z^3*(595812699442665547776000000000000000000 +
    ....: 6994092214348464533004288000000000000000*z +
    ....: 34708946736814927353542983680000000000000*z^2 +
    ....: 64135781486584141753707277824000000000000*z^3 +
    ....: 1049740530978348996701293958400000000000*z^4 -
    ....: 226302972537833147253780811598400000000000*z^5 -
    ....: 518937227107573341964843985332680000000000*z^6 -
    ....: 526332032930456915428235817813056400000000*z^7 -
    ....: 44891871663741237702913642763603760000000*z^8 +
    ....: 586378944861718695144037906690882422000000*z^9 +
    ....: 865953342265454601104437816976581680000000*z^10 +
    ....: 696554593654757665866719966270600171130000*z^11 +
    ....: 349803608265045461612489069936675179800000*z^12 +
    ....: 87213988833696382614552027738719280959850*z^13 -
    ....: 23459339067193287788165144055727575111225*z^14 -
    ....: 38330478964162570556645949941637505810110*z^15 -
    ....: 23191419391770985171480237991217872142915*z^16 -
    ....: 9468529098949077023394535618861256937240*z^17 -
    ....: 2858027882158570016919188514224326558185*z^18 -
    ....: 635954475887313295192241042199635547930*z^19 -
    ....: 93149956267467504725225680596497523339*z^20 -
    ....: 3066274907647801401815807099801425704*z^21 +
    ....: 3006740720618245361400876608130182349*z^22 +
    ....: 1112001535696035843878120629687073790*z^23 +
    ....: 247864598814302846690177415162792735*z^24 +
    ....: 41511153616540066669903815109576752*z^25 +
    ....: 5552646100941335755747908121811397*z^26 +
    ....: 607255705204278811351245801585018*z^27 +
    ....: 54750340798147926328921245513135* z^28 +
    ....: 4068564888973003880820853550310*z^29 +
    ....: 247501384020921867412586484240*z^30 +
    ....: 12162402278802667065896636880*z^31 + 472739613103493977658692800*z^32
    ....: + 14079224644087925329523520*z^33 + 305988393455491537290240*z^34 +
    ....: 4480274117205321023232*z^35 + 38072220474786769152*z^36 +
    ....: 130240020872181248*z^37)*Dz^5
    ....:
    ....: + z^4*(512323021813756999680000000000000000000 +
    ....: 6311156771304917325766656000000000000000*z +
    ....: 33882896755872071956886261760000000000000*z^2 +
    ....: 72511610277412390990839363072000000000000*z^3 +
    ....: 59704683972170679548931977222400000000000*z^4 -
    ....: 86642575450501391066787202019520000000000*z^5 -
    ....: 327383462755042385949747691240824000000000*z^6 -
    ....: 395683465592680867401293480616198000000000*z^7 -
    ....: 119682652007548350954457856750250720000000*z^8 +
    ....: 287121363379312616871562346484465378000000*z^9 +
    ....: 495779225046771906420255540348281344800000*z^10 +
    ....: 429409878921957648790555775268242743350000*z^11 +
    ....: 240689360358498296007939096187740586134000*z^12 +
    ....: 85149274357043292385925033653294291853550*z^13 +
    ....: 10278671248090335377408918358815408788425*z^14 -
    ....: 9076459539413303184641722134776573895810*z^15 -
    ....: 7573126212785007618891225542456994124245*z^16 -
    ....: 3356732946224373601649087937349109785896*z^17 -
    ....: 1033954017266382248984767586852072344191*z^18 -
    ....: 226886176666918560987240200768631693150*z^19 -
    ....: 31072001737970299221405533198706303141*z^20 -
    ....: 137626809673226795399591264079041112*z^21 +
    ....: 1319636945498761264973744224282378779*z^22 +
    ....: 441055376229095921513357130918811338*z^23 +
    ....: 94068732852089205756130773605094705*z^24 +
    ....: 15263082383031406770429022758762048*z^25 +
    ....: 1986708322085667572665525016037411*z^26 +
    ....: 211815796834464054711973645322142*z^27 +
    ....: 18631082892630536824222949409585* z^28 +
    ....: 1350855094398006902682870922050*z^29 +
    ....: 80160062388267727172211985080*z^30 + 3840828004490920060950969480*z^31
    ....: + 145494567985766484898923048*z^32 + 4221606838983473228197008*z^33 +
    ....: 89393980129433032096320*z^34 + 1276532600942212775168*z^35 +
    ....: 10612604051614486656*z^36 + 35882454730090752*z^37)*Dz^6
    ....:
    ....: + 2*z^5*(15 + z)*(1973392380319656591360000000000000000 +
    ....: 25084009812063190450176000000000000000*z +
    ....: 140360356659888583720114176000000000000*z^2 +
    ....: 314413056395938625838510182400000000000*z^3 +
    ....: 344718972957157801371250560000000000000*z^4 -
    ....: 145021874608394651059638847488000000000*z^5 -
    ....: 1074498717874767393664900393675200000000*z^6 -
    ....: 1460286146960184444033629739148560000000*z^7 -
    ....: 682640121106346995555734719308248000000*z^8 +
    ....: 564704048394845939194551470638922400000*z^9 +
    ....: 1251150937075501602577084871183562120000*z^10 +
    ....: 1138666598560461678104890857545212608000*z^11 +
    ....: 661181529544504134786063620152764386400*z^12 +
    ....: 253995260187409794081727430934766869450*z^13 +
    ....: 51498237061832672183443454747804923575*z^14 -
    ....: 7977590414255123112276744122571399783*z^15 -
    ....: 11704453530273493922795299130700457200*z^16 -
    ....: 5466573829106434312238352307226140764*z^17 -
    ....: 1638945569143497023502201509481372411*z^18 -
    ....: 331259809437872111827650003935308209*z^19 -
    ....: 35907063701591969077649893288537878*z^20 +
    ....: 3221036141212186087856769990927054*z^21 +
    ....: 2620577206027992337931632885352217*z^22 +
    ....: 724749378242590885585485419445843*z^23 +
    ....: 138105907223379522203625428215332* z^24 +
    ....: 20337622679657217515316342764256*z^25 +
    ....: 2406227015296631910854902756563*z^26 + 232115671681854334221586338585*
    ....: z^27 + 18309889884984684630822323370*z^28 +
    ....: 1175154434178119041671700740* z^29 + 60618715038937670473018584*z^30 +
    ....: 2462288021152606885358700*z^31 + 76318086060490791960792*z^32 +
    ....: 1719342411627828757728*z^33 + 25996840572204888512*z^34 +
    ....: 227389988057526336*z^35 + 800100086574208*z^36)*Dz^7
    ....:
    ....: + (-3 + z)*(-1 + z)*z^6*(4 + z)*(5 + z)*(9 + z)*(15 + z)^2*(24 + z)*(3
    ....: + 2*z)* (15 + 2*z)*(15 + 4*z)*(60 + 7*z)*(19280523023769600000000000 +
    ....: 242306901961056460800000000*z + 1348035643913347353600000000*z^2 +
    ....: 2878395143123986146432000000*z^3 + 3920543674198265211436800000*z^4 +
    ....: 753459769629110696243040000*z^5 - 5337917399156522389289280000*z^6 -
    ....: 8883487977021576719907033600*z^7 - 7971869741181425686355371200*z^8 -
    ....: 4872861027995366524279994100*z^9 - 2157072153972513398276826924*z^10 -
    ....: 693159300555093708939611829*z^11 - 152346950611719661239440526*z^12 -
    ....: 16970927000980381863663141*z^13 + 2189507486524206284827296*z^14 +
    ....: 1557656993073750677220582*z^15 + 412843760981101392072948*z^16 +
    ....: 72864795413899911011922*z^17 + 9465736161794804567892*z^18 +
    ....: 931032563834500230663*z^19 + 69321047461074869130*z^20 +
    ....: 3823803744461234343*z^21 + 149102740118852712*z^22 +
    ....: 3764987488054392*z^23 + 51659233261888*z^24 + 242161043152*z^25)*Dz^8)

Unfortunately, this operator is a bit too large for us at this point! ::

    sage: eval_diffeq(dop6, XXX, [0, 1]) # not tested
    [1.02774910062749883985936367927396850209243990900114872425172...]
"""

