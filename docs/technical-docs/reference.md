---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .no_toc }
# Reference documentation

## Anmelden und Registrieren

### `index()`
+ **Route:** `/`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Anmeldeseite an.
+ **Sample output:**

![route1](../assets/images/route1.png "Anmeldeseite")

### `register_page()`
+ **Route:** `/register-page`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Registrierungsseite an.
+ **Sample output:** 

![route2](../assets/images/route2.png "Registrierungsseite")

---

## Startbildschirm anzeigen

### `home()`
+ **Route:** `/home`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Startseite des Benutzers an, sowie Benutzerinformationen, Fortschritt und Reisen.
+ **Sample output:** 

![route3](../assets/images/route3.png "Startseite")

---

## Reisen Anzeigen, Bearbeiten und Hinzufügen

### `reisen_page()`
+ **Route:** `/reisen`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Seite mit den allen Reisen des Benutzers an.
+ **Sample output:** 

![route4](../assets/images/route4.png "Reisen")

### `reise_page()`
+ **Route:** `/reise`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Details einer bestimmten Reise an. Wenn keine `trip_id` angegeben ist, wird eine Fehlermeldung angezeigt.
+ **Sample output:** 

![route5](../assets/images/route5.png "Reise")

### `reise_bearbeiten_page()`
+ **Route:** `/reise_bearbeiten`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Ermöglicht das Bearbeiten einer bestimmten Reise. Wenn keine `trip_id` angegeben ist, wird eine Fehlermeldung angezeigt.
+ **Sample output:** 

![route6](../assets/images/route6.png "Reise Bearbeiten")

### `reise_hinzufuegen_page()`
+ **Route:** `/reise_hinzufuegen`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Seite zum Hinzufügen einer neuen Reise an.
+ **Sample output:** 

![route7](../assets/images/route7.png "Reise Hinzufügen")

---

## Profil Anzeigen und Bearbeiten

### `profil_page()`
+ **Route:** `/profil`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Profilseite des Benutzers an.
+ **Sample output:** 

![route8](../assets/images/route8.png "Profilseite")

### `profil_bearbeiten_page()`
+ **Route:** `/profil_bearbeiten`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Ermöglicht das Bearbeiten des Profils. Bei Fehlern wird eine entsprechende Fehlermeldung angezeigt.
+ **Sample output:** 

![route9](../assets/images/route9.png "Profil Bearbeiten")

### `profilbilder_page()`
+ **Route:** `/profilbilder`
+ **Methods:** `GET`
+ **Purpose:** Zeigt die Profilbilderseite des Benutzers an.
+ **Sample output:** 

![route10](../assets/images/route10.png "Profilbilderseite")

### `set_profile_picture()`
+ **Route:** `/set_profile_picture`
+ **Methods:** `POST`
+ **Purpose:** Aktualisiert das Profilbild des Benutzers.
+ **Sample output:** 

---

## Bucketlist Erstellen, Updaten und Löschen

### `bucketlist_clicked()`
+ **Route:** `/bucketlist`
+ **Methods:** `GET`, `POST`
+ **Purpose:** Zeigt die Bucketlist des Benutzers an.
+ **Sample output:** 

![route12](../assets/images/route12.png "Bucketlist")

### `add_bucketlist_item()`
+ **Route:** `/add_bucketlist_item`
+ **Methods:** `POST`
+ **Purpose:** Fügt einen neuen Punkt zur Bucketlist des Benutzers hinzu.
+ **Sample output:** 

### `update_bucketlist_item()`
+ **Route:** `/update_bucketlist_item/<int:item_id>`
+ **Methods:** `POST`
+ **Purpose:** Aktualisiert den Status eines Bucketlist-Punkts.
+ **Sample output:** 

### `delete_bucketlist_item()`
+ **Route:** `/delete_bucketlist_item/<int:item_id>`
+ **Methods:** `POST`
+ **Purpose:** Löscht einen Punkt von der Bucketlist des Benutzers.
+ **Sample output:** 