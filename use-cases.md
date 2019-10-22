Opis skrócony przypadków użycia
===============================

Aktorzy procesu i ich cele
--------------------------

Aktor       Cel 
----------- -----------------------------
Klient 		 		 |		Celem Klienta jest wypłata lub wpłata pieniędzy, zakup kodów pre-paid do telefonu, sprawdzenienie stanu konta i dokonanie operacji przelewu dla innych użytkowników.
Serwisant 	  		 | 		Celem Serwisanta jest naprawa, przegląd i sprawdzenie wymaganych w systemie funkcjonalności. 
Pracownik obsługi    | 		Celem pracownika obsługi jest bezpieczna, szybka i bezproblemowa wpłata gotówki do bankomatu. W przypadku zamknięcia lub przeniesienia bankomatu, pracownik chce w łatwy sposób wypłacić całą zawartość bankomatu.


Słownik
-------

Hasło       Opis

Przypadki użycia
----------------

### Use case 1: Wypłata pieniędzy
Klient wkłada kartę, podaje PIN, a system potwierdza jego poprawność. W menu głównym klient wybiera opcję wypłaty. W nowym oknie określa kwotę, którą chciałby wypłacić. Następnie decyduje czy chce odebrać potwierdzenie. Klient odbiera kartę, gotówkę i ewentualne potwierdzenie.

### Use case 2: Wpłata pieniędzy
Klient wkłada kartę, podaje PIN i w menu głównym wybiera opcję wpłaty. Klient podaje kwotę, którą chciałby wpłacić, a następnie odpowiednią ilość gotówki umieszcza w podanym miejscu. Klient na ekranie widzi wpłaconą kwotę.

### Use case 3: Zakup kodów do telefonii pre-paidowej
Klient wkłada kartę, podaje PIN, a system potwierdza jego poprawność. W menu głównym klient wybiera opcję zakupu kodów do telefonii pre-paidowej. Na ekranie klient wybiera stosownego operatora sieci komórkowej. Następnie wybiera kwotę i odbiera kartę wraz z dedykowanym kodem.

### Use case 4: Sprawdzenienie stanu konta
Klient wkłada kartę, podaje PIN, a system potwierdza jego poprawność. W menu głównym klient wybiera opcję sprawdzenia stanu konta. System zwraca Klientowi kartę i paragon ze stanem konta.

### Use case 5: Dokonywanie operacji przelewu dla uzytkowników
Klient wkłada kartę, podaje PIN, a system potwierdza jego poprawność. W menu głównym klient wybiera opcję przekazu bankomatowego. Podaje swój numer PESEL, swój oraz odbiorcy numer telefonu, kwotę przekazu. Na ekranie pojawi się podsumowanie transakcji. Klient może odebrać kartę.
