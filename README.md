# Projekta darbs
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
   Tiek izmantota, lai mijiedarboties ar Coursera, MIT OpenCourseWare un edX vietnēm. WebDriver Chrome izmanto pārlūkprogrammas vadīšanai.

2) **BeautifulSoup**:
   Tiek izmantota, lai analizētu saņemto tīmekļa lapu HTML kodu un iegūtu nepieciešamo informāciju.

3) **urllib.parse**:
   urljoin tiek izmanta, lai no dažādiem tās komponentiem izveidotu pilnīgu saiti uz vietni.

4) **time**:
   time.sleep tiek izmanta, lai izveidotu pauzes starp darbībām, lai pārlūkprogrammai un lapām būtu laiks ielādēties.
   
