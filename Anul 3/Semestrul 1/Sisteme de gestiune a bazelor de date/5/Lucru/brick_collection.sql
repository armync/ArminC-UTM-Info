/*
-- rulare pe rand
-- create table my_brick_collection ( colour varchar2(10), shape varchar2(10), weight integer );
-- create table your_brick_collection ( height integer, width integer, depth integer, colour varchar2(10), shape varchar2(10) ); 
*/

/*
insert into my_brick_collection values ( 'red', 'cube', 10 ); 
insert into my_brick_collection values ( 'blue', 'cuboid', 8 );
insert into my_brick_collection values ( 'green', 'pyramid', 20 ); 
insert into my_brick_collection values ( 'green', 'pyramid', 20 ); 
insert into my_brick_collection values ( null, 'cuboid', 20 ); 
*/

/*
insert into your_brick_collection values ( 2, 2, 2, 'red', 'cube' ); 
insert into your_brick_collection values ( 2, 2, 2, 'blue', 'cube' ); 
insert into your_brick_collection values ( 2, 2, 8, null, 'cuboid' );
*/

desc my_brick_collection

select * from my_brick_collection;
select * from your_brick_collection;

select * from my_brick_collection union 
select * from your_brick_collection;

-- select cu mouse acest block si rulare
select colour, shape from my_brick_collection
union 
select colour, shape from your_brick_collection;

select colour, shape from my_brick_collection
union all
select colour, shape from your_brick_collection;

select distinct * from my_brick_collection;

select distinct shape from your_brick_collection;

select colour from my_brick_collection
union
select colour from your_brick_collection
order by colour;

select colour from my_brick_collection
union all
select colour from your_brick_collection
order by colour;

select colour, shape from my_brick_collection
minus
select colour, shape from your_brick_collection;

select colour, shape from your_brick_collection
intersect
select colour, shape from my_brick_collection;

select colour, shape from your_brick_collection
minus
select colour, shape from my_brick_collection;

select colour from my_brick_collection
intersect
select colour from your_brick_collection
order by colour;

