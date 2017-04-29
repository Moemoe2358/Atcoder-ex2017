//2 つの正整数 A,B が与えられるので、その大小を比較してください。

import scala.util.control.Breaks

object Mainb extends App {
  val b = new Breaks
  var flag = false
  val str1 = readLine
  val str2 = readLine
  if (str1.length > str2.length) {
    println("GREATER")
    flag = true
  }
  if (str1.length < str2.length) {
    println("LESS")
    flag = true
  }
  if (!flag) {
    b.breakable {
      for (i <- 0 to str1.length - 1) {
        if (str1(i) > str2(i)) {
          println("GREATER")
          b.break
        }
        else if (str1(i) < str2(i)) {
          println("LESS")
          b.break
        }
        if (str1(i) == str2(i) && i == str1.length - 1) {
          println("EQUAL")
        }
      }
    }
  }
}
