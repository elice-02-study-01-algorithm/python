select TITLE 
from VIDEOS 
where MPAA_RATE='G' and 
    RATE=(select max(RATE) from VIDEOS where MPAA_RATE='G')