Use Case 2: Wpłata gotówki
=====================

**Aktor podstawowy:** Klient


Główni odbiorcy i oczekiwania względem systemu:

Klient - chęć bezproblemowej wpłaty pieniędzy i otrzymania potwierdzenia tej transkacji.
Serwisant - chęć szybkiego zdiagnozowania i określenia problemu lub błędu. Chęć usunięcia błędu w łatwy sposób.
System bankowy - chęć poprawnej obsługi transakcji realizowanej przez bankomat. Chęć otrzymania poprawnego zapytania o potwierdzenie zapłaty.

-----------------------------------------------

Warunki wstępne:

Bankomat jest sprawny, tzn. wyświetlacz i przyciski działają tak, jak zakładał producent. Klient posiada kartę bankomatową i gotówkę do wpłaty.

----------------


Warunki końcowe:

Klient wpłacił wybraną kwotę. Bankomat wydał potwierdzenie transakcji.

----------------


Scenariusz główny (ścieżka podstawowa):
---------------------------------------

  1. Klient wkłada kartę do bankomatu.
  2. Klient podaje PIN.
  3. Bankomat poprawnie weryfikuje PIN.
  4. Kient wybiera opcję wpłaty.
  5. Bankomat informuje Klienta o wymaganiach technicznych procesu (m.in. o wymaganym stanie technicznym banknotów).
  6. Klient w otworze umieszcza odpowiednią ilość gotówki.
  7. Klient zatwierdza pokazaną na ekranie wartość, równą wartości wpłaconej kwoty.
  8. Klient odbiera potwierdzenie transakcji.

Rozszerzenia (ścieżki alternatywne):
------------------------------------

 *a. W dowolnym czasie, gdy system zawiesza się:
 a.1. System dokonuje resetu oraz zwraca kartę i pieniądze. 
 a.2.  System rozpoczyna pracę od nowa.  
 a.2a. System nie mógł rozpocząć pracy od nowa.  
 a.2a.1. System wzywa serwisanta.  
 a.2a.2. Serwisant przybywa i dokonuje potrzebnych napraw.  
 a.2a.3. Serwisant uruchamia system na nowo.  
 a.2a.4. System uruchamia się na nowo.  
 a.3. 

 6.a. Gotówka jest w złym stanie technicznym
 6.a.1. System informuje o nieodpowiednim stanie gotówki.
    6.a.1.1 Klient wybiera opcję ponownej wpłaty.
        6.a.1.1.1 Klient wpłaca ponownie gotówkę.
        6.a.1.1.2. System ponownie informuje o złym stanie gotówki.
        6.a.1.1.3. Klient wraca do punktu 6.a.1.1.1.
    6.a.1.2. Klient odbiera gotówkę, a transakcja jest zakończona.
    
7.a Klient postanawia wpłacić dodatkową kwotę
7.a.1 Klient zamiast zaakceptować widniejącą na ekranie kwotę, wybiera opcję "Dodaj".
7.a.2 Klient ponownie wkłada gotówkę do wpłatomatu.
7.a.3 System ponownie analizuje podaną kwotę.
7.a.3.1. Gdy gotówka jest w złym stanie, system przenosi Klienta do kroku 6.
7.a.3.2 Gdy gotówka jest w dobrym stanie, proces przebiega dalej bez zakłóceń.

7.b. Klient rezygnuje z operacji.
7.b.1. Klient rezygnuje z zakupu i wybiera opcję "Anuluj". Automat zwraca podaną gotówkę i powraca do stanu początkowego.
    


Wymagania specjalne:
--------------------

  - Bankomat wyposażny jest w płaski monitor, odpowiednio duży i wygodny dla Klienta

  - System oferuje dostęp w wielu językach

  - Autoryzacja użytkownika nie może trwać dłużej niż 15 sekund.

Wymagania technologiczne oraz ograniczenia na wprowadzane dane:
---------------------------------------------------------------
 5a. System w trakcie jednej operacji może przyjąć banknoty tylko z jednej waluty

 5b. System w przypadku Złotego przyjmuje banknoty o nominale 10, 20, 50, 100, 200 i 500 zł.

 5c. Wartość minimalnej wpłaty wynosi 50 zł.

Kwestie otwarte:
----------------

  - Jak system powinien zareagować na kilkukrotne błędne podanie PINu?

  - Czy wpłaty powyżej jakiejś kwoty, np. 10000 zł powinny być dodatkowo weryfikowane?
 
  - Czy dla bezpieczeństwa system nie powinien przyjmować banknotów o bardzo wysokim nominale, np. 500 zł?
  
