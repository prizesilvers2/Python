# 파일을 여러번 실행해주고 싶을 때
import sys

print(sys.argv)

# python sys1.py new.txt src.txt
# new.txt --> src.txt

fr = open(sys.argv[1], "r")
fw = open(sys.argv[2], "w")

for line in fr :
    fw.wirte(line)
    
fw.close()
fr.close()