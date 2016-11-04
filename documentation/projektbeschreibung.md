% Projektbeschreibung
% Angelique Gößl

## Ausgangszustand

Am MPIWG gibt viele Webprojekte, die verwaist sind, weil die dafür verantwortlichen Wissenschaftler das Institut verlassen haben. Dadurch werden sie weder gepflegt noch erfährt die zugrundeliegende Server-Software die oft dringend notwendigen (Sicherheit) Updates. Außerdem entspricht das Design der Anwendungen nicht mehr den heutigen Ansprüchen, da veraltet. Insbesondere auf neueren Geräten (Tablet, Smartphone, Konsole) sind die Anwendungen nicht richtig zu bedienen. 

Das Virtuelle Laboratorium für Physiologie (VLP) ist solch ein verwaistes Projekt, das schon seit etlichen Jahren nicht mehr betreut wird, aber dennoch sehr pobulär ist und nach den Serverstatisiken des Instituts sehr hohe Zugriffszahlen besitzt. Daher 
die Idee, das VLP als Prototypen für eine Fallstudie auszuwählen, wie man solch verwaiste Projekte zukunftssicher weiter zugänglich machen kann, ohne dass ein größerer Wartungsaufwand anfällt.

## Ziele

Dem VLP als verwaistem Projekt werden keine neuen Inhalte mehr zugefügt, ist es also ein statisches Projekt. Daher liegt die Idee nahe, das Projekt als statische Seiten im Web zu präsentieren. Statische Seiten haben einmal den Vorteil, dass sie außer dem eigentlichen Server keine Applikationssoftware mehr benötigen. Dadurch entfallen Wartungs- und Sicherheitsupdates. 

Ziel des Projektes ist es, im Rahmen einer Fallstudie zu untersuchen, mit welchen Methoden und Werkzeugen das VLP, aber auch andere verwaiste Projekte des Instituts in statische Seiten überführt werden können.

Zweites Ziel ist es, durch eine Trennung von Inhalt (Daten) und Layout zu erreichen, dass die Seiten den modernen Anfoderungen (responsives Design) genügen und zukünftige Anforderungen bestenfalls nur eine Änderung in den Stylesheets (CSS) benötigen.

Die Fallstudie soll entsprechend dokumentiert werden, um den Mitarbeitern, die zukünftigt Ähnliches vorhaben, eine Handreichung bieten zu können.

## Methoden und Werkzeuge

Daher soll die Fallstudie prototypisch alle Werkzeuge nutzen, die ein reales Projekt benötigt. Reale Projekte besitzen in der Regel einen viel größeren Umfang und müssen daher von mehreren Mitarbeitern gemeinsam bearbeitet werden. 

  * Das Projekt wird mit einem Versionskontrollsystem (Git mit GitHub) durchgeführt.
  * Zentrales Werkzeug des Projektes ist ein Texteditor, in diesem Falle TextMate 2 (Begründung weiter unten) 
  * Die Dokumentation des Projektes wird mithilfe von Markdown durchgeführt, die mit Pandoc und einigen Skripten nach HTML und PDF herausgeschrieben wird.
  * Herausgeschrieben werden die statischen Seiten mithilfe einer Template Engine, da dieser Vorgang mehr oder weniger automatisert ablaufen soll.

Als Template Engines wurden drei unterschiedliche ausgewählt, um vergleichen zu können, welche für solch ein Projekt die geeignetsten sind. Ausgewählt wurden
  
  1. Hugo, eine Template Engine, die in Googles Programmiersprache Go geschrieben wurde und sehr schnell sein soll,
  2. Das Perl Template Toolkit, eine Template Engine, die schon einige Jahre existiert, als sehr ausgereift gilt und die ebenfalls -- da sie die Templates nach Perl kompiliert -- sehr schnell ist,
  3. RubyFrontier -- diese Template Engine wurde aus historischen Gründen ausgewählt, da das VLP in seiner ersten Fassung mit dem RubyFrontier-Vorgänger Frontier erstellt wurde.
  
## Geplante Vorgehensweise

Als erstes soll die Arbeitsumgebung komplett eingerichtet werden, danach wird ein Prototyp entwickelt, der einen Ausschnitt des VLPs aufnimmt. Dieser Prototyp soll schon die geplante Trennung von Inhalt und Design besitzen.

Danach werden die Templates für die oben genannten drei Template Engines erstellt und getestet. 

Mithilfe eines Skriptes wird dann ein hinreichend großer Testdatenbestand erzeugt und mit ihm dann Benchmarks gefahren, um die Geschwindigkeit, mit der die Engines die Seiten herausrendern zu vergleichen.

Als letztes soll eine Vergleichsmatrix aufgestellt werden, die die Vor- und Nachteile der einzelnen Werkzeuge aufzählt und gegebenenfalls Empfehlungen ausspricht. 

Falls einer der geplanten Wege sich tatsächlich eignet, das VLP und andere verwaiste Projekte zukunftssicher zu machen, soll dies in der Projektbeschreibung dokumentiert und eine Handreichung für die betroffenen Mitarbeiter des Instituts erstellt werden.  