
word0='\n'

print(word0)
##### 字串設定 #####
anyname = "這個是字串It's str.\n"
print(anyname)

print(word0)
##### 字串加總 #####
word1='中華'
word2='鋼鐵\n'
word3=word1+word2
print(word3)

print(word0)
#r###不能字串加數值###
interger=2002
#word4=word3+interger###不能字串加數值###
word4=word3+str(interger)
print(word4)

print(word0)
##### 字串長度計算 #####
count='我想要買中鋼，在23元的時候'
print(len(count))

print(word0)
##### 取字串 #####
word5='我覺得現在中鋼好像很便宜，可以下手'
print(word5[1:3])
print(word5[1:])
print(word5[:3])
print(word5[:-3])


print(word0)
###### 刪除前後空白 ######
word7 = ' hello apple '
print(word7.strip())

print(word0)
###### 刪除所有空白 ######
word6 = ' hello apple '
print(word6.replace(" ",""))
