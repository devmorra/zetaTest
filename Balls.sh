echo "How many students are there in your class?"
tooManyBalls () {
    blueballs=$(( $1 - 5 ))
  echo "You have selected $blueballs too many blue balls."
  echo "Please enter a number less than 6"  
}

read numStudents
counter=$numStudents
while [ $counter != 0 ]
# Ask a user how many balls they want
do
  echo "What is your name"
  read name 
  studentnames+=$name
  while :
  do
    echo "How many blue balls do you want?"
    read blue
    if (( $blue <= 10 ))
      then
      break
    else
      echo "Please enter a number less than 10"
    fi
  done
  
  #then
  # tooManyBalls $(( blue ))
  #else
  totalblue=$(( totalblue + blue ))
  #fi
  echo "How many red balls do you want?"
  read red
  totalred=$(( totalred + red ))
  echo "How many yellow balls do you want?"
  read yellow
  totalyellow=$(( totalyellow + yellow ))
  totalballs=$(( totalballs + red + blue + yellow ))
  echo "$name want $blue blue balls, $red red balls and $yellow yellow balls for a total of $totalballs balls"
  counter=$(( counter - 1 ))
done
echo ""
echo ""
echo "$studentnames want "
echo "$totalblue blue balls"
echo "$totalyellow yellow balls"
echo "$totalred red balls"
echo ""


echo "We have $totalballs total balls"
