# Complementary_exercises


SQL

cmd
create schema my_schema;
create table my_schema.todo(id serial, prio int, comment varchar(100));
set search_path to my_schema;

select * from my_schema.todo;
insert into my_schema.todo (prio, comment) values ... ;
alter table my_schema.todo add column status varchar(10);

Task: insert values into my_schema.todo:
• prio 1: buy pie soup
• prio 2: buy tooth paste
Task: add a column status to my_schema.todo, and set the statuses:

update todo status = 'Done' where id = 1;
update todo status = 'not done' where id = 2;

• buy pie soup: DONE
• buy tooth paste: not done

UPDATE TABLE_NAME
SET COLUMN_VALUE 
= CASE COLUMN_NAME
WHEN 'COLUMN_NAME1' THEN COLUMN_VALUE1
WHEN 'COLUMN_NAME2' THEN COLUMN_VALUE2
ELSE COLUMN_VALUE
END
WHERE BAND_NAME IN('COLUMN_NAME1', 'COLUMN_NAME2');