package main

import ("fmt"
		"net/http"
		"math"
		"math/rand")


func P1(){
	fmt.Println("welcome to GO!")
}

func P2(){
	fmt.Println("the square root of 4 is",math.Sqrt(4))
	fmt.Println("A number from 1-100",rand.Intn(100))
}


func add(x float64,y float64) float64 {
	return x+y
}
func multiple(a,b string) (string,string){
	return a,b
}
func p3(){
	//var num1,num2 float64 = 5.6,9.6
	num1,num2 := 5.6,9.5
	fmt.Println(add(num1,num2))
	w1,w2 := "Hey","There"
	fmt.Println(multiple(w1,w2))
}

func p4(){
	x := 15
	a := &x
	fmt.Println(a)
	fmt.Println(*a)
	*a = 5 
	fmt.Println(x)

	*a = *a**a // = (*a)*(*a) 
	fmt.Println(x)
	fmt.Println(*a)
	fmt.Println(a)
}


func index_handler(w http.ResponseWriter,r *http.Request){
	fmt.Fprintf(w,"Goal is neat!")
}

func about_handler(w http.ResponseWriter,r *http.Request){
	fmt.Fprintf(w,"first subweb for about ")
}
func p5(){
	http.HandleFunc("/",index_handler)
	http.HandleFunc("/about/",about_handler) //http://localhost:8000/about/ 
	http.ListenAndServe(":8000",nil)
	// how to see the result : open http://localhost:8000/ 
	// in chrome and you will see the print 
}
func main() {
/*	P1()
	P2()
	P3()
	p4()*/
	p5()

}