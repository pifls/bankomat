Zdarzenia systemowe
===================

* - zdarzenia unikatowe

Use case 1: Wypłata pieniędzy
-----------------

  - wprowadzenie karty przez klienta *A
  - podanie numeru PIN *A
  - wybranie opcji "Wypłata" z menu *M
  - podanie kwoty do wypłaty *M
  - zatwierdzenie kwoty do wypłaty *J
  - potwierdzenie chęci otrzymania paragonu *F
  - odebranie karty z bankomatu *M
  - odebranie pieniędzy z bankomatu *J
  - zmiana języka interfejsu *F
  - wybranie opcji "Zmiana języka" *M
  - wybranie języka interfejsu *J
  - wybranie opcji "Anuluj transakcję" *F
  - wybranie opcji "Wyjście" *M

Use case 2: Wpłata pieniędzy
-----------------

  - wprowadzenie karty przez klienta
  - podanie numeru PIN
  - wybranie opcji "Wpłata" z menu *J
  - podanie kwoty do wpłaty
  - zatwierdzenie kwoty do wpłaty
  - wprowadzenie pieniędzy do bankomatu *F
  - ewentualne potwierdzenie chęci otrzymania paragonu
  - odebranie karty z bankomatu
  - odebranie gotówki z bankomatu po nieudanej próbie wpłaty *M
  - wybranie opcji "Zmiana języka"
  - wybranie języka interfejsu
  - wybranie opcji "Anuluj transakcję"
  - wybranie opcji "Wyjście"

Use case 4: Sprawdzanie stanu konta
-----------------

  - wprowadzenie karty przez klienta
  - podanie numeru PIN
  - wybranie opcji "Stan konta" z menu *J
  - odebranie paragonu ze stanem konta
  - odebranie karty z bankomatu
  - wybranie opcji "Zmiana języka"
  - wybranie języka interfejsu
  - wybranie opcji "Anuluj transakcję"
  - wybranie opcji "Wyjście"
 
Use case 3: Zakup kodów do telefonii pre-paid
-----------------

  - wprowadzenie karty przez klienta
  - podanie numeru PIN
  - wybranie opcji "Zakup kodów Pre-paid" z menu *F
  - wybranie operatora sieci *M
  - wybranie kwoty do zasilenia konta *J
  - odebranie paragonu z kodem pre-paid *F
  - odebranie karty z bankomatu
  - wybranie opcji "Zmiana języka"
  - wybranie języka interfejsu
  - wybranie opcji "Anuluj transakcję"
  - wybranie opcji "Wyjście"

Use case 5: Dokonywanie operacji przelewu dla użytkowników
-----------------

  - wprowadzenie karty przez klienta
  - podanie numeru PIN
  - wybranie opcji "Przelew" z menu *M
  - podanie numeru PESEL *J
  - podanie numeru telefonu odbiorcy *F
  - podanie numeru telefonu nadawcy *F
  - podanie kwoty do przelewu *J
  - odebranie karty z bankomatu
  - wybranie opcji "Zmiana języka"
  - wybranie języka interfejsu
  - wybranie opcji "Anuluj transakcję"
  - wybranie opcji "Wyjście"