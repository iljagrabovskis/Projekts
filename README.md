## Projekta uzdevums
Šī projekta mērķis ir automātiski izpētīt un meklēt nepieciešamo informāciju no 3 vietnēm, kas nodrošina iespēju apmeklēt tiešsaistes kursus par lietotāju interesējošām tēmām. Pēc koda izpildes lietotājs saņem teksta dokumentu, kurā ir aprakstīta pamatinformācija par kursu (ieskaitot saiti uz vietni). Koda palaišanas brīdī lietotājam ir iespēja ievadīt kursa nosaukumu angļu valodā (piemēram, Finance, Information Technologies vai kaut kas cits), un programma automātiski meklēs kursus.
Šajā projektā izmantotās vietnes:
```
1) Coursera.org
2) ocw.mit.edu
3) edx.org
```
Kopumā, ja visās trīs vietnēs ir kursi, kas atbilst lietotāja ievadītajai tēmai, programma parādīs 11 dažādus rezultātus. 4 rezultāti būs no "Coursera" vietnes, vēl 4 no "ocw.mit.edu" vietnes, un vēl 3 no "edx.org"

## Izmantotās bibliotēkas
1) **Selenium**:
   Tiek izmantota, lai mijiedarboties ar Coursera, MIT OpenCourseWare un edX vietnēm, ļauj noklikšķināt uz pogām un ievadīt tekstu laukos. WebDriver Chrome izmanto pārlūkprogrammas vadīšanai. Visas pogas un lauki tiek meklēti, izmantojot ID, klases vai citus atbilstošās lapas HTML koda atribūtus

2) **BeautifulSoup**:
   Tiek izmantota, lai analizētu saņemto tīmekļa lapu HTML kodu un iegūtu nepieciešamo informāciju.

3) **urllib.parse**:
   urljoin tiek izmanta, lai no dažādiem tās komponentiem izveidotu pilnīgu saiti uz vietni.

4) **time**:
   time.sleep tiek izmanta, lai izveidotu pauzes starp darbībām, lai pārlūkprogrammai un lapām būtu laiks ielādēties.

Jāpiebilst, ka kodam ir pievienots arī viens teksta dokuments library.txt, kurā aprakstītas visas izmantotās bibliotēkas. Tas nozīmē, ka jebkuram lietotājam, kuram dažas bibliotēkas nav instalētas, ir iespējams ievadīt vienu komandu "pip install -r library.txt" pirms koda palaišanas, nevis manuāli instalēt katru bibliotēku.

## Programmatūras izmantošanas metodes
Koda izpildes process sastāv no vairākiem posmiem. Darbs ar katru vietni ir aprakstīts kā atsevišķa funkcija, kas tiek izsaukta koda beigās, lai programma izskatītos strukturēta un saprotama. Ir vērts atzīmēt, ka kods tika izstrādāts Visual Studio Code izstrādes vidē, jo GitHub vietnes nodrošinātajā codespace nav iespējams izmantot Selenium bibliotēku, jo tā nevar atvērt citu pārlūkprogrammas. Lai precīzi pārbaudītu koda funkcionalitāti, tas jāpalaiž kādā programmām, kas nodrošina izstrādes vidi.

1) Pirmkārt, kods importē visas nepieciešamās bibliotēkas

2) Pēc tam lietotājs ievada interesējošo tēmu (piemēram Computer Science)

3) Talāk kods konfigurē Coursera pārlūkprogrammas Chrome iestatījumus, atver Coursera vietni, akceptē sīkdatņes (noklikšķina uz pogas "Piekrist"), meklēšanas laukā ievada tēmu, kuru pierakstīja lietotajs programmas sakumā, gaida 6 sekundes, līdz tiek ielādēti rezultāti. Izmantojot BeautifulSoup tiek atrasts datu bloks ar kursiem. Nepieciešama informācija tiek izņemta no datu bloka, saglabāta sarakstā un pierakstītā jaunajā teksta failā.

4) Atkārto līdzīgas darbības ar MIT OpenCourseWare un edX vietnem. 
Atšķirība ir tāda, ka informācija no šīm vietnēm tiek ierakstīta teksta failā nevis ar “w” metodi, bet ar metodi “a”, lai nepazaudētu ierakstus no iepriekšējām vietnēm.

5) Pēc darba ar pārlūkprogrammu un visas saņemtās informācijas ierakstīšanas teksta failā programma aizver pārlūkprogrammu un pabeidz darbu

Pēc koda atkārtotas palaišanas visa vecā informācija no teksta faila tiek aizstāta ar jaunu un aktuālo informāciju.

## Video ar programmas piemēru

https://youtu.be/BsQW_yVsCUo
