// lib/screens/exercise1.dart
import 'package:flutter/material.dart';

// https://www.codewars.com/kata/5264d2b162488dc400000001/train/dart

class Exercise1 extends StatelessWidget {
  const Exercise1({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Exercise 1'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: const <Widget>[
              Text(
                'Stop gninnipS My sdroW!',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(height: 16),
              Text(
                'Write a function that takes in a string of one or more words, '
                'and returns the same string, but with all words that have five or more letters reversed '
                '(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. '
                'Spaces will be included only when more than one word is present.\n\n'
                'Examples:\n'
                '"Hey fellow warriors"  --> "Hey wollef sroirraw"\n'
                '"This is a test        --> "This is a test"\n'
                '"This is another test" --> "This is rehtona test"\n',
                style: TextStyle(fontSize: 16),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
