#!/bin/bash
squareNumber () {
  squared=$(( $1 * $1 ))
  echo $squared
}
multiply () {
  product=$(( $1 * $2 ))
  echo $product
}
multiply 3 4
squareNumber 3
squareNumber 4
squareNumber 5
squareNumber 6