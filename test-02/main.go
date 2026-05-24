package main 

type Job struct {
	ID int 
	Partition string
	Attempts int 
}

type JobResult struct {
	JobID int 
	Success bool
}

func runPipeline(workerID)
