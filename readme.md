# Ammomaly
### A simple framework to use when trying real-time annomaly detection.

Ammomaly aims to provide a framework which can be used to detected changes in behavior.
The framework itself provides a (very) simple update loop which will test for changes every 'x' (insert timeunit).
The project started as an idea for a tool for blueteam CTF. 
When a new port opens, I want to run a full .pcap capture from the moment that port opens.
There are multiple scenario's which can be thought out this way, so I decided to write a 'framework' to handle these 'data-driven-triggers'.

The main idea is as follows:
- Define a method for the generation of the data.
- Define a method for a difference measurement between two data points/sets.
- Define an action to execute upon finding a difference.

### Local portscan

Using the above framework, each x (insert timeunit) new data is generated (which ports are open).
After this, a function is called to see if new ports are found.
Lastly start a tcpdump session based on the netflow data.

### Usage

Start the ammomaly.py with -m to load all the modules inside ammomaly_modules, without the -m argument it will load a manual function (which does the same if no new modules are added)

### Realized

- A basic implementation of the 'idea'.
- Dynamic importing using naming conventions in example_module.py. It will load all available (and correctly written) modules into ammomaly and will keep track of changes.

### Current limitations
- Very basic
- No concurrect threads
- No sophisticated 'time' implementation

### Future plans
- Building a stable-agent (correct errorhandling, testing etc.)
- Buildin log connectors (ES, RSYSlog, databases)
- Store results in database
- Front-end (flask)

