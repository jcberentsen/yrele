# Decisions for værdata-innhenter case

Denne filen med avgjørelser holdes på norsk. Domene-språk i kodebasen velger jeg å holde på engelsk, også kommentarer, siden engelsk er globalt mer tilgjengelig, siden github repo er public.

Implementasjonen er i python > 3.14

Siden det er både en http klient og server del, ser jeg etter et http bibliotek som kan støtte begge deler, om mulig. Dette for aligne rundt concurrency, feilhåndtering, logging.

Persistens: En mulig løsning kan være å skille Klient og Server fullstendig og bruker database som informasjonsbærer.
Separert Klient og Server vanskeliggjør en potensielt enklere persistensløsning som filsystem (json blobs)
For database foreslår oppgaven sqlite og da er sqlite3 et naturlig valg her.

For tester er pytest et naturlig valg, siden det er de-facto standard.

Jeg går for dependency injection for http og persistency så vi kan teste behaviour uten ekte IO

Git og github er naturlig etter oppgave-definisjon

Bruk av Docker og docker compose etter oppgaven

Github Actions for CI test kjøring (om det blir tid)

README.md inneholder instruksjoner for oppsett og kjøring av tester og service. (på engelsk)

Oppgaven spesifiserer ikke multi-user, så jeg hopper over alt som har med bruker, auth, ident å gjøre. Dette gjør også persistens noe enklere.
Jeg utelater db schema migrasjon, da dette er out of scope. Vi kan alltids gjenskape db fra upstream yr data, bruker må kanskje registrere locations på nytt.

Bruker kan registrere locations, men vi gjør ingenting foreløbig for å hindre duplikater. Eksakte duplikater kan muligens sjekkes, men sammenligning av floats må takles.
