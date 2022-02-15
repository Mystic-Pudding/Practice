import 'package:flutter/material.dart';
import 'diary.dart';

class Servey extends StatelessWidget {
  const Servey({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Text("Survey")) 
      );
  }
}