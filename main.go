package main

import (
	"fmt"
	"sync"
)

type NumberFollower interface {
	Follow(in <- chan int)
}
type Generator struct {
	from int 
	to int
	out chan int
}

func NewGenerator(from, to int) *Generator {
	return &Generator{from: from, to: to}
}

func (g *Generator) SetFollower(f NumberFollower) {
	g.out = make(chan int, 10)
	f.Follow(g.out)
}

func (g *Generator) Start(wg *sync.WaitGroup) {
	defer wg.Done()
	defer close(g.out)
	
	for i := g.from; i <= g.to; i++ {
		fmt.Println("Sent Generator", i)
		g.out <- i
	}

}
 // --- stage 2: Doubler 
type Doubler struct {
	in <- chan int
	out chan int
}

func NewDoubler() *Doubler {
	return &Doubler{}
}
func (d *Doubler) Follow(in <-chan int) {
	d.in = in
}

func (d *Doubler) SetFollower(f NumberFollower) {
	d.out = make(chan int, 10)

	f.Follow(d.out)
}

func (d *Doubler) Start(wg *sync.WaitGroup) {
	defer wg.Done()
	defer close(d.out)
	for n := range d.in {
		result := n * 2
		fmt.Println("Doubler printing", result)
		d.out <- result
	}
}

// ---- Stage 3: printer

type Printer struct {
	in <- chan int
}

func NewPrinter() *Printer {
	return &Printer{}
}

func (p *Printer) Follow (in <- chan int) {
	p.in = in
}
func (p *Printer) Start(wg *sync.WaitGroup) {
	defer wg.Done()
	for n := range p.in {
		fmt.Println("Printer final value", n)
	}
}


func main() {
	gen := NewGenerator(1, 5)
	doubler := NewDoubler()
	printer := NewPrinter()

	// wire 
	gen.SetFollower(doubler)
	doubler.SetFollower(printer)

	// Run concurrently
	var wg sync.WaitGroup
	wg.Add(3)
	go gen.Start(&wg)
	go doubler.Start(&wg)
	go printer.Start(&wg)
	wg.Wait()
	fmt.Println("pipeline done")

}