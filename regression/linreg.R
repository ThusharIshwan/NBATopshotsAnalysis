options(max.print = 5000)
files <- list.files(path="data/txn_data/play_consolodated", pattern="*.csv", full.names=TRUE, recursive=FALSE)

big_data <- read.csv(files[1])
for (x in files) {
  if (x != files[1]){
    big_data <- rbind(big_data, read.csv(x))
  }
}


big_data$logprice = log(big_data$price)
big_data$editionPerc = big_data$editionSupply/big_data$playSupply

big_data$player_date = paste(big_data$player, big_data$date)
big_data$playtype_date = paste(big_data$playType, big_data$date)
big_data$playID_date = paste(big_data$playID, big_data$date)


na_free_data = na.omit(big_data)
sole_edition_free_data = na_free_data[na_free_data$editionID != "-1", ]  



#Set 1 Regressions:

supply_reg1 = lm(logprice ~ editionSupply, data=na_free_data)
supply_reg2 = lm(logprice ~ playSupply, data=na_free_data)
supply_reg3 = lm(logprice ~ typeSupply, data=na_free_data)
supply_reg4 = lm(logprice ~ playerSupply, data=na_free_data)
supply_reg5 = lm(logprice ~ editionSupply +playSupply+ typeSupply + playerSupply, data=na_free_data)


#Set 2 Regressions:

pop_reg1 = lm(logprice ~ salary, data= na_free_data)
pop_reg2 = lm(logprice ~ followers, data= na_free_data)
pop_reg3 = lm(logprice ~ pie, data= na_free_data)
pop_reg4 = lm(logprice ~ salary + followers + pie, data= na_free_data)

#Set 3 Regressions:

simple_reg = lm(logprice ~ editionSupply + editionPerc, data= na_free_data)
date_fixed_reg = plm(logprice ~ editionSupply + editionPerc, index="date", model="within",data = na_free_data)
player_indicator_reg = lm(logprice ~ editionSupply + editionPerc + followers + pie, data=na_free_data)
player_fixed_reg = plm(logprice ~ editionSupply + editionPerc, index="player", model="within",data = na_free_data)
player_date_fixed_reg = plm(logprice ~ editionSupply + editionPerc, index="player_date", model="within", data = na_free_data)
type_fixed_reg = plm(logprice ~ editionSupply + editionPerc, index="playType", model="within",data = na_free_data)
type_date_fixed_reg = plm(logprice ~ editionSupply + editionPerc, index="playtype_date", model="within", data = na_free_data)


#Set 4 Regressions:

play_fixed_reg = plm(logprice ~ editionPerc, index="playID", model="within",data = sole_edition_free_data)
play_date_fixed_reg = plm(logprice ~ editionPerc, index="playID_date", model="within",data = sole_edition_free_data)




# From here, take the summary

summary(simple_reg)





