Exerciţiu
Folosind modulul sqlite3, creați o bază de date clienți în bancă. Clientul are ca atribute un id ca şi cheie principală, numele și prenumele, numărul de cont și parola. De asemenea, este nevoie să definim atributul token în care va fi stocat tokenul utilizatorului care accesează contul. Este necesar să introducem în baza de date trei utilizatori arbitrari.

Trebuie să creăm un program care va necesita numărul de cont și codul clientului sub formă de intrare. Dacă clientul nu există în baza de date, programul va returna eroarea. În caz contrar, este necesar ca programul să creeze un token care va fi valabil pentru următoarele 45 de secunde și să introducă același token pentru un anumit utilizator în coloana destinată lui. De asemenea, este necesar ca programul să afișeze un mesaj de acces reuşit și să returneze tokenul utilizatorului.

---------------------------------------------

Metoda do_GET va avea ca scop returnarea unui token(valabil o anumită perioadă) dacă autentificarea va reuși. Altfel metoda do_GET va returna un string corespunzător unui mesaj de eroare.

Metoda do_POST va avea ca scop utilizarea token-ului generat cu metoda do_GET, pentru a simula o acțiune ce în mod normal presupune logarea. Deci, această metodă trebuie să primească un token, pe care îl va verifica dacă este unul valid, iar apoi îl va decripta, pentru a extrage valorile necesare logării.

Deci, aplicația va fi utilizată prin secvența GET -> POST. Metoda GET va genera token-ul, iar metoda do_POST va consuma acest token-ul.

Metode POST va utiliza doar un token, netrevuind ca logica să poată utiliza și o formă "clasică" de logare ce presupune transmiterea usernaneme-ului și parolei.