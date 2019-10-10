# covpare
A program to compare the read coverages of two genome assemblies

## To Install
```
git clone git@github.com:deprekate/covpare.git
cd covpare
make
```

## Quick start
```sh
python covpare.py FILE1 FILE2
```

## Testing
To test whether your covpare install is working correctly, you can run the command:
```
python covpare.py tests/coverage1.tsv tests/coverage2.tsv
```


## Prepare input data    
You will need to create a coverage map.


## Output
If **covpare** ran correctly you should get an output image that should look like the image below:
![](https://github.com/deprekate/covpare/blob/master/figure.png)

