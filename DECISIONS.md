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

Bruker kan registrere locations, men vi gjør ingenting foreløbig for å hindre duplikater.

# Utenfor tidsramme:

Det ble en del kaninhull å dukke ned i, så ting er i varierende fremdrift

Neste skritt om det var mer tid:
1. Dekomponere yr respons og plukke ut interessant info, bare persistere det som er ønsket
   1.1 Trekke ut tidsserier for å støtte history og latest handlere
2. Få mer logikk rundt tids-serier
3. Implementere flere api handlere. Nå er locations api, fetch og forecasts implementert
   1. forecasts dumper all info om en lokasjon og fasongen bør tilpasses
   2. stale kan implementeres etter litt vurdering av representasjon av tid
   3. latest og history kan implementeres etter videre nedbrytning av data
4. Finne god måte å behandle tid på, slik at man kan skrive tester rundt 'stale' data
5. Bedre feilhåndtering når yr ikke svarer som forventet. (Vi lagrer ihvertfall ikke noe). Vil vi lagre feil, prøve igjen senere etc?
6. Fullføre github actions for pytest og smoketesting, fikk ikke testet dette fullstendig
7. Vurdere om duplikate locations er et problem i db, det kan henge på fremtidige valg rundt brukere. F.eks hvis man tillater update av location (f.ex gi nytt navn) kan man tillate flere varianter av samme fysiske lokasjon. (Eller flytting location punktet nærmere 'hjem')
8. Forbedre dokumentasjon
9. Flere og dypere automatiske tester. Det var praktisk å bruker docs/ Swagger endepunktet som tilbyr "Try it out". Dette gav en rask feedback loop, men sikrer ikke mot fremtidige regresjoner.

# Utenfor scope
* User auth el.l
* Logging
* Mock framework (Jeg pleier unngå disse, men det kunne gitt verdi her, f.ex. requests-mock)
* Mer sofistikert python prosjekt config (som 'uv' el.l)
