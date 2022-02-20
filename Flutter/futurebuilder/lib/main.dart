import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Future Builder Example'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              '이곳은 데이터 상관없이 불려져 오는 곳입니다.',
              style: TextStyle(fontSize: 20),
            ),
            FutureBuilder(
                future: _fetch1(),
                builder: (BuildContext context, AsyncSnapshot snapshot) {
                  //해당 부분은 data를 아직 받아 오지 못했을때 실행되는 부분을 의미한다.
                  if (snapshot.hasData == false) {
                    return CircularProgressIndicator();
                  }
                  else {
                    return Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(
                        snapshot.data.toString(),
                        style: TextStyle(fontSize: 15),
                      ),
                    );
                  }
                })
          ],
        ),
      ),
    );
  }

  Future<String> _fetch1() async {
    await Future.delayed(Duration(seconds: 2));
    return 'Call Data';
  }
}