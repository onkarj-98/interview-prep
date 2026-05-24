package main

import (
	"fmt"
	"sync"
)

// ── Contexts ──────────────────────────────────
type ValidateCtx struct{ Config string }

type ConfigCtx struct{ Progress map[string]int }

// ── Lifecycle interfaces ───────────────────────
// Validateble Node returns the Configurable node which is next step.
type ValidateableNode interface {
	Validate(ValidateCtx) (ConfigurableNode, error)
}

// Configurable Node returns the Runnable node which is next step.
type ConfigurableNode interface {
	Configure(ConfigCtx) (RunnableNode, error)
}
type RunnableNode interface {
	Start(stop <-chan struct{}) error
}

type RunnableGraph struct {
	nodes []ValidateableNode
}

// ── Follower — just Follow, nothing else ───────
type EntityFollower interface {
	Follow(in <-chan string)
}

// stage 1

type Scanner struct {
	out      chan string // channel Scanner writes INTO
	follower EntityFollower 
}

func NewScanner(f EntityFollower) *Scanner {
	out := make(chan string, 10)
	f.Follow(out)
	return &Scanner{out: out, follower: f}
}

func (s *Scanner) Validate(_ ValidateCtx) (ConfigurableNode, error) {
	fmt.Println("[Scanner] Validate")
	return s, nil
}

func (s *Scanner) Configure(_ ConfigCtx) (RunnableNode, error) {
	fmt.Println("[Scanner] Configure")
	return s, nil
}

func (s *Scanner) Start(stop <-chan struct{}) error {
	defer close(s.out)
	// actual logic
	for _, e := range []string{"alice", "bob", "charlie"} {
		select {
		case s.out <- e:
			fmt.Println("[Scanner] sent: ", e)
		case <-stop:
			return nil
		}
	}
	return nil

}

// stage 2
type Processor struct {
	in       <-chan string // here the data is coming from the some upstream,
	out      chan string // to the downstream, we process the business logic in Start() then push it to the downstream
	follower EntityFollower 
}

func NewProcessor(f EntityFollower) *Processor {
	out := make(chan string, 10)
	f.Follow(out)
	return &Processor{out: out, follower: f}
}

func (p *Processor) Follow(in <-chan string) {
	p.in = in
}

func (p *Processor) Validate(_ ValidateCtx) (ConfigurableNode, error) {
	fmt.Println("[Processor] Validate")
	return p, nil
}

func (p *Processor) Configure(_ ConfigCtx) (RunnableNode, error) {
	fmt.Println("[Processor ] Configure")
	return p, nil
}

func (p *Processor) Start(stop <-chan struct{}) error {
	defer close(p.out)
	for {
		select {
		case e, ok := <-p.in:
			if !ok {
				return nil
			}
			fmt.Println("Processor transformed:", e)

		case <-stop:
			return nil
		}
	}
}

// stage 3

type Writer struct {
	in <-chan string
}

func NewWriter() *Writer {
	return &Writer{}
}

func (w *Writer) Follow(in <-chan string) {
	w.in = in
}

func (w *Writer) Validate(_ ValidateCtx) (ConfigurableNode, error) {
	fmt.Println("[Writer]   Validate")
	return w, nil
}
func (w *Writer) Configure(_ ConfigCtx) (RunnableNode, error) {
	fmt.Println("[Writer]   Configure")
	return w, nil
}
  func (w *Writer) Start(stop <-chan struct{}) error {
        for {
                select {                                                                                                                                                                                  
                case e, ok := <-w.in:
                        if !ok {                                                                                                                                                                          
                                return nil                                                                                                                                                              
                        }
                        fmt.Println("[Writer]   written:", e)
                case <-stop:
                        return nil
                }
        }
}



  func NewRunnableGraph(nodes ...ValidateableNode) *RunnableGraph {
		return &RunnableGraph{nodes: nodes}
  }

  func (g *RunnableGraph) Run() {
		vctx := ValidateCtx{Config: "segment_id=1bcs"}
		cctx := ConfigCtx{Progress: map[string]int{"last_offset":500}}
		stop := make(chan struct{})

		fmt.Println("===== Validate and config ======")
		var runnables []RunnableNode
		for _, node := range g.nodes {
			configurable, err := node.Validate(vctx)
			if err != nil {
				fmt.Println("error", err)
				return
			}
			runnable, err := configurable.Configure(cctx)
			if err != nil {
				fmt.Println("error", err)
				return
			}
			runnables = append(runnables, runnable)
		}
		fmt.Println("======= START ========")
		var wg sync.WaitGroup
		for _, r := range runnables {
			wg.Add(1)
			r := r 
			go func() {
				defer wg.Done()
				r.Start(stop)
			}()
		}
		wg.Wait()
		fmt.Println("====Done===")

  }

  func ExportFactory() *RunnableGraph {
	writer := NewWriter()
	processor := NewProcessor(writer)
	scanner := NewScanner(processor)
	return NewRunnableGraph(scanner, processor, writer)
  }
  func main() {
	ExportFactory().Run()
  }

  // from handler to 