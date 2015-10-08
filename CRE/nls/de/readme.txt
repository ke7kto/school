###################################################################
#
#    Citrix Receiver für Linux, Version 11.x
#
#    Copyright 1996-2009 Citrix Systems, Inc. Alle Rechte vorbehalten.
#
###################################################################

Diese Datei enthält aktuelle Informationen über
den Citrix Receiver für Linux.

Informationen zu neuen Funktionen und Systemanforderungen finden Sie in der
Administratordokumentation für den Citrix Receiver für Linux Version 11.x.

Bitte lesen Sie diese Datei vor der Installation und Verwendung des Citrix
Receivers für Linux komplett durch. Die Datei enthält wichtige Informationen,
die ggf. aktueller als andere in der Dokumentation enthaltene Angaben sind.

Die neuesten Informationen zu diesem Produkt und anderen Produkten
von Citrix Systems, Inc. finden Sie auf der Website unter:

http://www.citrix.com/

1.  Inhalt
============

Abschnitt 2 - Dokumentation
Abschnitt 3 - Support
Abschnitt 4 - Bekannte Probleme
Abschnitt 5 - Kontaktinformationen

2.  Dokumentation
=================

Dieses Dokument enthält wichtige aktuelle Informationen und Hinweise zu
bekannten Problemen mit dem Citrix Receiver für Linux Version 11.x. 

Informationen zum Installieren und Konfigurieren des Citrix Receivers für
Linux Version 11.x finden Sie in der Administratordokumentation für den Citrix
Receiver für Linux Version 11.x auf der Citrix Website
http://support.citrix.com/pages/docs/.

3.  Support
===================

Citrix bietet technischen Support hauptsächlich durch die Partner 
im CSN-Netzwerk (Citrix Solutions Network) an. Wenden Sie sich
für Support bitte zuerst an Ihren Vertragshändler oder ermitteln Sie
mit den Onlinesupportdiensten von Citrix den nächstgelegenen CSN-Partner.

Citrix bietet technische Supportdienste auf der Citrix Website
an. Auf der Supportseite finden Sie Links zu Downloads, zum
Citrix Knowledge Center, zu Citrix Consulting Services und
anderen Supportseiten.

4.  Bekannte Probleme
=====================

4.1  Maximieren und anschließendes Wiederherstellen von Seamless-Fenstern 
kann zu Anzeigefehlern führen 
----------------------------------------------------------------------------
Wenn Sie ein Seamless-Fenster über die Taskleiste maximieren und das Fenster 
anschließend über die Titelleiste wiederherstellen, kann die Anzeige fehlerhaft
sein. Sie vermeiden dieses Problem, indem Sie über die Taskleiste maximierte
Seamless-Fenster auch über die Taskleiste wiederherstellen und nicht über 
die Titelleiste.
[#143377]

4.2  Bei vereinfachtem Chinesisch als Gebietseingabeschema funktionieren
einige Tasten nicht in einigen Distributionen
----------------------------------------------------------------------------
Bei vereinfachtem Chinesisch als Gebietseingabeschema funktionieren die  
Pfeiltasten sowie die Tasten Pos1, Ende, Bild auf und Bild ab auf einigen 
Linux-Distributionen nicht. Sie können dieses Problem beheben, indem Sie
folgende Zeile aus der Datei module.ini des Clients entfernen:
UseLocalM=True
[#150369]

4.3  Im Dialogfeld 'Firewall' können nur ASCII-Zeichen eingegeben werden
-------------------------------------------------------------------------
In manchen alten Linux-Distributionen können im Dialogfeld 'Firewall' keine
Zeichen eingegeben werden, die nicht zum ASCII-Zeichensatz gehören. Wenn Sie
diese Zeichen in diesem Dialogfeld aktivieren möchten, kommentieren Sie die
folgenden Zeilen in der Ressourcendatei wfica im Installationsverzeichnis des
Clients aus oder entfernen Sie sie:

Wfica*ProxyAuthDialog.ProxyUsername*international: False
Wfica*ProxyAuthDialog.ProxyPassword*international: False

Hinweis: Aufgrund eines Drittanbieterproblems kann diese Lösung dazu führen,
dass der Client in einigen alten Linux-Distributionen unerwartet beendet wird,
wenn ein Benutzer in diesem Dialogfeld doppelklickt.
[#150143]

4.4  Im Verbindungsstatus-Dialogfeld wird das Euro-Zeichen nicht richtig angezeigt
----------------------------------------------------------------------------------
Wenn Sie sich mit einem Benutzernamen anmelden, der das Euro-Zeichen enthält,
wird dieses Zeichen im Verbindungsstatus-Dialogfeld im Connection Center nicht
richtig angezeigt. Momentan gibt es keine Lösung für dieses Problem.
[#151152]

4.5  Client wird unter Umständen nicht richtig gestartet, wenn en_GB.UTF-8 
unter SuSE 10.x verwendet wird
---------------------------------------------------------------------------
Bei Verwendung von en_GB.UTF-8 unter SuSE 10.x wird der Client u. U. nicht
richtig gestartet, wenn die Fallbackschriftartenspezifikation in der 
Schriftartenliste verwendet wird. Sie können die Ressourcendatei
Wfcmgr im Verzeichnis $ICAROOT/nls/{Sprache}/UTF-8 bearbeiten, um dieses 
Problem zu beheben. Ändern Sie die letzten zwei Zeilen im Abschnitt
Wfcmgr*fontList folgendermaßen:

-*-*-medium-r-*-*-*-120-75-75-c-*-*-*;\
-*-*-medium-r-*-*-*-120-*-*-c-*-*-*:

Hiermit legen Sie die Verwendung von Zeichen-Zellen (feste Zellengröße) fest
und verhindern so, dass die Fallbackschriftartenspezifikation verwendet wird.
[#151365]

4.6  Bei PowerPoint-Dateien auf zugeordneten Clientlaufwerken ist 
gleichzeitiger Zugriff möglich
------------------------------------------------------------------
Der Citrix Receiver für Linux unterstützt das Sperren von Dateien auf
zugeordneten Clientlaufwerken. Hierdurch wird gleichzeitiger Schreibzugriff auf
Dateien von Microsoft Word, Microsoft Excel sowie anderen Dokumenten auf
zugeordneten Laufwerken verhindert. Bei einigen Anwendungen wird mehrfacher
Zugriff jedoch durch das Öffnen von Dateien in Windows-Freigabemodi verhindert,
die auf UNIX-Plattformen nicht unterstützt werden. Aus diesem Grund wird unter
bestimmten Umständen gleichzeitiger Schreibzugriff auf Dateien von Microsoft
PowerPoint zugelassen, wenn dies nicht möglich sein sollte. Wenn gleichzeitiger
Zugriff auf PowerPoint-Dateien erforderlich ist, empfiehlt Citrix,
diese Dateien nicht auf einem zugeordneten Clientlaufwerk, sondern in
einem Dateisystem abzulegen, auf das vom Server aus zugegriffen werden kann.
[#151466]

4.7  Selektive Vertrauensstellung führt dazu, dass einige Proxyeinstellungen
nicht beachtet werden
-----------------------------------------------------------------------------
Bei selektiven Vertrauensstellungen sind nur Proxytypen zulässig, die keinen
Server angeben (also Auto, None und Wpad). Sichere und Socks-Proxyeinstellungen
werden nicht beachtet. Sie können dies ändern, indem Sie Trusted_Region.ini
bearbeiten. Die Datei enthält Kommentare mit Anleitungen hierzu.
[#199319]

4.8  Wiederverbindung mit virtuellen Desktops über das Citrix XenApp-Menü
ist nicht möglich
--------------------------------------------------------------------------
Sie können eine Verbindung zu einem virtuellen Desktop nicht mit der Option
'Citrix XenApp wiederverbinden' im Menü 'Citrix XenApp' wiederherstellen.
Alternativ dazu können Sie im Hauptfenster des Clients in der Ansicht
'Citrix XenApp' auf das Desktopsymbol für den virtuellen Desktop klicken,
zu dem Sie eine Verbindung herstellen möchten.
[#205538]

4.9  Große Dateien auf zugeordneten Clientlaufwerken haben eine Dateigröße von
null und können nicht verschoben werden
--------------------------------------------------------------------------------
Wenn Sie versuchen, eine große Datei von einem lokalen zugeordneten Laufwerk
in einen freigegebenen Serverordner zu verschieben, schlägt dies fehl und Sie
erhalten eine Fehlermeldung, dass die Datei nicht gefunden wurde. Wenn Sie
versuchen, die Datei zu öffnen, erhalten Sie dieselbe Fehlermeldung. In beiden
Fällen scheint die Dateigröße null zu sein. Beachten Sie, dass dieser Fehler
nur bei Dateien auftritt, die ursprünglich größer als 2 GB sind. 
[#199215] 

4.10 Multimediadateien funktionieren nicht richtig, wenn SpeedScreen-
Multimediabeschleunigung aktiviert ist
----------------------------------------------------------------------
Wenn SpeedScreen-Multimediabeschleunigung aktiviert ist, funktionieren
Multimedia-Dateien eventuell nicht richtig auf dem Client. Mediendatein werden
z. B. gar nicht wiedergegeben, das Medienplayer-Fenster wird nach der Suche
schwarz oder Audioinhalt wird nicht richtig synchronisiert oder nicht mit der
richtigen Geschwindigkeit abgespielt. Um dieses Problem zu umgehen, können Sie
die SpeedScreen-Multimediabeschleunigung auf dem Clientgerät deaktivieren.

Um SpeedScreen-Multimediabeschleunigung für alle Clientgeräte zu deaktivieren, 
setzen Sie in der Datei module.ini den Multimedia-Parameter auf 'Off'.

Um SpeedScreen-Multimediabeschleunigung für ein einzelnes Clientgerät zu
deaktivieren, setzen Sie in der Datei module.ini die Parameter
SpeedScreenMMAVideoEnabled und SpeedScreenMMAAudioEnabled auf 'Off'.
[#198305, 198337, 198369, 198370, 205952, 206253, 206304, 203605, 203607]

4.11 SpeedScreen-Multimediabeschleunigung funktioniert nicht auf 64-Bit-
Betriebssystemen
--------------------------------------------------------------------------------
Der Citrix Receiver für Linux benötigt 32-Bit-GStreamer-Codecs, damit
SpeedScreen-Multimediabeschleunigung ordnungsgemäß funktioniert. Um SpeedScreen-
Multimediabeschleunigung auf 64-Bit-Betriebssystemen zu verwenden, müssen
Sie vor der Installation des Citrix Receivers für Linux die entsprechenden
32-Bit-GStreamer-Codecs für Ihr Betriebssystem installieren.
[#201589] 

4.12 Anwendungen werden nach der Wiederverbindung nur auf einem einzigen
Monitor angezeigt
-------------------------------------------------------------------------
Wenn Sie eine Multimonitorumgebung verwenden und Anwendungen auf
unterschiedlichen Monitoren angezeigt werden, werden alle Anwendungen nach der
Wiederverbindung auf einem einzigen Monitor angezeigt. Dieses Problem tritt
nur beim Compiz-Fenstermanager auf.
[#201028]

4.13 Beim Maximieren von Anwendungen in Multimonitorumgebungen werden
Leerzeichen angezeigt
----------------------------------------------------------------------
Beim Maximieren von Anwendungen in Multimonitorumgebungen werden Leerzeichen 
angezeigt, wo normalerweise die Taskleiste des Betriebssystems ist.
[#200474]

4.14 Der Citrix Receiver für Linux kann möglicherweise auf 64-Bit-
Betriebssystemen nicht richtig installiert werden
-------------------------------------------------------------------
Der Citrix Receiver für Linux lässt sich möglicherweise auf 64-Bit-
Betriebssystemen nicht richtig installieren. Um dieses Problem zu umgehen,
müssen Sie vor der Installation des Citrix Receivers für Linux 32-Bit-Audio-
und X Server-Bibliotheken installieren.
[#200461]

4.15 Bekannte Probleme mit USB-Geräten
---------------------------------------
Eine Liste bekannter Probleme bei der Verwendung von USB-Geräten mit virtuellen
Desktops finden Sie unter http://support.citrix.com/article/CTX120090.
[#205817, 205818, 205819]

4.16 Leerzeichen im Installationspfad des Clients
--------------------------------------------------
Es können Probleme auftreten, wenn Sie versuchen, den Client in einem 
Verzeichnis zu installieren, dessen Pfad Leerzeichen enthält. Der
Installationspfad des Clients darf keine Leerzeichen enthalten.
[#206306]  

5.  Kontaktinformationen
========================

Citrix Systems, Inc.
851 West Cypress Creek Road
Fort Lauderdale, Florida 33309 USA
954-267-3000
http://www.citrix.com/

##################################################################

