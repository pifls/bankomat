Use Case 1: Wypłata pieniędzy
=====================
 
**Aktor podstawowy:** Klient
 
 
Główni odbiorcy i oczekiwania względem systemu:
-----------------------------------------------
 
- Klient: oczekuje możliwości szybkiego wprowadzania danych, braku błędów w działaniu bankomatu oraz wydania mu odpowiedniej kwoty po poprawnym przeprowadzeniu wszystkich kroków potrzebnych do wypłaty środków.
- System bankowy: chce bezproblemowej obsługi przez klienta oraz sprawne działanie
- Serwisant: chce szybko zdiagnozować problem oraz go rozwiązać
 
Warunki wstępne:
----------------
- Bankomat jest sprawny a klient posiada kartę płatniczą.
- Klient nie będzie korzystać z innych funkcjonalności bankomatu poza "Wpłata pieniędzy".
- Domyślnym językiem systemu jest język polsku.
- Na każdym ekranie oprócz "Menu" jest w rogu przycisk "Wróć do menu"
 
Warunki końcowe:
----------------
- Po poprawnym przeprowadzeniu transakcji "Wypłata pieniędzy" bankomat zawsze wydaje odpowiednią kwotę w odpowiednim miejscu
 
Scenariusz główny (ścieżka podstawowa):
---------------------------------------
 
  1. Klient rozpoczyna obsługę bankomatu
  2. System wyświetla na ekranie główne menu
  3. Klient wprowadza kartę płatniczą do bankomatu
  4. System weryfikuje kartę
  5. Bankomat prosi klienta o wprowadzenie numeru PIN
  6. Klient wprowadza poprawny PIN
  7. Na ekranie bankomatu wyświetlają się możliwe akcje do wykonania przez klienta
  8. Klient wybiera opcję "Wypłata środków"
  9. Bankomat wyświetla na ekranie kwoty do wyboru jak i opcję do wyboru innej kwoty
  10. Klient wybiera jedną z proponowanych przez interfejs kwot
  11. Bankomat wyświetla na ekranie podaną kwotę i prosi klienta o jej zatwierdzenie
  12. Klient zatwierdza swój wybór
  13. System weryfikuje czy podane środki mogą zostać wypłacone z danego konta
  14. Bankomat wyświetla na ekranie komunikat o tym, że pieniądze zostaną zaraz wydane
  15. Bankomat wydaje kartę płatniczą
  16. Bankomat wydaje podaną kwotę w odpowiednim miejscu
  17. Klient zabiera wydane pieniądze
 
Rozszerzenia (ścieżki alternatywne):
------------------------------------

*a W dowolnym czasie, gdy system przestanie działać
 1. System oddaje klientowi kartę płatniczą
 2. System wyświetla na ekranie informację o błędzie
 3. Przechodzimy do punktu 1 głównego scenariusza

  4a. System nie weryfikuje karty płatniczej
1. System oddaje klientowi kartę płatniczą
2. System wyświetla na ekranie informację o braku weryfikacji karty płatniczej
3. Przechodzimy do punktu 1 głównego scenariusza
 
  6a. Klient wprowadza błedny numer PIN po raz pierwszy lub drugi
1. System informuje klienta o wprowadzeniu przez niego błednego numeru PIN
2. Przechodzimy do punktu 5 głównego scenariusza
   
  6b. Klient wprowadza błędny PIN 3 raz z rzędu
1. System informuję klienta o wpisaniu przez niego błędnego numeru PIN 3 raz z rzędu oraz o zablokowaniu karty
2. Przechodzimy do punktu 15 i na nim kończymy scenariusz

8a. Klient wybiera opcję "Zmiana języka"
1. System wyświetla na ekranie języki do wyboru.
2. Klient wybiera jeden z języków na ekranie
-1. System zmienia swój język na podany na ekranie
-2. Przechodzimy do punktu 2 głównego scenariusza 
- 2a. Klient wybiera opcję "Wróć do menu"
- 1. Przechodzimy do punktu 2 głównego scenariusza

8b. Klieny wybiera inną opcję niż "Wypłata środków" i "Zmiana języka"
1. System przechodzi do podanego widoku
2. Klient naciska opcję "Wróć do menu"
3. Przechodzimy do punktu 7 głównego scenariusza
 
  14a. System wyświetla klientowi informację o braku podanych środków na koncie
1. System wyświetla na ekranie opcję "Wróć do menu" oraz "Wyjście"
2. Klient wybiera opcję "Wróć do menu"
    1. Przechodzimy do punktu 7 głównego scenariusza 
- 2a. Klient wybiera opcję "Wyjście"
- 1. Przechodzimy do punktu 15 i na nim kończymy scenariusz
 
Wymagania specjalne:
--------------------
  - Weryfikacja karty i PINU nie powinna trwać więcej niż 10 sekund. Podczas czasu oczekiwania system wyświetla specjalny buffer aby klient był świadomy, że musi czekać na weryfikację
  - Wyświetlanie komunikatów trwa 30 sekund. Po tym czasie system przechodzi do kolejnego kroku scenariusza
  
Wymagania technologiczne oraz ograniczenia na wprowadzane dane:
---------------------------------------------------------------
- Przy wprowadzaniu numeru PIN oraz innej kwoty na ekrania wyświetla się klawiatura tylko cyframi
 
Kwestie otwarte:
----------------
- Ograniczenie bankomatu na możliwość wypłacanej kwoty przez klienta
- Czy klient przy wypłacie powinien mieć możliwość wydrukowania/wyświetlenia swojego obecnego stanu konta?
- Czy klient powinien mieć możliwość wpłaty gotówki w innej walucie niż PLN?