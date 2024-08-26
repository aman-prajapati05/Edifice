import multiprocessing
import time
from edifice import simple

# Function to generate multiples of a number
def generate_multiples(number, queue):
    while True:
        multiples = [number * i for i in range(1, 11)]  # Generate first 10 multiples
        queue.put(multiples)
        time.sleep(1)  # Sleep for a while before generating next set of multiples

# Function to update block with multiples
def update_block(block, queue):
    while True:
        multiples = queue.get()
        block.text = ', '.join(map(str, multiples))
        block.update()

# Create a multiprocessing queue
queue1 = multiprocessing.Queue()
queue2 = multiprocessing.Queue()

# Start processes for generating multiples of different numbers
process1 = multiprocessing.Process(target=generate_multiples, args=(2, queue1))
process2 = multiprocessing.Process(target=generate_multiples, args=(3, queue2))
process1.start()
process2.start()

# Create GUI blocks
app = simple.SimpleApp()

block1 = app.add_label("Multiples of 2:")
block2 = app.add_label("Multiples of 3:")

# Function to update blocks with multiples
def update_blocks():
    update_block(block1, queue1)
    update_block(block2, queue2)

# Run the GUI
app.set_timer(1000, update_blocks)
app.run()
