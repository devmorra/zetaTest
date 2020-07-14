#!/bin/bash
input="/home/runner/ZetaBashLab/names.txt"
output="/home/runner/ZetaBashLab/firstLetter.txt"
#read startingLetter
while IFS= read -r line
do
  #if the line starts with the letter we asked for then echo that
  #line into the new file
  #otherwise don't echo it into the new file
  #echo ${line:0:1}
  #if [ startingLetter == ${line:0:1} ]
  #then
  echo ${line:0:1} >> $output
  #fi
  #echo $line
done < $input
# < "$input"