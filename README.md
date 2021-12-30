# Benchmark_Requests
<div class="span">
    <span>
    Benchmark_Requests is a scripting tool to measure response time elapsed between a range of request with a specific bash script with curl
    </span>
</div>
<br/>
<br/>
<br/>

## How to run ##
<div class="span">
    <span>
    Set the SCRIPT_PATH constant with yur own script with curl to run the requests.
    </span>
</div>

```python
SCRIPT_PATH = "./<your-script>.sh"
```

<div class="span">
    <span>
    Set the max number of iterations which will be the iterations of the requests execution.
    </span>
</div>

```python
RATE_REQUESTS = 100
```
<div class="span">
    <span>
    Set the VERBOSE constant to 0 if you dont want noise during the requests execution. By default is 1 so this means the script will print all the requests status.
    </span>
</div>

```python
VERBOSE = 1
```

<style>
    div.span {
        min-width: 100px;
        background-color: rgba(30,30,30, .8);
        padding: 10px 8.5px;
        border-radius: 10px;
    }
    div > span {
        font-weight: 800;
        font-style: oblique;
        font-size: 1.1em;
    }
</style>