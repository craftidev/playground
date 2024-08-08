import 'package:flutter/material.dart';

// https://www.codewars.com/kata/5264d2b162488dc400000001/train/dart

class SpinWords extends StatelessWidget {
  const SpinWords({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Spin words'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
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
                '"Hey fellow warriors" --> "Hey wollef sroirraw"\n'
                '"This is a test --> "This is a test"\n'
                '"This is another test" --> "This is rehtona test"\n',
                style: TextStyle(fontSize: 16),
              ),
              GridView.count(
                shrinkWrap: true,
                crossAxisCount: 4,
                crossAxisSpacing: 8.0,
                mainAxisSpacing: 8.0,
                children: <Widget>[
                  TransformingButton(initialText: "This is reversed"),
                  TransformingButton(initialText: "This is not"),
                  TransformingButton(initialText: "crossAxisCount doesn't exist in Gridview - Nevermind just a const to delete"),
                  TransformingButton(initialText: "What a chance I don't have to care about ponctuation u_u"),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// Button with string to transform
class TransformingButton extends StatefulWidget {
  final String initialText;

  const TransformingButton({super.key, required this.initialText});

  @override
  _TransformingButtonState createState() => _TransformingButtonState();
}

// State/transformation on click
class _TransformingButtonState extends State<TransformingButton> {
  late String displayedText;
  late bool isTransformed;

  @override
  void initState() {
    super.initState();
    displayedText = widget.initialText;
    isTransformed = false;
  }

  void onClick() {
    setState(() {
      if (isTransformed) {
        displayedText = widget.initialText;
      } else {
        displayedText = transformText(displayedText);
      }
      isTransformed =!isTransformed;
    });
  }

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onClick,
      style: ElevatedButton.styleFrom(
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8.0),
        ),
      ),
      child: Text(
        displayedText,
        style: TextStyle(fontSize: 26),
      ),
    );
  }
}

// Transformation logic (REAL EXERCISE)
String transformText(String input) {
  List<String> listOfWords = input.split(' ');

  listOfWords.asMap().forEach((index, word) {
    if (word.length >= 5) {
      listOfWords[index] = word.split('').reversed.join('');
    }
  });

  return listOfWords.join(' ');
}
