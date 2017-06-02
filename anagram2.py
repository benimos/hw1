import itertools
import bisect
dictionary_orig_copy = []
answer_list_tmp = []
answer_list = []

def SortDictionary(dic):
	for line in dic:
		dictionary_orig_copy.append([line.replace('\n',''), ''.join(sorted(list(line.replace('\n',''))))]) #original dictionary,sorted dictionary
	dictionary_orig_copy.sort(key=lambda x:x[1])

def Anagram_part(dictionary_orig_copy,chkword):
	for i in range(3,len(chkword)+1):
		for chkword_tuple in itertools.combinations(chkword,i):
			chkword2 = ''.join(sorted(list(chkword_tuple)))

			begin = 0
			end = len(dictionary_orig_copy)-1
			# t は中央番目の数
			t = (begin + end) // 2

			# 探索の下限のlowが上限のhighになるまで探索
			# lowがhighに達すると数は見つからなかったということ
			while (begin<=end):
			    if (chkword2==dictionary_orig_copy[t][1]):
			    	answer_list_tmp.append(dictionary_orig_copy[t][0])
			    	break
			    elif (chkword2 > dictionary_orig_copy[t][1]):
			    	begin = t + 1
			    elif (chkword2 < dictionary_orig_copy[t][1]):
			    	end = t - 1
			    t = (begin + end) // 2
			
			"""for j in range(len(dictionary_orig_copy)):
				if (chkword_list == dictionary_orig_copy[j][1]):
						answer_list_tmp.append(''.join(dictionary_orig_copy[j][0]))
						break"""

def Score(answer_list):
	twopoint_list = ['c','f','h','l','m','p','v','m','y','C','F','H','L','M','P','V','M','Y']
	threepoint_list = ['j','k','q','x','z','J','K','Q','X','Z']
	maxscore=0
	top_word=''
	for word in answer_list:
		answerscore = 0
		for k in word:
			if(k in twopoint_list):
				answerscore += 2
			elif(k in threepoint_list):
				answerscore += 3
			else:
				answerscore += 1
		if(answerscore > maxscore):
			maxscore = answerscore
			top_word = word
	print (top_word)


wordin=input('Enter anagram:')
f=open('dictionary.txt', 'r')
SortDictionary(f)
Anagram_part(dictionary_orig_copy,wordin)
answer_list = list(set(answer_list_tmp))
Score(answer_list)
f.close()
