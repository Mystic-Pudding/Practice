import CreateML
import Foundation

let dataFile = URL(fileURLWithPath: "/Users/mystic/Downloads/regression_test.csv")
let data = try MLDataTable(contentsOf: dataFile)
print(data.size)

let (trainData, testData) = data.randomSplit(by: 1, seed: 0)
print(trainData)
let params = MLBoostedTreeRegressor.ModelParameters(maxIterations:500)
let model = try MLBoostedTreeRegressor(trainingData: trainData, targetColumn: "solution", parameters : params)
let saveModel = MLModelMetadata(author: "mystic", shortDescription: ".", license: ".")
try model.write(to: URL(fileURLWithPath: "/Users/mystic/Downloads/regression_test.mlmodel"), metadata: saveModel)
