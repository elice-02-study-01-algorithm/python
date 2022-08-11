-- 코드를 입력하세요
SELECT SALES_CATEGORY from TOSS_SALES 
where ITEM_ID in (select ID from TOSS_ITEMS where ON_SALE=1)
group by SALES_CATEGORY
having avg(PRICE) < 500000
order by sum(AMOUNT) desc