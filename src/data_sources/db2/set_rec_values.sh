# Open Bash in container
sudo docker exec -it db2 bash -c "sudo docker exec -it db2 bash -c 'su - db2inst1'"

# Connect to TESTDB
db2 "connect to testdb" >> log.txt

# Drop SHIRTS table if it exists
db2 "DROP TABLE IF EXISTS SHIRTS;" >> log.txt

# Create SHIRTS table
db2 "CREATE TABLE SHIRTS (
  ORDER_ID INTEGER NOT NULL PRIMARY KEY,
  NAME VARCHAR(200),
  GENDER CHAR(1),
  AGE INTEGER,
  SIZE CHAR(2),
  STYLE VARCHAR(200),
  CITY VARCHAR(200),
  ZIP_CODE CHAR(5)
);" >> log.txt

# Insert 10000 rows into SHIRTS table
db2 "BEGIN
  DECLARE i INTEGER DEFAULT 1;
  WHILE i <= 10000 DO
    INSERT INTO SHIRTS (ORDER_ID, NAME, GENDER, AGE, SIZE, STYLE, CITY, ZIP_CODE)
    VALUES (
      i,
      'Name' || i,
      CASE MOD(i, 2) WHEN 0 THEN 'M' ELSE 'F' END,
      MOD(i, 100),
      CASE MOD(i, 3) WHEN 0 THEN 'S' WHEN 1 THEN 'M' ELSE 'L' END,
      'Style' || MOD(i, 100),
      'City' || MOD(i, 100),
      LPAD('ZIP' || MOD(i, 1000)::char(5), 5, '0')
    );
    SET i = i + 1;
  END WHILE;
END;"  >> log.txt

# Select the count of rows in SHIRTS table
db2 "SELECT COUNT(*) as COUNTS FROM SHIRTS" > count_shirts.txt >> log.txt
