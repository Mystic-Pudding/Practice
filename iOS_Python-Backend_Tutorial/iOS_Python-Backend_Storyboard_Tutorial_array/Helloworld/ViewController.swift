//
//  ViewController.swift
//  Helloworld
//
//  Created by mystic on 2021/06/06.
//

import UIKit

class ViewController: UIViewController {
    var data = test(name: ["first"], old: "0",length: 0)
    var search_url = "http://127.0.0.1:5000/"
    var chageable = "false"
    var title_array = [String]()
    
    func getData(){
        let urlString = search_url
        let url = URL(string: urlString)
        
        URLSession.shared.dataTask(with: url!){data,_, error in
            DispatchQueue.main.async {
                if let data = data{
                    do {
                        let decoder = JSONDecoder()
                        let decodeData = try decoder.decode(test.self, from: data)
                        self.data = decodeData
                    } catch {
                        print("error")
                    }
                }
            }
            
        }.resume()
    }
        @IBOutlet var space: UILabel!
    @IBOutlet var changeabletext: UILabel!
    
    @IBAction func btnstart(_ sender: UIButton) {
        var  sumstring = ""
        for i in 0..<data.length{
            if (i==0){
                sumstring = sumstring + data.name[i]
            }
            else{
                sumstring = sumstring + "," + data.name[i]
            }
        }
                search_url="http://127.0.0.1:5000/"
                self.getData()
                space.text = sumstring + ","+data.old
        changeabletext.text="Changeable:"+self.chageable
    }
    
    @IBAction func btnchange(_ sender: UIButton) {
        var sumstring_change = ""
        for i in 0..<data.length{
            if (i==0){
                sumstring_change = sumstring_change + data.name[i]
            }
            else{
                sumstring_change = sumstring_change + "," + data.name[i]
            }
        }
                search_url="http://127.0.0.1:5000/?name=hello&old=15"
                self.getData()
                chageable = "true"
                space.text = sumstring_change + "," + data.old
        changeabletext.text="Changeable:"+self.chageable
        
    }
    
    
    
    
//    @IBOutlet var space: UILabel!
//
//
//
//    @IBAction func start(_ sender: UIButton) {
//        search_url="http://127.0.0.1:5000/"
//        self.getData()
//        space.text=data.name+data.old
//
//
//    }
    
//    @IBAction func change(_ sender: UIButton) {
//        search_url="http://127.0.0.1:5000/?name=hello&old=15"
//        self.getData()
//        chageable = "true"
//        space.text=data.name+data.old
//        
//        
//        
//    }
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


}

