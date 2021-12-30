# Benchmark_Requests
<em>

```
Benchmark_Requests is a scripting tool to measure response time elapsed between a range of request with a specific bash script with curl
```
</em>

<br/>
<br/>

## How to run ##
<em>

```
Set the SCRIPT_PATH constant with yur own script with curl to run the requests.
```
</em>

```python
SCRIPT_PATH = "./<your-script>.sh"
```

<em>

```
Set the max number of iterations which will be the iterations of the requests execution.
```
</em>

```python
RATE_REQUESTS = 100
```
<em>

```
Set the VERBOSE constant to 0 if you dont want noise during the requests execution. By default is 1 so this means the script will print all the requests status.
```
</em>

```python
VERBOSE = 1
```