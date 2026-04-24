with milk as (select cart_id from CART_PRODUCTS where name='Milk'),
yogurt as (select cart_id from CART_PRODUCTS where name='Yogurt')

select distinct(m.cart_id) from milk m join yogurt y on m.cart_id=y.cart_id order by m.cart_id