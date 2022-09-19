class info {
  constructor (color,plan,size){
    this.color = color
    this.plan = plan
    this.size = size
  }
  getFurniture(A){
    return this.plan + " info with a plan of " + this.color + " " + A
  }
}
const info1 = new info ("red", "single", " fifty")
const info2 = new info ("green", "multi", " hundred")

console.log()
console.log(info1)
console.log(info1.getFurniture("first"))

console.log()
console.log(info2)
console.log(info2.getFurniture("second"))
