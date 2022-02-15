import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
void main() {
  runApp(const MyApp());
}


class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {


    return MaterialApp(
      title: 'Welcome to Flutter',
      home: MyHomepage() 
      
    );
  }
}

class MyHomepage extends StatefulWidget {
  MyHomepage({Key? key, this.title}) : super(key: key);

  final String? title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomepage>{
  final ImagePicker picker = ImagePicker();
  PickedFile? _image;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
          floatingActionButton: FloatingActionButton(
            onPressed: getImage,
            child: Icon(Icons.add_a_photo),
          ),
          body:Center(child: 
          _image == null ? Text('no image selected') : Image.file(File(_image!.path))
          )
          )
          );

  }
Future getImage() async{
  PickedFile image = (await picker.pickImage(source: ImageSource.gallery)) as PickedFile;
  setState(() {
    _image = image;
  });
   }
}




