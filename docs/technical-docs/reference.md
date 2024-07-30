---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .no_toc }
# Reference documentation

## Anmelden und Registrieren

### `index()`
**Route:** `/`
**Methods:** `GET`, `POST`
**Purpose:** Zeigt die Anmeldeseite an.
**Sample output:**

![users](../assets/images/users.png "users-Tabelle")

 ### `register_page()`
**Route:** `/register-page`
**Methods:** `GET`, `POST`
**Purpose:** Zeigt die Registrierungsseite an.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

—

## Startbildschirm anzeigen

### `home()`
**Route:** `/home`
**Methods:** `GET`, `POST`
**Purpose:** Zeigt die Startseite des Benutzers an, sowie Benutzerinformationen, Fortschritt und Reisen.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

—

## Reisen Anzeigen, Bearbeiten und Hinzufügen

### `reisen_page()`
**Route:** `/reisen`
**Methods:** `GET`, `POST`
**Purpose:** Zeigt die Seite mit den allen Reisen des Benutzers an.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

### `reise_page()`
**Route:** `/reise`
**Methods:** `GET`, `POST`
**Purpose:** Zeigt die Details einer bestimmten Reise an. Wenn keine `trip_id` angegeben ist, wird eine Fehlermeldung angezeigt.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

### `reise_bearbeiten_page()`
**Route:** `/reise_bearbeiten`
**Methods:** `GET`, `POST`
**Purpose:** Ermöglicht das Bearbeiten einer bestimmten Reise. Wenn keine `trip_id` angegeben ist, wird eine Fehlermeldung angezeigt.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

### `reise_hinzufuegen_page()`
**Route:** `/reise_hinzufuegen`
**Methods:** `GET`, `POST`
**Purpose:** Zeigt die Seite zum Hinzufügen einer neuen Reise an.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

—

## Profil Anzeigen und Bearbeiten

### `profil_page()`
**Route:** `/profil`
**Methods:** `GET`, `POST`
**Purpose:** Zeigt die Profilseite des Benutzers an.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

### `profil_bearbeiten_page()`
**Route:** `/profil_bearbeiten`
**Methods:** `GET`, `POST`
**Purpose:** Ermöglicht das Bearbeiten des Profils. Bei Fehlern wird eine entsprechende Fehlermeldung angezeigt.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")

### `profilbilder_page()`
**Route:** `/profilbilder`
**Methods:** `GET`
**Purpose:** Zeigt die Profilbilderseite des Benutzers an.
**Sample output:** 

![users](../assets/images/users.png "users-Tabelle")