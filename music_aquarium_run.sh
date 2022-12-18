# backup.sh
#!/bin/bash

# 1. 백업 파일 이름을 만들 때 필요한 시간
echo "sync date and clock from time server"
rdate -s time.bora.net && clock -w
dat=`date +%Y-%m-%d_%H%M`

# 2. db 이름
# argv[1] = dbNames 로 db 이름 받아옴 
classification=$(python3 classification.py classification)
#echo $DBNames

for db in $classification;
do
  # if tonality == major
  if [ $db = "False" -o $db = "local" ]; then
    python3 ./music_aquarium/Fish-Bowl/index_major.html $db
  # if tonality == minor
  else
    python3 ./music_aquarium/Fish-Bowl/index_minor.html $db
    
  fi
done