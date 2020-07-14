#!bin/bash
# Ask a user their name
echo "Who do I have the pleasure to speak with?"
read name
echo "Hi, I am Philburt. Nice to meet you, $name"
if [ $name == "Tom" ]
then
  echo "$name you're late again"
else 
  echo "$name great job"
fi

# names is an array
names="Stan Kyle Cartman Veronica $name"
for name in $names
do
  echo $name
done
echo All done   

names2=( "Philburt" "Kiwi" "Hershey" "$name" "Thierno" )
#i=2
for i in ${names2[@]}
do
  echo $i
done
echo All done   

sentence1="I am having a good day sir!"
for word in $sentence1
do
  echo $word
done
echo All done   

sum=0
for x in {1..100}
do
  sum=$(( $sum + $x ))
  done
echo $sum

# Open or list files, using a for loop.
for file in $directory
do 
  echo $file
done
echo ALL done


#grab a ball
#if(green)
#  put in green bucket
#elif(red)
#  put in red bucket
#elif(blue)
#  put in blue bucket
#else
#  throw away





