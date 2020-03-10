import multiprocessing
import numpy as np

sequenceTarget = 3
printTarget = 200000
runLinearFlag = False
runWorkerFlag = True


def linearWorker():
    cycleWasteLinear = []
    for sequenceI in range(sequenceTarget):
        for subI in range(0, printTarget):
            badVar = np.sqrt(np.sin(subI))
            cycleWasteLinear.append(badVar)
            #print('Worker: linear  sequence: ' + str(sequenceI) + ' cycle: ' + str(subI))
        print("sequence: " + str(sequenceI) + " done.")
    print("linear done.")


def worker(workerNumber):
    """worker function"""
    cycleWasteList = []
    for workerI in range(0, printTarget):
        badVar = np.sqrt(np.sin(workerI))
        cycleWasteList.append(badVar)
        #print('Worker: ' + str(workerNumber) + ' cycle: ' + str(workerI))
    print("worker: " + str(workerNumber) + " done.")
    return


def runWorkers():
    jobs = []
    for i in range(sequenceTarget):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()


if __name__ == '__main__':
    if (runWorkerFlag == True):
        print("starting parallel computation...")
        jobs = []
        for i in range(sequenceTarget):
            p = multiprocessing.Process(target=worker, args=(i,))
            jobs.append(p)
            p.start()
    if(runLinearFlag == True):
        print("starting single core computation...")
        linearWorker()
