---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Frontend Design Method

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: 23.06.2024

### Problem statement

Wir möchten, dass unsere Webseite ein bestimmtes Aussehen hat, um so auch die Funktionalitäten optimal zu gewährleisten. 
Wir wollten so früh wie möglich beginnen, damit es am Ende keinen Zeitdruck gibt.

Entscheidung getroffen von:

### Decision

Wir haben uns dafür entschieden, mit CSS zu arbeiten. 
Aus früheren Semestern kennen wir die grundlegende Struktur und Möglichkeiten davon. Dies hat es uns ermöglicht, auch schon vor der Vorlesung zum Thema User-Interface mit dem Projekt zu beginnen. Zudem lernen wir dieses Semester in diesem und auch anderen Kursen viele verschiedene neue Technologien kennen und konzentrieren uns daher lieber auf andere, die notwendiger sind wie Python und Flask.

### Regarded options

Wir haben zwischen CSS und Bootstrap überlegt.

| Criterion | CSS | Bootstrap |
| --- | --- | --- |
| **Know-how** | ✔️ Wir kennen die grundlegende Funktionsweise und Gestaltungsmöglichkeiten | ❌ Wir müssen uns mit der Implementierung, Verwendung und Gestaltung von vorne befassen |
| **Aussehen anpassen** | ❌ Alles muss grundlegend von vorne aufgebaut werden | ❔ Good: Es gibt schon eine große Anzahl an Vorlagen und Klassen, die einfach verwendet werden können, Bad: Man muss alles ausprobieren und testen, was welche Änderungen bewirkt |
| **Verwendung** | ✔️ Kann einfach verwendet werden, Datei muss nur in der html-Datei verlinkt sein -> kann so auch leicht gewechselt werden | ❌ Muss erst installiert und in das Projekt eingebunden werden | 

---

## [Example, delete this section] 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-Jun-2024

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

Our web application is written in Python with Flask and connects to an SQLite database. To complete the current project, this setup is sufficient.

We intend to scale up the application later on, since we see substantial business value in it.



Therefore, we will likely:
Therefore, we will likely:
Therefore, we will likely:

+ Change the database schema multiple times along the way, and
+ Switch to a more capable database system at some point.

### Decision

We stick with plain SQL.

Our team still has to come to grips with various technologies new to us, like Python and CSS. Adding another element to our stack will slow us down at the moment.

Also, it is likely we will completely re-write the app after MVP validation. This will create the opportunity to revise tech choices in roughly 4-6 months from now.
*Decision was taken by:* github.com/joe, github.com/jane, github.com/maxi

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ❔ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |

---
