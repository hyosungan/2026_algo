#먼저 레어인거 찾아서
#parent_id에 그 아이디 있으면
#그놈의  ID,name, rarity 출력
with rare as (select * from ITEM_INFO where RARITY='RARE'),
mapping as (select * from item_tree where parent_item_id in (select item_id from rare))

select m.item_id,item_name,rarity  from mapping m join item_info i on m.item_id=i.item_id order by item_id desc