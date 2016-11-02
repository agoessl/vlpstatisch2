% Dokumentation VLP-Statisch
% Angelique Gößl

## Einleitung

  * Ziel des Projekts  
  * Es gibt wissenschaftliche Webprojekte die verwaisen, da die Projektteilnehmer das Institut verlassen haben etc.
  * Die Projekte stehen aber weiterhin im Netz und müssen am Leben erhalten werden.
  * Die Software der Projekte veraltet und die Sicherheit der Server ist dadurch gefährdet.
  * Frage: Wie können wir solche Projekte zukunftsfähig machen und erhalten.
  * Ansatz: Statische Seiten


## VLP

  * Das VLP wurde als Beispiel für die Statifizierung ausgewählt, weil 
    * das Projekt verwaist ist
	* es aber immer noch viel augerufen wird
	* die darunterliegende Serversoftware (Zope) veraltet ist und nicht mehr gewartet wird
  * Das Projekt soll einen *proof of concept* liefern, ob und wie solch eine Website statifiziert werden kann.
  
## Schritte

  1. Auswahl eines zukuntfsfähigen Layouts (Responsives Design/Rechner,Tablet,Handy)
  1. Auswahl einer hinreichend schnellen Template-Engine 
  1. Daten sollen in reinen YAML, JSON oder TOML Dateien vorliegen (Trennung von Daten und Layout)
  1. Implentierung der Template-Engine und Verknüpfung mit den Daten
  1. Testlauf
  1. Dokumentation