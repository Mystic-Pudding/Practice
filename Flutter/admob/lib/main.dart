import 'package:flutter/material.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  MobileAds.instance.initialize();

  runApp(MyApp());
}
class MyApp extends StatefulWidget {
  const MyApp({ Key? key }) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}



class _MyAppState extends State<MyApp> {
  final String androidTestId = 'ca-app-pub-3940256099942544/6300978111';

  BannerAd? banner;

  @override
  void initState(){
    super.initState();
    banner = BannerAd(
      size: AdSize.banner,
      adUnitId: androidTestId,
      listener: BannerAdListener(),
      request: AdRequest(),
    )..load();
  }

  Widget build(BuildContext context) {
       return MaterialApp(
         home:  Scaffold(
      appBar: AppBar(
        title: Text('Admob'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.separated(
              itemBuilder: (_, index) {
                return Padding(
                  padding: EdgeInsets.all(16.0),
                  child: Container(
                    child: Text(index.toString()),
                  ),
                );
              },
              separatorBuilder: (c, index) {
                return Divider();
              },
              itemCount: 100,
            ),
          ),
          Container(
            height: 50.0,
            child: AdWidget(
              ad: banner!,
            ),
          ),
        ],
      ),
    )
);
  }
}