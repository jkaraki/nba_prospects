library(tidyverse)

player_data_2008$X <- NULL
player_data_2008[28:35] <- list(NULL)
colnames(player_data_2008) <- c('Yr','Cls','Ht','Player','Team','Conf',
                                'G','Min%', 'PRPG!','GBPM', 'ORtg', 'Usg', 'eFG', 'TS', 'OR',
                                'DR','Ast', 'TO','Blk','Stl', 'FTR','FT_raw','FT_pct',
                                '2P_raw', '2P_pct','3P_raw', '3P_pct' ) 
final_player<-subset(player_data_2008, !Conf=="")
i = 1
while  (i < 5779)
{
  if (!is.na(final_player$Yr[i]))
  {
    year = final_player$Yr[i]
    cls = final_player$Cls[i]
    ht = final_player$Ht[i]
    name = final_player$Player[i]
  } 
  else
  {
    final_player$Yr[i] = year 
    final_player$Cls[i] = cls 
    final_player$Ht[i] = ht 
    final_player$Player[i] =  name
  }
  i = i+1
  
}


draft_data$X <- NULL
merged <-final_player %>%
  inner_join(draft_data, by=c("Player"))





