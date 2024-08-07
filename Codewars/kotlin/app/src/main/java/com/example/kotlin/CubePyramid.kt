package com.example.kotlin

/*
Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of n^3,
the cube above will have volume of (n-1)^3 and so on
until the top which will have a volume of 1^3.

You are given the total volume m of the building.
Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb, ...)
will be an integer m and you have to return the integer n such as
n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = m
if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
*/

import kotlin.random.Random // For custom test

// Finding n for volumeInput = n^3 + (n-1)^3 + ... + 1^3
fun findNb(volumeInput: Long): Long {
    var numberOfFloors: Long = 0L
    var volume: Long = volumeInput

    while (volume > 0) {
        numberOfFloors++
        volume -= (numberOfFloors * numberOfFloors * numberOfFloors)
    }

    if (volume == 0L && numberOfFloors > 0) {
        return numberOfFloors
    }

    return -1
}

// Custom test
fun main() {
    val randomInt: Long = Random.nextInt(1, 10000).toLong()
    var m: Long = 0L

    for (i in 1..randomInt) {
        m += (i * i * i)
    }

    val test: Long  = findNb(m)

    println("Volume of $m.")
    if (test == randomInt) {
        println("TEST PASSED")
    } else {
        println("/!\\TEST FAILED/!\\")
    }
    println("Number of floors: $randomInt")
}
