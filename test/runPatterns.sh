#!/bin/bash

ARGS=1
myFile=$1 
regSum=True #$2
realPattern=0
outputDir=~/scratch0
if [ $# -ne "$ARGS" ]
#if [ true ]
then
	echo "need to include a pattern name or a .txt file and True/False for region sums"
exit $EXIT_BADARGS
fi

if [[ $1 == *.txt ]]
    then
    while [ 1 ]
      do
      read line || break
      sh makePatternConfig.sh $line $regSum ; 
      echo "running pattern $line" 
      cmsRun rctPattern_cfg.py >& pattern.log; 
      if [ -e  $line\Input.txt ]; then
	  mv $line\Input.txt $outputDir/; 
	  mv $line.txt $outputDir/;
      else
	  echo "Files not made, pattern making unsuccessful, check pattern.log file"
      fi
    done < $myFile
else
    line=$1
    while [ 1 ]
      do      
      read fileLine || break
      if [ $fileLine == $line ]
	  then
	  realPattern=1;
      fi
    done < "patternList.txt"
    if [ "$realPattern" -eq "1" ]
	then
	if [[ $line == "random" && $2 == "many" ]]; then
	    maxRandom=40;
	    for ((num=30; num<$maxRandom; num++)); do
		
		sh makePatternConfig.sh $line $regSum ; 
		cmsRun rctPattern_cfg.py >& pattern.log; 
		if [ -e  $line\Input.txt ]; then
		    mv $line\Input.txt $outputDir/${line}${num}Input.txt; 
		    mv $line.txt $outputDir/${line}${num}.txt;
		else
		    echo "Files not made, pattern making unsuccessful, check pattern.log file"
		fi
	    done
	else
	    sh makePatternConfig.sh $line $regSum ;
	    echo "running pattern $line" 
	    cmsRun rctPattern_cfg.py >& pattern.log;
	    if [ -e  $line\Input.txt ]; then
		mv $line\Input.txt $outputDir/${line}Input.txt;
		mv $line.txt $outputDir/${line}.txt;
	    else
		echo "Files not made, pattern making unsuccessful, check pattern.log file"
	    fi
	fi
	else
	echo "NOT A REAL PATTERN TEST";
	echo "Choose from walkingOnes, walkingZeros, walkingOnesZeros, walkingOnes456, walkingZeros456, walkingOnesZeros456, cornerSharing, edges, intraEdges, testCard6, flooding, allTowers. zeroMax, regionSumPins0, regionSumPins1, regionSumPins2, regionSumPins3, test, zeros, count, testCrateNumber, random"
    fi
fi


#"walkingOnes"
#"walkingZeros"
#"walkingOnesZeros"
#"walkingOnes456"
#"walkingZeros456"
#"walkingOnesZeros456"
#"cornerSharing"
#"edges"
#"intraEdges"
#"testCard6"
#"flooding"
#"allTowers"
#"zeroMax"
#"regionSumPins0"
#"regionSumPins1"
#"regionSumPins2"
#"regionSumPins3"
#"testTO"
#"testCrateNumber"
#"zeros"
#"count"
#"test"

