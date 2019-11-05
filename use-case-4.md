Use Case 4: Sprawdzanie stanu konta
=====================

**Aktor podstawowy:** Klient


Główni odbiorcy i oczekiwania względem systemu:
-----------------------------------------------

- Klient: możliwość przejścia sekwencji kroków prowadzącej do sprawdzenia własnego stanu konta. 

- Serwisant: Chęć szybkiego zdiagnozowania problemu oraz możliwość szybkiej naprawy lub wymiany jednego z niedziałających modułów. 

- Bank: Chęć monitorowania ilości operacji, czasu oraz miejsca w którym operacja została zlecona.

Warunki wstępne:
----------------
Klient posiada kartę bankową.

Warunki końcowe:
----------------
Wpisany pin jest przetwarzany w bezpieczny sposób, tak żeby nie wycieły żadne informacje dotyczące konta klienta. Dane dotyczące zlecenia operacji sprawdzenia stanu kąta są przechowywane.

Scenariusz główny (ścieżka podstawowa):
---------------------------------------

  1. Klient wkłada kartę do bankomatu.
  2. Bankomat wyświetla ekran wyboru języka.
  3. Klient wybiera język w którym będą wyświetlane komunikaty na ekranie.
  4. Bankomat wyświetla ekran wprowadzania PIN'u.
  5. Klient wprowadza PIN i zatwierdza jego wprowadzenie.
  6. Bankomat potwierdza poprawność wprowadzonego PIN'u i wyświetla ekran główny. 
  7. Klient wciska przycisk odpowiadający funkcji sprawdzenia stanu konta.
  8. Bankomat zwraca klientowi kartę.
  9. Bankomat drukuje paragon z wartością reprezentującą stan konta.

Rozszerzenia (ścieżki alternatywne):
------------------------------------
 1a. Wprowadzona karta nie jest aktywna lub nie jest kartą bankową:
  1. System informuje klienta o nieaktywności wprowadzonej karty.
  2. System prosi o wprowadzenie innej karty.

 5a. Został wprowadzony niepoprawny PIN:
  1. System informuje klienta o niepoprawności wprowadzonego pinu
  2. System prosi klienta o ponowne wpisanie kodu PIN.

 7a. Klient wcisnął zły przycisk który przekierował go do innego, niewłaściwego okna:
  1. Klient klika przycisk powrtodu do poprzedniego ekranu

 9a. Paragon wydrukował się niepoprawnie:
  1. Klient przechodzi do kroku pierwszego scenariusza głównego.

Wymagania specjalne:
--------------------

  - Niezbędny ekran z przyciskami z boku lub dotykowy.
  
  - Możliwość interfejsu wielojęzycznego.
  
  - Wielkość czcionki dostosowana również do osób starszych. 

Wymagania technologiczne oraz ograniczenia na wprowadzane dane:
---------------------------------------------------------------

 3a. Wprowadzany PIN jest długości 4 znaków i składa się wyłącznie z cyfr.


Kwestie otwarte:
----------------

  - Czy umożliwiamy uzytownikowi wyświetlenie na ekranie stanu konta zamiast lub wraz z wydrukiem papierowym?

